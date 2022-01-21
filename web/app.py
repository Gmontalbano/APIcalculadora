# projeto calculador com API

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

api = app = Flask(__name__)
api = Api(app)


def checkdata(data):
    if 'function' not in data:
        return 301.1, "Falta operação"
    else:
        function = data['function']
    if 'x' not in data or 'y' not in data:
        return 301, "Falta argumento"
    elif function == 'div':
        if data['y'] == 0:
            return function, 302, "Impossivel dividir por 0"
        else:
            return function, 200, "OK"
    else:
        return function, 200, "OK"


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


class Calculator(Resource):
    def post(self):

        data = request.get_json()
        op, code, message = checkdata(data)
        x = data['x']
        y = data['y']
        x = int(x)
        y = int(y)
        if code == 301:
            retjson = {
                'Code': code,
                'Message': message
            }
            return jsonify(retjson)
        if code == 301.1:
            retjson = {
                'Code': code,
                'Message': message
            }
            return jsonify(retjson)
        if code == 302:
            retjson = {
                'Code': code,
                'Message': message
            }
            return jsonify(retjson)
        if op == 'add':
            total = add(x, y)
        elif op == 'sub':
            total = sub(x, y)
        elif op == 'mult':
            total = mult(x, y)
        elif op == 'div':
            total = div(x, y)

        retjson = {
            'operação': op,
            'total': total,
            'Code': code,
            'Message': message
        }
        return jsonify(retjson)


api.add_resource(Calculator, "/calc")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0')


