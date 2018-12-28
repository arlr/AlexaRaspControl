#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Source : https://gist.github.com/keithweaver/3d5dbf38074cee4250c7d9807510c7c3
# Flask explain : https://flask-ask.readthedocs.io/en/latest/requests.html !!!!!!! USEFUL


from flask import Flask, render_template
from flask_ask import Ask, statement, question, request, session, convert_errors
import os, time

#Creation de l'app
app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def start_skill():
    welcome_message = render_template('Bonjour, que voulez vous faire ?')  #Message que vas dire Alexa
    return question(welcome_message)

@ask.intent('BlScanIntent')
def scan_bluetooth():
    devices=os.system("Bl_Scripts/ListBL.py")
    return statement('Les appareils disponibles son :', devices)

@ask.session_ended
def session_ended():
    return "{}", 200




#On Off command

if __name__ == '__main__':
    app.run(debug=True)