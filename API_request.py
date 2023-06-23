import requests


url = 'https://petstore.swagger.io/v2/user'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
    "id": 987789987,
    "username": "King",
    "firstName": "Louie",
    "lastName": "Monk",
    "email": "monk@ya.ru",
    "password": "test",
    "phone": "test",
    "userStatus": 0
}

data_put = {
    "id": 987789987,
    "username": "King",
    "firstName": "Louie",
    "lastName": "Moon",
    "email": "moon@ya.ru",
    "password": "test",
    "phone": "23783247982374",
    "userStatus": 0
}

# Method POST user
response_post = requests.post(url, headers=headers, json=data)

print('Метод POST выполнен со статусом ', response_post.status_code)
print(response_post.json())

# Method GET user

user = 'King'
url = f'https://petstore.swagger.io/v2/user/{user}'

response_get = requests.get(url, headers=headers, json=data)

print('Метод GET выполнен со статусом ',response_get.status_code)
print(response_get.json())


# Method PUT user

data_put = {
    "id": 987789987,
    "username": "King",
    "firstName": "Louie",
    "lastName": "Moon",
    "email": "moon@ya.ru",
    "password": "test",
    "phone": "23783247982374",
    "userStatus": 0
}

response_put = requests.put(url, headers=headers, json=data_put)
print('Метод PUT выполнен со статусом ',response_put.status_code)
print(response_put.json())


# Method DELETE user

response_del = requests.delete(url, headers=headers)
print('Метод DELETE выполнен со статусом ',response_del.status_code)
print(response_del.json())