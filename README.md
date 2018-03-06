# Test-Server-For-SFE

**Run by command:**

`$ pip install Flask
$ FLASK_APP=app.py flask run`

**Example:**

`$ FLASK_APP=app.py flask run`

` * Serving Flask app "app"`

 `* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
`

It would show the localhost url for the project. 
If you want to retrieve a student whose NUID is 1, try to send a GET request to http://127.0.0.1:5000/students/1 

**Wiki:**

All APIs' use cases are based on Google Doc:
https://docs.google.com/document/d/1js9rwdIXKSnJgGvB97btZ69GI2cgITWATli5YnodoUU/edit?usp=sharing

I didn't use database for now, so all the test data are stored in lists.
Due to the limitation of List, the prime key (nuid and id) maybe not correspond with the unique instance.
It may bring some disorders in delete and update operations, but will not influence the functionality.

All APIs has passed tests by using Postman.
