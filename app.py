import logging
from random import randint
from flask import Flask, render_template, request, redirect
from flask_ask import Ask, statement, question, session, request
import urllib2
import json


app = Flask(__name__)

log = logging.getLogger()

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def welcome():
    return question(render_template('welcome'))

@ask.intent('LoginIntent')
def displayCard():
    return question(render_template('login_please')).link_account_card()

@ask.intent('LoggedInIntent')
def getCredentials():
    key = str(session['user']['accessToken'])
    baseUrl = "https://api.amazon.com/user/profile?access_token="
    baseUrl += key
    print baseUrl
    webUrl = urllib2.urlopen(baseUrl)
    if webUrl.getcode() == 200:
        data = webUrl.read()
        result = json.loads(data)
        session.attributes['name'] = result['name']
        session.attributes['email'] = result['email']
    return question(render_template('logged_in'))

@ask.intent('RetirementIntent')
def getRetirement():
    session.attributes['product'] = "retirement"
    return question(render_template('state_question'))


@ask.intent('InsuranceIntent')
def getInsurance():
    session.attributes['product'] = "insurance"
    return question(render_template('state_question'))

@ask.intent('bothIntent')
def getBoth():
    session.attributes['product'] = "both"
    return question(render_template('state_question'))

@ask.intent('stateIntent', convert={'state':str})
def getState(state):
    session.attributes['state'] = str(state)
    return question(render_template('phoneNumber'))

@ask.intent('phoneIntent', convert={'phoneNumber':int})
def getPhone(phoneNumber):
    session.attributes['phone'] = phoneNumber
    state = str(session.attributes['state'])
    product = str(session.attributes['product'])
    name = str(session.attributes['name'])
    email = str(session.attributes['email'])

    return question(render_template('result', name = name, email = email, product = product, state = state, phone = phoneNumber))

if __name__ == '__main__':
    app.run(debug=True)
