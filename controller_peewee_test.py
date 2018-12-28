from bottle import route, run, get, post, request
import http.client
from util import *
from models import People, PeopleCreateMocks, PeopleProxy
from queries import findPeopleByFirstName, findPeopleByRelative, findPeopleByRelativeAndFirstName, findPeopleAll, findPeopleByid
import pickle
connection = http.client.HTTPConnection("localhost:8080")

@get('/people')
def peewee_test():
    if request.query.firstName:
        if request.query.is_relative:
            return findPeopleByRelativeAndFirstName(bool(request.query.is_relative), request.query.firstName)
        return findPeopleByFirstName(request.query.firstName)
    else:
        return findPeopleAll()

@get('/people/<id>')
def byid(id):
    return findPeopleByid(id)

@get('/people/firstname/<name>')
def byname(name):
    return findPeopleByFirstName(name)


@get('/people/rel/<rel>')
def byrel(rel):
    return findPeopleByRelative(rel)

@post('/people')
def createPeople():
    people = People(firstName=request.json.get('firstName'), is_relative=request.json.get('is_relative'))
    people.save()
    pjson=tojson(model_to_dict(people))
    return pjson

@get('/people_create')
def peewee_test():
    PeopleCreateMocks()
    return ""




@get('/peoplepiclle')
def peoplepiclle():
    f = open("example", "rb")
    peoples = []
    while True:

        try:
            peoples.append(pickle.load(f).__dict__)
        except Exception as e:
            print (e)
            break
    f.close()
    return tojson(peoples)

@post('/peoplepiclle')
def peoplepicllepost():
    f = open("example", "ba")
    people = PeopleProxy(firstName=request.json.get('firstName'), is_relative=request.json.get('is_relative'))
    pickle.dump(people, f)
    f.close()
    return people.__dict__

# @get('/peewee_proxy')
# def peewee_proxy():
#     connection.request("GET", "/peewee")
#     return connection.getresponse()

if __name__ == "__main__":
    # create_mocks()
    # example_selects()
    run(host='localhost', port=8080, debug=True)
