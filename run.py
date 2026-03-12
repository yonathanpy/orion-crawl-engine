from crawler.engine import OrionCrawler
import click


@click.command()
@click.argument("seed")
@click.option("--workers", default=5)
@click.option("--limit", default=100)
def start(seed, workers, limit):

    crawler = OrionCrawler(seed_url=seed, workers=workers, limit=limit)

    crawler.start()


if __name__ == "__main__":
    start()
