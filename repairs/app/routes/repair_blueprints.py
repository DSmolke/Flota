from flask import Blueprint, Response, request
from sqlalchemy.exc import IntegrityError

from app.db.configuration import sa
from app.db.model import RepairModel
from app.validator.repair import repair_schema

repairs = Blueprint('repairs', __name__, url_prefix='/repairs')


@repairs.route('/by_car_id/<int:car_id>', methods=['GET'])
def get_by_car_id(car_id: int) -> Response:
    """
    :param car_id: The ID of the car for which repairs are requested.
    :return: A response object containing the repairs associated with the specified car ID.

    """
    repairs_by_car_id = RepairModel.get_all_by_car_id(car_id)
    if repairs_by_car_id:
        return {'car_id': car_id, 'repairs': repairs_by_car_id}, 200
    return {"message": "No repairs for that car_id"}, 404

@repairs.route('/pending', methods=['POST'])
def add_pending() -> Response:
    """
    Adds a new pending repair.

    :return: The JSON representation of the created repair,
             the HTTP status code 201 (Created), and
             the 'Content-Type' header set to 'application/json'.
    """
    request_data = request.get_json()
    try:
        repair_schema.validate(request_data)
        repair = RepairModel(**request_data)
        repair.save()
        return repair.as_dict(), 201, {'Content-Type': 'application/json'}

    except IntegrityError as e:
        sa.session.rollback()
        return {"message": e.orig.args[1]}, 403

    except ValueError or TypeError:
        return {"message": "Invalid request"}, 400

@repairs.route('/start_pending/<int:repair_id>', methods=['POST'])
def start_pending(repair_id: int) -> Response:
    """
    Starts a pending repair.

    :param repair_id: The ID of the repair.
    :type repair_id: int
    :return: The updated repair details or an error message.
    :rtype: dict or tuple
    """
    request_data = request.get_json()
    repair = RepairModel.get_by_id(repair_id)
    if repair and request_data:
        repair.repair_status = 2
        repair.approximate_duration = request_data.get('approximate_duration', 14)
        repair.save()
        return repair.as_dict(), 201
    return {"message": "Repair not found"}, 404

@repairs.route('/finish/<int:repair_id>', methods=['POST'])
def finish_repair(repair_id: int) -> Response:
    """
    Finish a repair by updating its status.

    :param repair_id: The ID of the repair.
    :type repair_id: int
    :return: The updated repair as a dictionary and HTTP status code 201 if the repair is found, otherwise a message dictionary and HTTP status code 404.
    :rtype: Response
    """
    repair = RepairModel.get_by_id(repair_id)
    if repair:
        repair.repair_status = 3
        repair.save()
        return repair.as_dict(), 201
    return {"message": "Repair not found"}, 404
