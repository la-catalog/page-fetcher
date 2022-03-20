import os
import asyncio
from page_fetcher.abstractions import Marketplace


class GoogleShopping(Marketplace):
    def __init__(self):
        pass

    async def fetch(self, urls: list[str]) -> list[str]:
        return []

    async def cooldown(self) -> None:
        print("Google Shopping: cooldown start")
        await asyncio.sleep(5)
        print("Google Shopping: cooldown end")