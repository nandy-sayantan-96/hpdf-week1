HPDF - WEEK 1 TASKS

DESCRIPTION

This repository contains the files which were required to complete the tasks for week 1 of HPDF.

TASKS

1. A simple hello-world at http://localhost:8080/ that displays a simple string like "Hello World - Arpit"; replace "Arpit" with your own first name).

2. Add a route, for e.g. http://localhost:8080/authors, which:
	a. fetches a list of authors from a request to https://jsonplaceholder.typicode.com/users
	b. fetches a list of posts from a request to https://jsonplaceholder.typicode.com/posts
	c. Respond with only a list of authors and the count of their posts (a newline for each author).

3. Set a simple cookie (if it has not already been set) at http://localhost:8080/setcookie with the following values: name=<your-first-name> and age=<your-age>.

4. Fetch the set cookie with http://localhost:8080/getcookies and display the stored key-values in it.

5. Deny requests to your http://localhost:8080/robots.txt page. (or you can use the response at http://httpbin.org/deny if needed)

6. Render an HTML page at http://localhost:8080/html or an image at http://localhost:8080/image.

7. A text box at http://localhost:8080/input which sends the data as POST to any endpoint of your choice. This endpoint should log the received the received to stdout.
	
8. Please note that http://localhost:8080/ is just an example, you can run the flask, express web-servers at their default ports on your local machine. 

HOW TO USE

1. Clone the repository. 
2. Create a virtual environment and activate it. 
	virtualenv venv
	source venv/bin/activate
3. Install dependencies
	pip install flask
4. To run the application within venv do the following : 
	$ cd hpdf-week1/
	$ set EXPORT_APP = hello.py
	$ flask run
5. Open a wen browser and go to http://127.0.0.1:5000/ to run this app.


REQUIREMENTS
Python 2.7
Flask

