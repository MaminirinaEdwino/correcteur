from fastapi import FastAPI 
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json
import re
#Création du nouvelle instance FastAPI
app = FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials= True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# Définir un objet pour réaliser des requête
class request_body(BaseModel):
    mot_a_corriger: str

@app.get('/')
def index():
    return 'lenina'
# Création d'un terminaison
@app.post("/suggestions/")
def predict(data: request_body):
    with open('index.json','r') as fichier:
        donnees=json.load(fichier)
    liste1=[]
    liste2=[]
    liste3=[]
    for element in donnees:
        if (len(data.mot_a_corriger))+1==len(element) or (len(data.mot_a_corriger))==len(element) or (len(data.mot_a_corriger))-1==len(element):
            liste1.append(element)
    for element in liste1:
        if data.mot_a_corriger in element:
            liste2.append(element)
    for element in liste2:
        if re.match(data.mot_a_corriger,element) or re.fullmatch(data.mot_a_corriger,element):
                liste3.append(element)
    return liste3

    # Return la valeur du prédiction
    #return {'variety_of_iris': variety_predict}