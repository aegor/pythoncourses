import asyncio
import aiohttp
import gevent.monkey

urls = ['http://gturnquist-quoters.cfapps.io/api/random', 'http://gturnquist-quoters.cfapps.io/api/random', 'http://gturnquist-quoters.cfapps.io/api/random']

async def call_url(url):
    print('Starting {}'.format(url))
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.text()
        #print('{}: {} bytes: {}'.format(url, len(data), data))
    return data
if __name__ == "__main__":
    print(call_url('http://www.yandex.ru'))
    futures = [call_url(url) for url in urls]
    loop = asyncio.get_event_loop()
    results=loop.run_until_complete(asyncio.wait(futures))
    print(type(results[0]))
    print([i.result() for i in results[0]])

# Greenthreads  альтернатива
if __name__ == "__main__":

    from urllib.request import urlopen
    gevent.monkey.patch_all()
    data={"service1": []}
    def print_head(url):
        global data
        print('Starting {}'.format(url))
        data['service1'].append(urlopen(url).read())
        #print('{}: {} bytes: {}'.format(url, len(data), data))

    jobs = [gevent.spawn(print_head, _url) for _url in urls]
    #print(jobs[0])
    gevent.wait(jobs)
    print(data["service1"])
