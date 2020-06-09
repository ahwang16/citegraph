# flask-test.py
from flask import Flask, render_template, request, redirect, Response
import json, random, sys

app = Flask(__name__)

@app.route('/output')
def output():
	return "Hello World!"


@app.route('/brandon')
def brandon():
	return "Hi Brandon!!!!!!!!!!!"


@app.route('/name')
def name():
	return render_template("index.html", name="Joe")


@app.route('/')
def default():
	number = random.randint(0, 10)
	return render_template('index.html', name=number)



if __name__ == "__main__":
	app.run()