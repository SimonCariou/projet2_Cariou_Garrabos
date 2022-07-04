import os
import requests

#définition de l'adresse de l'API
api_adress = 'my-api-sentiment-analysis'
#port de l'API
api_port = 8000

#requête
r = requests.get(
	url='http://{address}:{port}/sentiment/log_reg'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	},
	params= {
		'sentence': 'it is a beautiful day'
	}
)

output = '''
============================
    Sentiment test
============================

request done at "/sentiment/log_reg"
| username="alice"
| password="wonderland"
| sentence='it is a beautiful day'

expected result = 1
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# score répondu par l'API
print(r.json())
score = r.json()["result"]

# affichage des résultats
if status_code == 200 and score == 1:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=score, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=score, test_status=test_status))

#==============================================================================================

#requête
r = requests.get(
	url='http://{address}:{port}/sentiment/log_reg'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	},
	params= {
		'sentence': 'that sucks'
	}
)

output = '''
============================
    Sentiment test
============================

request done at "/sentiment/log_reg"
| username="alice"
| password="wonderland"
| sentence='that sucks'

expected result = 0
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# score répondu par l'API
score = r.json()["result"]

# affichage des résultats
if status_code == 200 and score == 0:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=score, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=score, test_status=test_status))

#==================================================================================================
#requête
r = requests.get(
	url='http://{address}:{port}/sentiment/log_reg'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	},
	params= {
		'sentence': ''
	}
)

output = '''
============================
    Sentiment test
============================

request done at "/sentiment/log_reg"
| username="alice"
| password="wonderland"
| sentence=''

expected result = 400
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 400:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=status_code, test_status=test_status))

#===========================================================================================================

#requête
r = requests.get(
	url='http://{address}:{port}/sentiment/SGD'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	},
	params= {
		'sentence': 'life is beautiful'
	}
)

output = '''
============================
    Sentiment test
============================

request done at "/sentiment/SGD"
| username="alice"
| password="wonderland"
| sentence='life is beautiful'

expected result = 1
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# score répondu par l'API
score = r.json()["result"]

# affichage des résultats
if status_code == 200 and score == 1:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=score, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=score, test_status=test_status))

#==============================================================================================

#requête
r = requests.get(
	url='http://{address}:{port}/sentiment/SGD'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	},
	params= {
		'sentence': 'that sucks'
	}
)

output = '''
============================
    Sentiment test
============================

request done at "/rating/SGD"
| username="alice"
| password="wonderland"
| sentence='that sucks'

expected result = 0
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# score répondu par l'API
score = r.json()["result"]

# affichage des résultats
if status_code == 200 and score == 0:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=score, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=score, test_status=test_status))

#==================================================================================================
#requête
r = requests.get(
	url='http://{address}:{port}/sentiment/SGD'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	},
	params= {
		'sentence': ''
	}
)

output = '''
============================
    Sentiment test
============================

request done at "/sentiment/SGD"
| username="alice"
| password="wonderland"
| sentence=''

expected result = 400
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 400:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=status_code, test_status=test_status))


#===============================================================================================

#requête
r = requests.get(
	url='http://{address}:{port}/sentiment/decision_tree'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	},
	params= {
		'sentence': 'life is beautiful'
	}
)

output = '''
============================
    Sentiment test
============================

request done at "/sentiment/decision_tree"
| username="alice"
| password="wonderland"
| sentence='life is beautiful'

expected result = 1
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# score répondu par l'API
score = r.json()["result"]

# affichage des résultats
if status_code == 200 and score == 1:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=score, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=score, test_status=test_status))

#==============================================================================================

#requête
r = requests.get(
	url='http://{address}:{port}/sentiment/decision_tree'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	},
	params= {
		'sentence': 'that sucks'
	}
)

output = '''
============================
    Sentiment test
============================

request done at "/sentiment/decision_tree"
| username="alice"
| password="wonderland"
| sentence='that sucks'

expected result =0 0
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# score répondu par l'API
score = r.json()["result"]

# affichage des résultats
if status_code == 200 and score == 0:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=score, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=score, test_status=test_status))

#==================================================================================================
#requête
r = requests.get(
	url='http://{address}:{port}/sentiment/decision_tree'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	},
	params= {
		'sentence': ''
	}
)

output = '''
============================
    Sentiment test
============================

request done at "/sentiment/decision_tree"
| username="alice"
| password="wonderland"
| sentence=''

expected result = 400
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 400:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=status_code, test_status=test_status))

#============================================================================================

#requête
r = requests.get(
	url='http://{address}:{port}/sentiment/MNB'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	},
	params= {
		'sentence': 'life is beautiful'
	}
)

output = '''
============================
    Sentiment test
============================

request done at "/sentiment/MNB"
| username="alice"
| password="wonderland"
| sentence='life is beautiful'

expected result = 1
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# score répondu par l'API
score = r.json()["result"]

# affichage des résultats
if status_code == 200 and score == 1:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=score, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=score, test_status=test_status))

#==============================================================================================

#requête
r = requests.get(
	url='http://{address}:{port}/sentiment/MNB'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	},
	params= {
		'sentence': 'that sucks'
	}
)

output = '''
============================
    Sentiment test
============================

request done at "/sentiment/MNB"
| username="alice"
| password="wonderland"
| sentence='that sucks'

expected result = 0
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# score répondu par l'API
score = r.json()["result"]

# affichage des résultats
if status_code == 200 and score == 0:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=score, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=score, test_status=test_status))

#==================================================================================================
#requête
r = requests.get(
	url='http://{address}:{port}/sentiment/MNB'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	},
	params= {
		'sentence': ''
	}
)

output = '''
============================
    Sentiment test
============================

request done at "/sentiment/MNB"
| username="alice"
| password="wonderland"
| sentence=''

expected result = 400
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 400:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=status_code, test_status=test_status))

