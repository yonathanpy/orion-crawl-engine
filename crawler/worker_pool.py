import asyncio
from network.fetcher import fetch
from network.html_parser import extract_links
from pipeline.processor import process_page


class WorkerPool:

    def __init__(self, workers, frontier, repository):

        self.count = workers
        self.frontier = frontier
        self.repository = repository

    async def worker(self):

        while True:

            url = await self.frontier.pop()

            html = await fetch(url)

            if not html:
                continue

            data = process_page(url, html)

            self.repository.save(data)

            links = extract_links(url, html)

            for link in links:
                self.frontier.push(link)

    async def start(self):

        tasks = []

        for _ in range(self.count):

            tasks.append(asyncio.create_task(self.worker()))

        await asyncio.gather(*tasks)
