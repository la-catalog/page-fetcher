import asyncio
import unittest
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock, patch
from structlog.stdlib import get_logger
from page_fetcher.abstractions import Marketplace

from page_fetcher.options import options, get_marketplace_fetcher


class TestFetch(IsolatedAsyncioTestCase):
    @patch("asyncio.sleep", AsyncMock())
    async def test_interactive_fetch(
        self,
    ) -> None:
        urls = ["https://duckduckgo.com/", "https://en.wikipedia.org/"]
        coroutines = []

        for option in options:
            fetcher = get_marketplace_fetcher(option, get_logger())
            coroutine = self._interactive_fetch(fetcher, urls)

            coroutines.append(coroutine)

        await asyncio.gather(*coroutines)

    async def _interactive_fetch(self, fetcher: Marketplace, urls: list[str]):
        coroutine = fetcher.fetch(urls[:1])
        await anext(coroutine)

        for url in urls[1:]:
            _ = await coroutine.asend(url)


if __name__ == "__main__":
    unittest.main()
