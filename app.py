import string
import uvicorn
from fastapi import FastAPI
from MatchNote import MatchNote
from HomeAway import HomeAway
import numpy as np
import pickle
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Create the app object

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

Teams = pd.read_csv("TeamsCL.csv")


@app.get('/')
def index():
    return {'message': 'Hello, World'}



@app.post('/predict')
def predict_match(data:MatchNote):
    data = data.dict()
    is_cup=data['is_cup']
    home_team_history_goal=data['home_team_history_goal']
    away_team_history_goal=data['away_team_history_goal']
    home_team_history_opponent_goal=data['home_team_history_opponent_goal']
    away_team_history_opponent_goal=data['away_team_history_opponent_goal']
    home_team_history_rating=data['home_team_history_rating']
    away_team_history_rating=data['away_team_history_rating']
    home_team_history_opponent_rating=data['home_team_history_opponent_rating']
    away_team_history_opponent_rating=data['away_team_history_opponent_rating']


    prediction = classifier.predict_proba([[is_cup,home_team_history_goal,away_team_history_goal,home_team_history_opponent_goal,away_team_history_opponent_goal,home_team_history_rating,away_team_history_rating,home_team_history_opponent_rating,away_team_history_opponent_rating]])
    # if(prediction[0]==0):
    #     prediction="home"
    # else:
    #     prediction="away"
    # return {
    #     'prediction': prediction
    # }
    return {'home':prediction[0,0] , 'draw':prediction[0,1],'away':prediction[0,2]}

@app.post('/predictbyteam')
def predict_match(data:HomeAway):
    data = data.dict()
    home = Teams.loc[Teams['home_team_name'] == data['homeTeamName']]
    away = Teams.loc[Teams['home_team_name'] == data['awayTeamName']]
    
    is_cup=1
    home_team_history_goal=home.iloc[0]['home_team_history_goal']
    away_team_history_goal=away.iloc[0]['home_team_history_goal']
    home_team_history_opponent_goal=home.iloc[0]['home_team_history_opponent_goal']
    away_team_history_opponent_goal=away.iloc[0]['home_team_history_opponent_goal']
    home_team_history_rating=home.iloc[0]['home_team_history_rating']
    away_team_history_rating=away.iloc[0]['home_team_history_rating']
    home_team_history_opponent_rating=home.iloc[0]['home_team_history_opponent_rating']
    away_team_history_opponent_rating=away.iloc[0]['home_team_history_opponent_rating']

    prediction = classifier.predict_proba([[is_cup,home_team_history_goal,away_team_history_goal,home_team_history_opponent_goal,away_team_history_opponent_goal,home_team_history_rating,away_team_history_rating,home_team_history_opponent_rating,away_team_history_opponent_rating]])

    return {'home':prediction[0,0] , 'draw':prediction[0,1],'away':prediction[0,2]}


@app.get('/getteams')
def getTeamsName():
    names= []
    for name in Teams["home_team_name"]:
        names.append(name)
    return names

