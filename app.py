import logging
from random import randint
from flask import Flask, render_template, request, redirect
from flask_ask import Ask, statement, question, session, request
import urllib2
import json
import emailtext


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
    session.attributes['product'] = "a retirement product"
    return question(render_template('state_question'))


@ask.intent('InsuranceIntent')
def getInsurance():
    session.attributes['product'] = "a insurance product"
    return question(render_template('state_question'))

@ask.intent('bothIntent')
def getBoth():
    session.attributes['product'] = "both insurance and retirement products"
    return question(render_template('state_question'))

@ask.intent('stateIntent', convert={'state':str})
def getState(state):
    session.attributes['state'] = str(state)
    return question(render_template('phoneNumber'))

@ask.intent('phoneIntent', convert={'phoneNumber':int})
def getPhone(phoneNumber):
    if(len(str(phoneNumber)) < 9):
        return question(render_template('invalidPhoneNumber'))
    session.attributes['phone'] = phoneNumber
    state = str(session.attributes['state'])
    product = str(session.attributes['product'])
    name = str(session.attributes['name'])
    email = str(session.attributes['email'])
    txt = "Dear Sales Employee\n"
    txt += "A user named " + name + " made a request from " + state + " to our Alexa app to learn more about " + product + " today. He/She can be reached at this phone numner "
    txt += str(phoneNumber) + " and this email: " + email + ". Please send him/her more information about this product!\n Thanks, Upper Management"
    emailtext.sendEmail(txt)
    return statement(render_template('result', name = name, email = email, product = product, state = state, phone = phoneNumber))

if __name__ == '__main__':
    app.run(debug=True)
