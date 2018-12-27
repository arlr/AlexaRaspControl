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
    welcome_message = render_template('welcome')
return question(welcome_message)

@ask.intent('AMAZON.HelpIntent')
def help():
return start_skill()

@ask.intent('AMAZON.FallbackIntent')
def fallback():
    fallback_message = render_template('fallback_message')
    return statement(fallback_message)

@ask.session_ended
def session_ended():
return "{}", 200

@ask.intent('PowerIntent')
def power(onOffCommand):
    text = render_template('power_on') if onOffCommand == "on" else render_template('power_off')
return statement(text).simple_card('Status', text)


#On Off command

if __name__ == '__main__':
    app.run(debug=True)