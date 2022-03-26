import asyncio
from typing import Iterator
from aiohttp import ClientSession

from page_fetcher.abstractions import Marketplace


class GoogleShopping(Marketplace):
    def __init__(self):
        pass

    async def fetch(self, urls: list[str]) -> Iterator[str]:
        async with ClientSession() as session:
            async with session.get(urls[0]) as response:
                self._raise_for_status(response.status)

    async def cooldown(self) -> None:
        print("Google Shopping: cooldown start")
        await asyncio.sleep(5)
        print("Google Shopping: cooldown end")