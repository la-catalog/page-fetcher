import asyncio
import unittest
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock, patch

from logger_utility import RichPoint

from page_fetcher import Fetcher
from page_fetcher.abstractions import Marketplace
from page_fetcher.options import get_marketplace_fetcher, options


class TestFetch(IsolatedAsyncioTestCase):
    @patch("asyncio.sleep", AsyncMock())
    async def test_list_fetch(
        self,
    ) -> None:
        urls = ["https://www.google.com/", "https://search.brave.com/"]
        coroutines = []

        for marketplace in options:
            coroutine = self._list_fetch(marketplace, urls)
            coroutines.append(coroutine)

        await asyncio.gather(*coroutines)

    async def _list_fetch(self, marketplace: Marketplace, urls: list[str]):
        fetcher = Fetcher(logger=RichPoint("test"))
        async_gen = await fetcher.fetch(urls=urls, marketplace=marketplace)

        async for text, url in async_gen:
            pass


if __name__ == "__main__":
    unittest.main()
