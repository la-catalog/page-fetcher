import asyncio
import unittest
from unittest import IsolatedAsyncioTestCase
from structlog import get_logger
from unittest.mock import AsyncMock, patch

from page_fetcher import Fetcher
from page_fetcher.options import options, get_marketplace_fetcher


class TestCooldown(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self._logger = get_logger()

    @patch("asyncio.sleep", AsyncMock())
    async def test_cooldown(
        self,
    ) -> None:
        courotines = []

        for option in options:
            fetcher = get_marketplace_fetcher(option, self._logger)
            courotines.append(fetcher._cooldown())

        await asyncio.gather(*courotines)


if __name__ == "__main__":
    unittest.main()
