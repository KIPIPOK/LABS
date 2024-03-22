from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# GET эндпоинт /number/ в строку юрл пишем параметр =100
@app.route('/number/', methods=['GET']) # прописываем что это гет запрос
def get_number():

    param = float(request.args.get('param')) # получаем параметр из юрл

    number = random.random() * param # умножение рандом числа на параметр
    
    return jsonify({'Результат GET': number})

# POST 
@app.route('/number/', methods=['POST'])
def generate_number():
    data = request.json
    json_param = data['jsonParam']
    
    random_number = random.random()
    random_operation = random.choice(['Сложение', 'Вычитание', 'Умножение', 'Деление'])
    
    result = random_number + json_param if random_operation == 'Сложение' else \
             random_number - json_param if random_operation == 'Вычитание' else \
             random_number * json_param if random_operation == 'Умножение' else \
             random_number / json_param if json_param != 0 else None # Деление на 0 !!!!!!!!!!
    
    return jsonify({'Результат POST': result, 'Операция': random_operation})
    

# DELETE эндпоинт /number/
@app.route('/number/', methods=['DELETE'])
def delete_number():
    random_number = random.random()
    random_operation = random.choice(['Сложение', 'Вычитание', 'Умножение', 'Деление'])
    
    return jsonify({'Результат DELETE': random_number, 'Операция': random_operation})
    
