# flask-test.py
from flask import Flask, jsonify, render_template, request, redirect, Response
import json, random, sys

app = Flask(__name__)

authors = {
	"alyssa": {"id": 0, "cites": ["spongebob", "patrick"], "is_cited_by":[]},
	"spongebob": {"id": 1, "cites": ["patrick"], "is_cited_by": ["alyssa"]}
}

@app.route('/')
def home():
	number = random.randint(0, 10)
	return "Hello world! Here is a magic number: " + str(number)
	# return render_template('index.html', number=number, phrase="Hello world! Here is a magic number: ")


@app.route('/authors', methods=['GET'])
def get_authors():
	return jsonify(authors)


@app.route('/authors', methods=['POST'])
def add_author():
	authors.append(request.get_json())
	return "", 204


@app.route('/authors/<string:query>', methods=['GET'])
def get_author(query):
	if query in authors:
		return jsonify(authors[query])

	return "Author not found", 404


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)