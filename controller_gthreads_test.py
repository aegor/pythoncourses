import gevent.monkey, json, pickle
from bottle import route, run, get, post, request
from urllib.request import urlopen

gdata = {}

gevent.monkey.patch_all()
urls = ['https://jsonplaceholder.typicode.com/users']

def print_head(url):
    global gdata
    print('Starting {}'.format(url))
    gdata['users'] = urlopen(url).read()
    #print("gdataj->" + str(gdata))

@get('/gthreads')
def gthreads():
    jobs = [gevent.spawn(print_head, _url) for _url in urls]
    gevent.wait(jobs)
    obj = json.loads(gdata.get('users').decode("utf-8"))
    return obj[0]

run(host='localhost', port=8080, debug=True)
