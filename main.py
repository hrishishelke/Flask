from flask import Flask,render_template,request,redirect

import os
app=Flask(__name__)

@app.route('/')
def about():
    return render_template('login.html')

@app.route('/register')
def login():
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add_user',methods=['post'])
def add_user():

     return "WELCOME REGISTRATION SUCCESFULLY !"

@app.route('/register',methods=['post'])
def register():

     return "Registration Succesfully !"


@app.route('/logout')
def logout():
     session.pop('user_id')
     return redirect('/')

if __name__=="__main__":
     app.run(debug=True)