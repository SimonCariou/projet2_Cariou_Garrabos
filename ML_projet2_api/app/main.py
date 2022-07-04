from fastapi import FastAPI, HTTPException, Request, status, Depends
from fastapi.responses import JSONResponse

from app.auth.auth_rules import get_auth_status
import joblib
import os

from app.utils.text_preprocessing import finalize_preprocess
from app.utils.constants import *

#from pydantic import BaseModel
#from typing import Optional, List

responses = {
    200: {"detail": "OK"},
    401: {"detail": "Unauthorized"},
    404: {"detail": "Item not found"},
    302: {"detail": "The item was moved"},
    403: {"detail": "Not enough privileges"}
}

description = """
# Description

## Presentation

This API is the second part of the Data Engineer machine learning project.
The first project being the training of several machine learning algorithms on train sets. 
We chose to train a sentiments algorithm on reviews from dating apps users on app stores.

## Goal

The goal is to write an API that:
- allows an authenticated user to send sentences and get the sentiment as a response: 0 if negative and 1 if positive. The sentiment can be calculated by different models, all accessible via their own endpoints:\
  (decision tree, logistic regression, SGD CLassifier & Multinomial NB), test it, contenerize it with docker and deploy it using a Kubernetes Ingress.
- allows an authenticated user to access the performances of the different models in order to chose the right one. The performances that the API will return are\
  the recall_score, the accuracy_score, the f1_score and the precision_score. 

## How to use it 

Available routes:
GET: + parameter: `{"sentence": "xxxx"}` and returns the sentiments of the given sentence according to the chosen model.
```
/sentiment/log_reg
/sentiment/decision_tree
/sentiment/MNB
/sentiment/SGD
```

GET: Returns the accuracy_score, f1_score, recall_score & precision_score for the chosen model
```
/performances/log_reg
/performances/decision_tree
/performances/MNB
/performances/SGD
```

## Authors:

Matthieu Garrabos & Simon Cariou  
"""


api = FastAPI(
    title='ML API - Sentiment Analysis',
    description=description,
    version="1.0.0"
)

# Load the models
log_reg_model = joblib.load(os.path.join(MODELS_DIRECTORY, LOG_REG_FILENAME))
dec_tree_model = joblib.load(os.path.join(MODELS_DIRECTORY, DECISION_TREE_FILENAME))
multi_nb_model = joblib.load(os.path.join( MODELS_DIRECTORY, MULTINOMIAL_NAIVE_BAYES_FILENAME))
sgdc_model = joblib.load(os.path.join(MODELS_DIRECTORY, SGDC_FILENAME))

# Load the different models performances: metrics calculated on the test dataset
log_reg_performances = joblib.load(os.path.join(PERFORMANCES_DIRECTORY, LOG_REG_PERF_FILENAME))
dec_tree_performances = joblib.load(os.path.join(PERFORMANCES_DIRECTORY, DECISION_TREE_PERF_FILENAME))
multi_nb_performances = joblib.load(os.path.join( PERFORMANCES_DIRECTORY, MULTINOMIAL_NAIVE_BAYES_PERF_FILENAME))
sgdc_performances = joblib.load(os.path.join(PERFORMANCES_DIRECTORY, SGDC_PERF_FILENAME))

# Load the vectorizer
tfidf_vectorizer = joblib.load(os.path.join(MODELS_DIRECTORY, TFIDF_VECTORIZER_FILEMANE))

def predict_sentence_sentiment(model, sentence):
    """ This function calculates the sentiment of a given sentence based on the specified model. The sentiment is either 0 or 1 depending on if the sentence is estimated, respectively, negative or positive.
    Input: Machine learning trained model (logistic regression, multinomialNB...)and the sentence (string) which we want to calculate the sentiment.
    Output: The sentiment calculated by the provided model + the sentence it used.
    """
    if sentence == "":
        raise HTTPException(status_code=400, detail='Error, the \'sentence\' parameter should not be empty.')

    preprocessed_sentence = finalize_preprocess(sentence)
    transformed_sentence = tfidf_vectorizer.transform([preprocessed_sentence])
    return {
        "result": model.predict(transformed_sentence)[0].tolist()
    }


""" API IMPLEMENTATION
"""

@api.get("/", responses=responses, name="Check if the API is running")
async def get_root():
    return {"message": "The API is running"}

@api.get("/permissions", responses=responses, name="Check if a user is allowed to access the api")
async def get_permissions(username: bool = Depends(get_auth_status)):
    return {"detail": f"{username} is authorized."}

#GET the sentiment of a given sentence via 5 different ML models.
@api.get("/sentiment/log_reg", responses=responses, name="Get the sentiment (Positive: 1 or Negative: 0) of a sentence calculated by the logistic regression model.")
async def get_logreg_ratin(sentence: str, isAuthenticated: bool = Depends(get_auth_status)):
    return predict_sentence_sentiment(log_reg_model, sentence)

@api.get("/sentiment/decision_tree", responses=responses, name="Get the sentiment (Positive: 1 or Negative: 0) of a sentence calculated by the decision tree classifier model.")
async def get_dec_tree_sentiment(sentence: str, isAuthenticated: bool = Depends(get_auth_status)):
    return predict_sentence_sentiment(dec_tree_model, sentence)

@api.get("/sentiment/MNB", responses=responses, name="Get the sentiment (Positive: 1 or Negative: 0) of a sentence calculated by the Multinomial Naive Bayes model.")
async def get_multinomial_nb_sentiment(sentence: str, isAuthenticated: bool = Depends(get_auth_status)):
    return predict_sentence_sentiment(multi_nb_model, sentence)

@api.get("/sentiment/SGD", responses=responses, name="Get the sentiment (Positive: 1 or Negative: 0) of a sentence calculated by the Stochastic Gradient model.")
async def get_sgdc_sentiment(sentence: str, isAuthenticated: bool = Depends(get_auth_status)):
    return predict_sentence_sentiment(sgdc_model, sentence)


#GET the performances of the different models
@api.get("/performances/log_reg", responses=responses, name="Get the performances of the logistic regression model on the trained dataset.")
async def get_logreg_performances(isAuthenticated: bool = Depends(get_auth_status)):
    return log_reg_performances

@api.get("/performances/decision_tree", responses=responses, name="Get the performances of the decision tree classifier model on the trained dataset.")
async def get_dec_tree_performances(isAuthenticated: bool = Depends(get_auth_status)):
    return dec_tree_performances

@api.get("/performances/MNB", responses=responses, name="Get the performances of the Multinomial Naive Bayes model on the trained dataset.")
async def get_multinomial_nb_performances(isAuthenticated: bool = Depends(get_auth_status)):
    return multi_nb_performances

@api.get("/performances/SGD", responses=responses, name="Get the performances of the Stochastic Gradient classifier model on the trained dataset.")
async def get_sgdc_performances(isAuthenticated: bool = Depends(get_auth_status)):
    return sgdc_performances