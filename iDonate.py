#WebApp coding
import os
from flask import Flask, url_for, render_template, request
from flask import session

app = Flask(__name__)
#http://127.0.0.1:5000/

@app.route('/') #home page
def render_main():
    return render_template('home.html')

'''
@app.route('/questionaire')
def render_questionaire():
    return render_template('questionaire.html')

@app.route('/eligibility') #displays if eligible
def render_eligibility():
    return render_template('eligibility.html')

@app.route('/procedures') #if eligible
def render_procedure():
    return render_template('procedures.html')

@app.route('/appointment')
def render_appointment():
    return render_template('appointment.html')

@app.route('/overview')
def render_overview():
    return render_template('overview.html')

@app.route('/notifications')
def render_notifications():
    return render_template('notifications.html')

@app.route('/hydrationtest')
def render_hydrationtest():
    return render_template('hydrationtest.html')'''

if __name__== "__main__":
    app.run()

