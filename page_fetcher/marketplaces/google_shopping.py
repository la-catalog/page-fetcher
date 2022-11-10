import asyncio
from collections.abc import AsyncGenerator
from typing import Tuple

from aiohttp import ClientSession
from la_headers import generate_random_headers
from la_stopwatch import Stopwatch
from page_models import URL

from page_fetcher.abstractions import Marketplace


class GoogleShopping(Marketplace):
    async def fetch(
        self, urls: list[URL]
    ) -> AsyncGenerator[Tuple[str | None, URL], URL | None]:
        stopwatch = Stopwatch()
        headers = generate_random_headers(os=["linux"], browser=["chrome"])

        async with ClientSession(headers=headers) as session:
            for url in urls:
                while url:
                    async with session.get(url) as response:
                        (
                            await self._logger.copy()
                            .tag("event", "response received")
                            .field("url", url)
                            .field("status", response.status)
                            .field("duration", str(stopwatch))
                            .print()
                            .write("scraper")
                        )

                        if response.status == 429:
                            (
                                await self._logger.copy()
                                .tag("event", "start cooldown")
                                .write("scraper")
                            )

                            await asyncio.sleep(5)

                        response.raise_for_status()

                        text = await response.text()
                        url = yield (text, url)

                        stopwatch.reset()
