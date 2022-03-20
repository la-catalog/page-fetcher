import asyncio
import unittest
from unittest import TestCase
from unittest.mock import MagicMock, AsyncMock, patch

from page_fetcher import Fetcher
from page_fetcher.options import options


class TestCooldown(TestCase):
    def setUp(self) -> None:
        self.fetcher = Fetcher(MagicMock())
        return super().setUp()

    def test_cooldown(
        self,
    ) -> None:
        async def test():
            await asyncio.gather(
                self.fetcher.cooldown("google shopping"),
                self.fetcher.cooldown("rihappy"),
            )

        asyncio.run(test())


if __name__ == "__main__":
    unittest.main()
