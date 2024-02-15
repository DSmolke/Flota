from flask import Blueprint, Response, request
from app.security.configuration import token_required
import httpx
import logging
from pathlib import Path

insurances_blueprint = Blueprint('insurances_blueprint', __name__, url_prefix='/insurances')
# @token_required(roles=['ADMIN'])
@insurances_blueprint.route('/all')
def get_all() -> Response:
    res = httpx.get('http://insurances-service:8004/insurances/all')
    logging.info(res.json())
    return res.json(), res.status_code

@insurances_blueprint.route('/<int:insurance_id>', methods=['GET'])
def get_one_by_id(insurance_id: int) -> Response:
    res = httpx.get(f'http://insurances-service:8004/insurances/{insurance_id}')
    logging.info(res.json())
    return res.json(), res.status_code


@insurances_blueprint.route('/', methods=["POST"])
def create_insurance() -> Response:
    data = dict(request.form)
    file = request.files['file']
    filename = file.filename
    file.save(file.filename)
    aws_response = httpx.post(f'http://aws-resources-service:8003/file', files={'file': open(f'{filename}', 'rb')})
    Path.cwd().joinpath(filename).unlink()
    res = httpx.post('http://insurances-service:8004/insurances', json={**data, 'img_url': aws_response.json()['url']})
    return res.json(), res.status_code


@insurances_blueprint.route('/<int:insurance_id>', methods=['DELETE'])
def delete_insurance(insurance_id: int) -> Response:
    insurance_res = httpx.get(f"http://insurances-service:8004/insurances/{insurance_id}")
    insurance_data = insurance_res.json()
    img_url = insurance_data.get('img_url')
    if img_url:
        aws_response = httpx.request('DELETE', f'http://aws-resources-service:8003/file', json={"file": img_url})
        if aws_response.status_code == 201:
            res = httpx.delete(f'http://insurances-service:8004/insurances/{insurance_id}')
            return res.json(), res.status_code
    return insurance_res.json(), insurance_res.status_code
