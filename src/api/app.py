from flask import Flask, jsonify, request

from src.api.inputs.product_inputs import ProductInputs

app = Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
    inputs = ProductInputs(request)

    if not inputs.validate():
        return jsonify(success=False, errors=inputs.errors)

    category = 'Cachorro/Roupas e Acessórios/Roupinhas de Inverno'
    return jsonify({'prediction': {'category': category}})

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')
