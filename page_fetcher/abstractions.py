import asyncio
from collections.abc import AsyncGenerator
from typing import Tuple

from logger_utility import WritePoint
from page_models import URL


class Marketplace:
    """
    Base class for the marketplaces classes.
    """

    def __init__(self, marketplace: str, logger: WritePoint) -> None:
        self._marketplace = marketplace
        self._logger = logger.copy().tag("marketplace", marketplace)

    async def fetch(
        self, urls: list[str]
    ) -> AsyncGenerator[Tuple[str | None, URL], URL | None]:
        """
        Navegate through urls to return the contents of each one.
        New urls can be processed on time using coroutines `asend()`.

        Yields
            - Tuple with
                - Text scrapped or None.
                - URL from text.
        Sends
            - URL to scrap or None to stop.
        """

        await asyncio.sleep(1)
        _ = yield ("", "")
