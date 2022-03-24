import asyncio
import unittest
from unittest import IsolatedAsyncioTestCase
from unittest.mock import MagicMock, AsyncMock, patch

from page_fetcher import Fetcher
from page_fetcher.options import options


class TestCooldown(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.fetcher = Fetcher(MagicMock())

        return super().setUp()

    @patch("asyncio.sleep", AsyncMock())
    async def test_cooldown(
        self,
    ) -> None:
        args = [self.fetcher.cooldown(m) for m in options]

        await asyncio.gather(*args)


if __name__ == "__main__":
    unittest.main()
