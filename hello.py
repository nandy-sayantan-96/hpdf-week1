from flask import Flask, render_template, make_response, request
import urllib
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World - Sayantan"

@app.route('/authors')
def authors():
    response = urllib.urlopen('https://jsonplaceholder.typicode.com/users')
    authors = json.loads(response.read().decode('utf-8'))
    response = urllib.urlopen('https://jsonplaceholder.typicode.com/posts')
    posts = json.loads(response.read().decode('utf-8'))
    for author in authors:
        post_count = 0
        for post in posts:
            if author['id'] == post['userId']:
                post_count = post_count + 1
        user['post_count'] = post_count
    return render_template('authors.html', authors=users)


@app.route('/setcookie')
def setcookie():
    resp = make_response('Setting Cookie...')
    if 'name' not in request.cookies:
        resp.set_cookie('name', 'Sayantan Nandy')
    if 'age' not in request.cookies:
        resp.set_cookie('age', '21')
    return resp

@app.route("/getcookie")
def getcookie():
	name = request.cookies.get('name')
	age = request.cookies.get('age')
	return 'The cookies are name and age. The name is ' + name + ' and the age is ' + age


@app.route('/robots.txt')
def deny_request():
    return render_template('deny.html')

@app.route('/html')
def render_html():
	return render_template('test.html', name = 'Sayantan')

@app.route('/input', methods=['POST' , 'GET'])
def input():
	if request.method == 'POST' :
		input_text = request.form['input_text']
		return render_template('display.html', input_text = input_text)
	if request.method == 'GET':
		return render_template('input.html')
        
    
