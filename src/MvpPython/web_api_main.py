import json
from array import array

import numpy as np
import pandas as pd
from flask import Flask, jsonify, request, send_file
from flasgger import Swagger
from controller.web_api_handler import Handler

app = Flask(__name__)
swagger = Swagger(app)
handler = Handler()

global signatures

@app.route('/upload_image', methods=['POST'])
def upload_image():
    """
    Этот эндпоинт загружает изображение и возвращает его название
    ---
    parameters:
      - name: image
        in: formData
        type: file
        required: true
        description: Изображение для загрузки
    responses:
      200:
        description: Успешный ответ
    """
    global signatures
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})

    signatures = handler.get_captions_from_image(request.files['image'])

    return pd.Series(signatures).to_json(orient='values')

# Пример эндпоинта для принятия двух чисел и возврата строки
@app.route('/concatenate_numbers', methods=['POST'])
def concatenate_numbers():
    """
    Этот эндпоинт принимает два числа и возвращает строку
    ---
    parameters:
      - name: number1
        in: formData
        type: string
        required: true
        description: Первое число
      - name: number2
        in: formData
        type: string
        required: true
        description: Второе число
      - name: long_text
        in: formData
        type: string
        required: false
    responses:
      200:
        description: Успешный ответ
    """

    signatures = json.loads(request.form['long_text'])
    number1 = int(request.form['number1'])
    number2 = int(request.form['number2'])
    firstSignature = np.array(signatures[number1], dtype="uint8")
    secondSignature = np.array(signatures[number2], dtype="uint8")
    result = handler.compare_two_signatures(firstSignature,
                                            secondSignature)

    return str(result)

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    app.run(debug=True)
