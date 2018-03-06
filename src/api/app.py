 # -*- coding: utf-8 -*-

from flask import Flask, jsonify, request

from src.api.schemas.product_schema import ProductSchema

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/api/predict', methods=['POST'])
def predict():
    json_data = request.get_json()
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400
    product = ProductSchema().load(json_data)
    if product.errors:
        return jsonify(product.errors), 422
    category = 'Cachorro, Rações, Ração Seca'
    return jsonify({'prediction': {'category': category}})

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')
