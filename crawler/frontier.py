import asyncio
from utils.fingerprint import fingerprint


class URLFrontier:

    def __init__(self):

        self.queue = asyncio.Queue()
        self.seen = set()

    def push(self, url):

        key = fingerprint(url)

        if key not in self.seen:

            self.seen.add(key)

            self.queue.put_nowait(url)

    async def pop(self):

        return await self.queue.get()
