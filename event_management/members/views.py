import pyrebase
from django.shortcuts import render

config = {
  "apiKey": "AIzaSyCSK5bM5B00lQusJUbRXOwiPaWUguWNU58",
  "authDomain": "eventmanagement-3dbc6.firebaseapp.com",
  "databaseURL":"https://eventmanagement-3dbc6-default-rtdb.firebaseio.com",
  "projectId": "eventmanagement-3dbc6",
  "storageBucket": "eventmanagement-3dbc6.appspot.com",
  "messagingSenderId": "590218801338",
  "appId": "1:590218801338:web:0dad569c6cd5d6d9e1d283"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

# Create your views here.
def index(request):
    day = database.child('Day').get().val()
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "temp.html",{"day":day})