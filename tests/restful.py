from flask import Flask, request
from flask_restful import Resource,  Api
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token, jwt_required
from flask_cors import CORS

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'my_cool_secret'
jwt = JWTManager(app)
CORS(app)
api = Api(app)


class UserLogin(Resource):
    def post(self):
        username = request.get_json()['username']
        password = request.get_json()['password']
        if username == 'admin' and password == 'habr':
            access_token = create_access_token(identity={
                'role': 'admin',
            }, expires_delta=False)
            result = {'token': access_token}
            return result
        return {'error': 'Invalid username and password'}


class ProtectArea(Resource):
    @jwt_required
    def get(self):
        return {'answer': 42}


api.add_resource(UserLogin, '/api/login/')
api.add_resource(ProtectArea, '/api/protect-area/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
