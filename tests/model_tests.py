import json
import requests
import os

URI = 'http://127.0.0.1:8000/api'
LOGIN = f'{URI}/auth/login/'
REFRESH = f'{URI}/auth/refresh/'
ADMIN = f'{URI}/admin'
HEADER = {'Content-Type': 'application/json'}

print('----------LOGIN----------')
data = {'email': 'admin@abc.com', 'password': 'admin'}
req = requests.post(LOGIN, data=json.dumps(data), headers=HEADER)
print(req.status_code)
print(req.text)
reqJSON = req.json()
API_TOKEN = reqJSON['token']

print('----------GET USER DETAILS----------')
ARTIST = 'http://127.0.0.1:8000/api/artist/details/2'
HEADER_WITH_TOKEN = {'Authorization': f'JWT {API_TOKEN}'}
req = requests.get(ARTIST, headers=HEADER_WITH_TOKEN)
print(req.status_code)
print(req.text)

print('----------GET LIST OF USERS (ADMIN)----------')
ADMIN_ARTIST = f'{ADMIN}/artist/'
HEADER_WITH_TOKEN = {
    'Content-Type': 'application/json',
    'Authorization': f'JWT {API_TOKEN}'
}
req = requests.get(ADMIN_ARTIST, headers=HEADER_WITH_TOKEN)
print(req.status_code)

getJSON = req.json()
print(getJSON)


# print('----------GET LIST USER DETAILS----------')
# ARTIST = f'{URI}/artist/details/1'
# HEADER_WITH_TOKEN = {
#     'Content-Type': 'application/json',
#     'Authorization': f'JWT {API_TOKEN}'
# }
# req = requests.get(ARTIST, headers=HEADER_WITH_TOKEN)
# print(req.status_code)
# print(req.text)
