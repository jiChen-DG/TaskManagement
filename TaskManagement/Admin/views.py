from TaskManagement.model import Admin
from . import adminBP
from flask import jsonify, request
import TaskManagement.Admin.controller as controller


@adminBP.route('/login', methods=['POST'])
def login():
    code = 400
    msg = ''
    data = {}

    username = request.json.get('username')
    password = request.json.get('password')

    if(username and password):
        code = controller.login(username, password)
        if(code == 1):
            msg = 'Login Success'
            code = 200
        elif(code == 0):
            msg = 'Login Failed'

    return jsonify({'code': code, 'msg': msg, 'data': data})
