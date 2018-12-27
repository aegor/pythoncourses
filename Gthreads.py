import gevent.monkey, json, pickle
from bottle import route, run, get, post, request
from urllib.request import urlopen

gdata = ""

gevent.monkey.patch_all()
urls = ['https://jsonplaceholder.typicode.com/users']

def print_head(url):
    global gdata
    print('Starting {}'.format(url))
    gdata = urlopen(url).read()
    #print("gdataj->" + str(gdata))

jobs = [gevent.spawn(print_head, _url) for _url in urls]
gevent.wait(jobs)

@get('/qqq')
def qqq():
    obj = json.loads(gdata.decode("utf-8"))
    return obj[0]

run(host='localhost', port=8080, debug=True)
