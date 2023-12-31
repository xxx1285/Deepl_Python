import asyncio
import sys

# https://proxy6.net/checker

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from proxybroker import Broker

async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None: break
        print(f"{proxy.host}:{proxy.port}")

proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(
    broker.find(types=['HTTP', 'HTTPS'], countries=['UA'], limit=13),
    show(proxies))

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)