import asyncio
from crawler.frontier import URLFrontier
from crawler.worker_pool import WorkerPool
from storage.repository import PageRepository


class OrionCrawler:

    def __init__(self, seed_url, workers=5, limit=100):

        self.seed = seed_url
        self.limit = limit

        self.frontier = URLFrontier()
        self.repository = PageRepository()

        self.pool = WorkerPool(
            workers=workers,
            frontier=self.frontier,
            repository=self.repository
        )

    async def _run(self):

        self.frontier.push(self.seed)

        await self.pool.start()

    def start(self):

        asyncio.run(self._run())
