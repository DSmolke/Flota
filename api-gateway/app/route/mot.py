from flask import Blueprint, Response, request, jsonify
from app.security.configuration import token_required
import httpx
import logging
from pathlib import Path

mots_blueprint = Blueprint('mots_blueprint', __name__, url_prefix='/mots')
# @token_required(roles=['ADMIN'])
@mots_blueprint.route('/all')
def get_all() -> Response:
    res = httpx.get('http://mots-service:8002/mots/all')
    logging.info(res.json())
    return res.json(), res.status_code

@mots_blueprint.route('/<int:mot_id>', methods=['GET'])
def get_one_by_id(mot_id: int) -> Response:
    res = httpx.get(f'http://mots-service:8002/mots/{mot_id}')
    logging.info(res.json())
    return res.json(), res.status_code


@mots_blueprint.route('/', methods=["POST"])
def create_mot() -> Response:
    data = dict(request.form)
    file = request.files['file']
    filename = file.filename
    file.save(file.filename)
    aws_response = httpx.post(f'http://aws-resources-service:8003/file', files={'file': open(f'{filename}', 'rb')})
    Path.cwd().joinpath(filename).unlink()

    res = httpx.post('http://mots-service:8002/mots', json={**data, 'img_url': aws_response.json()['url']})
    return res.json(), res.status_code


@mots_blueprint.route('/<int:mot_id>', methods=['DELETE'])
def delete_mot(mot_id: int) -> Response:
    # TODO, czy trzeba to przerabiac
    mot_res = httpx.get(f"http://mots-service:8002/mots/{mot_id}")
    mot_data = mot_res.json()
    img_url = mot_data.get('img_url')
    if img_url:
        aws_response = httpx.request('DELETE', f'http://aws-resources-service:8003/file', json={"file": img_url})
        if aws_response.status_code == 201:
            res = httpx.delete(f'http://mots-service:8002/mots/{mot_id}')
            return res.json(), res.status_code
    return mot_res.json(), mot_res.status_code
