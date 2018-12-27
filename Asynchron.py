import asyncio
import aiohttp

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']
urls1 = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

async def call_url(url):
    print('Starting {}'.format(url))
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.text()
        print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

print(call_url('http://www.yandex.ru'))
# futures = [call_url(url) for url in urls]
# futures1 = [call_url(url) for url in urls1]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(futures))
# loop.run_until_complete(asyncio.wait(futures1))

# Greenthreads  альтернатива
import gevent.monkey
from urllib.request import urlopen
gevent.monkey.patch_all()
urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

def print_head(url):
    print('Starting {}'.format(url))
    data = urlopen(url).read()
    print('{}: {} bytes: {}'.format(url, len(data), data))

jobs = [gevent.spawn(print_head, _url) for _url in urls]
print(jobs[0])
#gevent.wait(jobs)