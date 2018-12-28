import asyncio
import aiohttp
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor

data={"service1": []}
futures = []
loop = asyncio.get_event_loop()
executor = ThreadPoolExecutor(max_workers=3)

async def a_url(url):
    print('Starting async {}'.format(url))
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.text()
        #print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

def s_url(url):
    global data
    print('Starting sync {}'.format(url))
    data['service1'].append(urlopen(url).read())
    #print('{}: {} bytes: {}'.format(url, len(data), data))

futures.append(loop.run_in_executor(executor, s_url, 'http://gturnquist-quoters.cfapps.io/api/random'))
futures.append(a_url('http://gturnquist-quoters.cfapps.io/api/random'))
results=loop.run_until_complete(asyncio.wait(futures))
print(data["service1"])
print([i.result() for i in results[0]])