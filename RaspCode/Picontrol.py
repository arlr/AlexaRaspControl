#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Source : https://gist.github.com/keithweaver/3d5dbf38074cee4250c7d9807510c7c3
# Flask explain : https://flask-ask.readthedocs.io/en/latest/requests.html !!!!!!! USEFUL


from flask import Flask, render_template
from flask_ask import Ask, statement, question, request, session, convert_errors
import os, time ,sys, subprocess

#Creation de l'app
app = Flask(__name__)
ask = Ask(app, "/PiControle")

@app.route('/')
def homepage():
    return "Page de la raspberry"

@ask.launch
def start_skill():
    welcome_message = "Bonjour, que voulez vous faire ?"  #Message que vas dire Alexa
    return question(welcome_message)

@ask.intent('BlScanIntent')
def scan_bluetooth():
    #log.info("Request ID: {}".format(request.requestId))


    #Travaillé sur le problème du temp de réponse !!
    #devices = subprocess.run(["python3", "../RaspCode/Bl_Scripts/ListBL.py"],stdout=subprocess.PIPE)
    #listeDevice=devices.stdout.decode('utf-8')
    listeDevice = 2+2
    return statement('Les appareils disponibles sont :', str(listeDevice))

@ask.session_ended
def session_ended():
    return "{}", 200




#On Off command

if __name__ == '__main__':
    app.run(debug=True)