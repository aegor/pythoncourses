import json, pickle
from bottle import route, run, get, post, request
from controller_peewee_test import *

@get('/hello')
def hello():
    p = {firstName: "hello", lastName: "world"}
    return json.dumps(p, ensure_ascii=False)

@post('/hello')
def hellopost():
    people = People(request.json.get('firstName'),request.json.get('lastName'))

    return {"firstName": request.json.get('firstName'), "lastName": request.json.get('lastName')}

if __name__ == "__main__":
    # create_mocks()
    # example_selects()
    run(host='localhost', port=8080, debug=True)
