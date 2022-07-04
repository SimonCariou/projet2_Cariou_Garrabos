import os
import requests


#définition de l'adresse de l'API
api_adress = 'my-api-sentiment-analysis'
#port de l'API
api_port = 8000

#requête
r = requests.get(
	url='http://{address}:{port}/performances/log_reg'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	}
)

output = '''
============================
    Performances test
============================

request done at "/performances/log_reg"
| username="alice"
| password="wonderland"

expected result > 0.8
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# recall score répondu par l'API
recall_score = r.json()["recall_score"]

# accuracy score répondu par l'API
accuracy_score = r.json()["accuracy_score"]

# recall score répondu par l'API
f1_score = r.json()["f1_score"]

# accuracy score répondu par l'API
precision_score = r.json()["precision_score"]

# affichage des résultats
if status_code == 200 and recall_score >  0.8 and accuracy_score > 0.8 and f1_score > 0.8 and precision_score > 0.8:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=r.json(), test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=r.json(), test_status=test_status))

#=======================================================================================

#requête
r = requests.get(
	url='http://{address}:{port}/performances/SGD'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	}
)

output = '''
============================
    Performances test
============================

request done at "/performances/SGD"
| username="alice"
| password="wonderland"

expected result > 0.8
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# recall score répondu par l'API
recall_score = r.json()["recall_score"]

# accuracy score répondu par l'API
accuracy_score = r.json()["accuracy_score"]

# recall score répondu par l'API
f1_score = r.json()["f1_score"]

# accuracy score répondu par l'API
precision_score = r.json()["precision_score"]


# affichage des résultats
if status_code == 200 and recall_score >  0.8 and accuracy_score > 0.8 and f1_score > 0.8 and precision_score > 0.8:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=r.json(), test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=r.json(), test_status=test_status))

#=============================================================================================

#requête
r = requests.get(
	url='http://{address}:{port}/performances/decision_tree'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	}
)

output = '''
============================
    Performances test
============================

request done at "/performances/decision_tree"
| username="alice"
| password="wonderland"

expected result > 0.8
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# recall score répondu par l'API
recall_score = r.json()["recall_score"]

# accuracy score répondu par l'API
accuracy_score = r.json()["accuracy_score"]

# recall score répondu par l'API
f1_score = r.json()["f1_score"]

# accuracy score répondu par l'API
precision_score = r.json()["precision_score"]


# affichage des résultats
if status_code == 200 and recall_score >  0.8 and accuracy_score > 0.8 and f1_score > 0.8 and precision_score > 0.8:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=r.json(), test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=r.json(), test_status=test_status))

#=========================================================================================

#requête
r = requests.get(
	url='http://{address}:{port}/performances/MNB'.format(address=api_adress, port=api_port),
	headers= {
		"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="
	}
)

output = '''
============================
    Performances test
============================

request done at "/performances/MNB"
| username="alice"
| password="wonderland"

expected result > 0.8
actual result = {status_code}

==> {test_status}

'''

# statut de la requête
status_code = r.status_code

# recall score répondu par l'API
recall_score = r.json()["recall_score"]

# accuracy score répondu par l'API
accuracy_score = r.json()["accuracy_score"]

# recall score répondu par l'API
f1_score = r.json()["f1_score"]

# accuracy score répondu par l'API
precision_score = r.json()["precision_score"]


# affichage des résultats
if status_code == 200 and recall_score >  0.8 and accuracy_score > 0.8 and f1_score > 0.8 and precision_score > 0.8:
	test_status = 'SUCCES'
else:
	test_status = 'FAILURE'
print(output.format(status_code=r.json(), test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
	with open('/home/test/api_test.log', 'a') as file:
		file.write(output.format(status_code=r.json(), test_status=test_status))


