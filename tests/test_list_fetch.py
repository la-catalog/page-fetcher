import asyncio
import unittest
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock, patch

from structlog.stdlib import get_logger

from page_fetcher.abstractions import Marketplace
from page_fetcher.options import get_marketplace_fetcher, options


class TestFetch(IsolatedAsyncioTestCase):
    @patch("asyncio.sleep", AsyncMock())
    async def test_list_fetch(
        self,
    ) -> None:
        urls = ["https://www.google.com/", "https://search.brave.com/"]
        coroutines = []

        for option in options:
            fetcher = get_marketplace_fetcher(option, get_logger())
            coroutine = self._list_fetch(fetcher, urls)

            coroutines.append(coroutine)

        await asyncio.gather(*coroutines)

    async def _list_fetch(self, fetcher: Marketplace, urls: list[str]):
        async for _ in fetcher.fetch(urls):
            pass


if __name__ == "__main__":
    unittest.main()
