# Projet 2 - Review Analysis

## Choix d'architecture

Les différents modèles de Machine learning entraînés dans nôtre Notebook du projet 1 ont été sauvegardés en utilisant la librairie joblib et ont été placés dans un dossier à la racine du dossier de l'API. Nous avons fait de même avec les fichiers de performances car ils nécessitent d'avoir le jeu de test sous la main. Nous avons choisi arbitrairement 4 différentes métriques que nous mettons à disposition des utilisateurs qui utilisent les endpoints performances (Plus de détail dans la partie 2 "Implémentation de l'API").

Les fichiers de performances sauvegardés par joblib sont des fichiers JSON qui ont la forme suivante:
```
{
    "recall_score": AA,
    "accuracy_score": BB,
    "f1_score": CC,
    "precision_score": DD
}
```

Ce qui permet à l'API de les retourner directement dans ce format.

## Implémentation de l'API

### Sentiment d'une phrase, calculé par les différents modèles

GET: + paramètre: `{"sentence": "xxxx"}` qui retourne le sentiment de la phrase donnée en paramètre. Le sentiment peut être:
* 0: Phrase à connotation négative
* 1: Phrase à connotation positive. 

Les différents endpoints permettent à l'utilisateur (authentifié) d'accéder aux ressources suivantes:
```
/sentiment/log_reg
/sentiment/decision_tree
/sentiment/MNB
/sentiment/SGD
```

Chacun de ces endpoints retourne un JSON de la forme:

```
{
    "result": score
}
```

### Performances des différents modèles

GET: Retourne: `accuracy_score`, `f1_score`, `recall_score` & `precision_score` pour le modèle/endpoint sélectionné.
```
/performances/log_reg
/performances/decision_tree
/performances/MNB
/performances/SGD
```

Chacun de ces endpoints retourne un JSON de la forme:
```
{
    "recall_score": AA,
    "accuracy_score": BB,
    "f1_score": CC,
    "precision_score": DD
}
```

## Implémentation des tests

### Test de l’authentification des utilisateurs

L’authentification de chaque utilisateur est testée, un test supplémentaire sur un utilisateur inconnu est également réalisé pour vérifier l’erreur retournée.
Test des différents endpoints:

#### Test des endpoints sentiment

```
/sentiment/log_reg
/sentiment/decision_tree
/sentiment/MNB
/sentiment/SGD
```

Chaque endpoint “sentiment” est testé avec une phrase positive, une phrase négative et une phrase vide.

#### Test des endpoints performances

```
/performances/log_reg
/performances/decision_tree
/performances/MNB
/performances/SGD
```
Chaque endpoint “performance” est testé. Une vérification est réalisée sur le JSON reçu, chaque paramètre doit être supérieur à 0.8 pour valider le fonctionnement.


## Containerization de l'API et des Tests

Les images de l’API et des tests sont insérées dans des containers lancés à l’aide de Docker Compose (`docker-compose.yml`):
- Lancement de 2 containers:
    - **API**:
        - *image API*: ml-api-sentiment-analysis
        - *container API*: my_api_sentiment_analysis
    - **Tests**:
        - *image test*: ml-api-sentiments-analysis-tests
        - *container test*: my_api_sentiments_analysis_tests

le container de test n’est lancé qu’une fois que celui de l’API est opérationnel.
création du volume `my_volume_for_project2`: sauvegarde des résultats des tests.
création du network `my_network_for_project2` et exposition du port `8000` pour l’API.

## Déploiement avec Kubernetes

Nous avons fait le choix d'héberger notre image d'API dans un répertoire privé dans le dockerhub afin d'en cacher sa visibilité au grand public. Cette décision nous a amené à créer un secret permettant aux fichiers de configuration Kubernetes de s'authentifier pour la télécharger.
Ce secret (`imagePullSecrets`) est en fait un json contenant les informations de login rentrées en se loggant sur le docker hub avec le terminal (`docker login`) que nous avons encodé en base64.

Avant toute chose, pour lancer le processus de déploiement de l'API sur les 3 pods comme demandé, il va falloir créer le déploiement, le secret, le service et l'ingress, à l'aide de ces commandes:

```
kubectl create -f sentiment-analysis-api-deployment.yml
kubectl create -f registry-pull-secret.yml
kubectl create -f sentiment-analysis-api-ingress.yml
kubectl create -f sentiment-analysis-api-service.yml 
```

## Auteurs

Matthieu Garrabos & Simon Cariou