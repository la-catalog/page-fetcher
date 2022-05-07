import asyncio
import unittest
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock, patch

from structlog.stdlib import get_logger

from page_fetcher.options import get_marketplace_fetcher, options


class TestCooldown(IsolatedAsyncioTestCase):
    @patch("asyncio.sleep", AsyncMock())
    async def test_cooldown(
        self,
    ) -> None:
        coroutines = []

        for option in options:
            fetcher = get_marketplace_fetcher(option, get_logger())
            coroutine = fetcher._cooldown()

            coroutines.append(coroutine)

        await asyncio.gather(*coroutines)


if __name__ == "__main__":
    unittest.main()
