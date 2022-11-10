import asyncio
import unittest
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock, patch

from logger_utility import WritePoint

from page_fetcher import Fetcher
from page_fetcher.abstractions import Marketplace
from page_fetcher.options import options


class TestFetch(IsolatedAsyncioTestCase):
    @patch("asyncio.sleep", AsyncMock())
    async def test_interactive_fetch(
        self,
    ) -> None:
        urls = ["https://duckduckgo.com/", "https://en.wikipedia.org/"]
        coroutines = []

        for marketplace in options:
            coroutine = self._interactive_fetch(marketplace, urls)
            coroutines.append(coroutine)

        await asyncio.gather(*coroutines)

    async def _interactive_fetch(self, marketplace: Marketplace, urls: list[str]):
        fetcher = Fetcher(logger=WritePoint("test", AsyncMock()))
        coroutine = await fetcher.fetch(urls=urls[:1], marketplace=marketplace)

        text, url = await anext(coroutine)

        for url in urls[1:]:
            text, url = await coroutine.asend(url)


if __name__ == "__main__":
    unittest.main()
