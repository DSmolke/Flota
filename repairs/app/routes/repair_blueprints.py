from flask import Blueprint, Response, request
from sqlalchemy.exc import IntegrityError

from app.db.configuration import sa
from app.db.model import RepairModel
from app.validator.repair import repair_schema

repairs = Blueprint('repairs', __name__, url_prefix='/repairs')


@repairs.route('/by_car_id/<int:car_id>', methods=['GET'])
def get_by_car_id(car_id: int) -> Response:
    pass

@repairs.route('/pending', methods=['POST'])
def add_pending() -> Response:
    pass

@repairs.route('/start_pending/<int:repair_id>', methods=['POST'])
def start_pending(repair_id: int) -> Response:
    pass

@repairs.route('/finish/<int:repair_id>', methods=['POST'])
def finish_repair(repair_id: int) -> Response:
    pass
