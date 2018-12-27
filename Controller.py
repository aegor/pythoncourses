import json, pickle
from bottle import route, run, get, post, request
from PeeWeeTest import *


@get('/hello')
def hello():
    p = People("Иван", "Иванов")
    return json.dumps(p.__dict__, ensure_ascii=False)

@post('/hello')
def hellopost():
    people = People(request.json.get('firstName'),request.json.get('lastName'))
    print(people)
    return people.__dict__

run(host='localhost', port=8080, debug=True)
