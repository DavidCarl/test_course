import json
from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api, request


app = Flask(__name__)
api = Api(app)

custOrder = []

@app.route('/')
def index():
    return render_template('layout.html')


@app.route('/orders')
def api_test():
    return render_template('orders.html')

class order(Resource):
    def get(self):
        print(custOrder)
        return jsonify(orders=custOrder)

    def post(self):
        json_data = request.get_json(force=True)
        order_obj = {'name': json_data['name'], 'pizza': json_data['pizza']}
        custOrder.append(order_obj)
        return jsonify(newdata=order_obj)

api.add_resource(order, '/makeOrder')

def main():
    app.run(debug=False, host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()
