import requests
import random

url = 'http://127.0.0.1:5000/number/'

random_param = random.randint(1, 10)
# Раздел 1

# # GET request
# result = requests.get(f'http://127.0.0.1:5000/number/?param={random_param}')
# print(result.json())



# # POST request
# result = requests.post(url, json ={'jsonParam': random_param}, headers={'content-type': 'application/json'})
# print(result.json())  # Печатает результат POST-запроса

# # # DELETE request
# result = requests.delete(url)
# print(result.json())  # Печатает результат DELETE-запроса

# Раздел 2
# GET 
# response_get = requests.get(f'http://127.0.0.1:5000/number/?param={random_param}')
# data_get = response_get.json()
# number_get = data_get['Результат GET']

# # POST 
# response_post = requests.post(url, json={'jsonParam': random_param}, headers={'content-type': 'application/json'})
# data_post = response_post.json()
# number_post = data_post['Результат POST']
# operation_post = data_post['Операция']

# # DELETE 
# response_delete = requests.delete(url)
# data_delete = response_delete.json()
# number_delete = data_delete['Результат DELETE']
# operation_delete = data_delete['Операция']

# # Операции
# if operation_post == 'Сложение':
#     result = number_get + number_post
# elif operation_post == 'Вычитание':
#     result = number_get - number_post
# elif operation_post == 'Умножение':
#     result = number_get * number_post
# elif operation_post == 'Деление':
#     result = number_get / number_post

# if operation_delete == 'Сложение':
#     result += number_delete
# elif operation_delete == 'Вычитание':
#     result -= number_delete
# elif operation_delete == 'Умножение':
#     result *= number_delete
# elif operation_delete == 'Деление':
#     result /= number_delete

# # Привести результат к целому числу
# result_int = int(result)

# print("Результат:", result_int)