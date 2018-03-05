 # -*- coding: utf-8 -*-

from flask import Flask, jsonify, request

from src.api.schemas.product_schema import ProductSchema

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

product_schema = ProductSchema()

@app.route('/api/predict', methods=['POST'])
def predict():
    json_data = request.get_json()
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400
    try:
        product = product_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    category = 'Cachorro/Roupas e Acessórios/Roupinhas de Inverno'
    return jsonify({'prediction': {'category': category}})

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')
