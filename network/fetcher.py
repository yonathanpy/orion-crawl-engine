import aiohttp


async def fetch(url):

    try:

        async with aiohttp.ClientSession() as session:

            async with session.get(url, timeout=10) as response:

                if response.status == 200:
                    return await response.text()

    except Exception:
        return None
