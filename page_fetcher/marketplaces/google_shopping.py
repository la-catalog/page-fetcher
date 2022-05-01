import asyncio
from typing import Iterator
from aiohttp import ClientSession
from la_headers import generate_headers

from page_fetcher.abstractions import Marketplace


class GoogleShopping(Marketplace):
    async def fetch(self, urls: list[str]) -> Iterator[str]:
        headers = generate_headers("chrome", "99.0", "Linux")

        async with ClientSession(headers=headers) as session:
            for url in urls:
                async with session.get(url) as response:
                    self.logger.info(
                        event="Response received",
                        status=response.status,
                        url=url,
                    )

                    self.raise_for_status(response.status)
                    response.raise_for_status()

                    yield await response.text()

    async def cooldown(self) -> None:
        self._logger.debug(event="Start cooldown")
        await asyncio.sleep(5)
        self._logger.debug(event="End cooldown")
