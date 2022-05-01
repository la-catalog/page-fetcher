import asyncio
from typing import AsyncGenerator
from aiohttp import ClientSession
from la_headers import generate_random_headers

from page_fetcher.abstractions import Marketplace


class Rihappy(Marketplace):
    async def fetch(self, urls: list[str]) -> AsyncGenerator[str, None]:
        headers = generate_random_headers(os=["linux"], browser=["chrome"])

        async with ClientSession(headers=headers) as session:
            for url in urls:
                async with session.get(url) as response:
                    self._logger.info(
                        event="Response received",
                        status=response.status,
                        url=url,
                    )

                    await self._raise_for_status(response.status)
                    response.raise_for_status()

                    yield await response.text()

    async def _cooldown(self) -> None:
        self._logger.debug(event=f"Start cooldown")
        await asyncio.sleep(1)
