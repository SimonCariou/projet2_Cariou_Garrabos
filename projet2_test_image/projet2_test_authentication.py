import os
import requests
from passlib.context import CryptContext
import time

time.sleep(10)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#définition de l'adresse de l'API
api_adress = 'my-api-sentiment-analysis'
#port de l'API
api_port = 8000

#requête
r = requests.get(
	url='http://{address}:{port}/permissions'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	}
)

output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="alice"
| password="wonderland"

expected result = 200
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=status_code, test_status=test_status))

#==============================================================================================

#requête
r = requests.get(
	url='http://{address}:{port}/permissions'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic Ym9iOmJ1aWxkZXI="
	}
)

output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="bob"
| password="builder"

expected result = 200
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=status_code, test_status=test_status))

#========================================================================================

#requête
r = requests.get(
	url='http://{address}:{port}/permissions'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic Y2xlbWVudGluZTptYW5kYXJpbmU="
	}
)

output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="clementine"
| password="mandarine"

expected result = 200
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=status_code, test_status=test_status))


#========================================================================================

#requête
r = requests.get(
	url='http://{address}:{port}/permissions'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic dGl0aTp0b3Rv"
	}
)

output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="toto"
| password="titi"

expected result = 401
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 401:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=status_code, test_status=test_status))
