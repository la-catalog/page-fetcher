import asyncio
from typing import Iterator
from la_headers import generate_headers

from page_fetcher.abstractions import Marketplace

class Rihappy(Marketplace):
    async def fetch(self, urls: list[str]) -> Iterator[str]:
        return super().fetch(urls)
    
    async def cooldown(self) -> None:
        print("Rihappy: cooldown start")
        await asyncio.sleep(1)
        print("Rihappy: cooldown end")
        