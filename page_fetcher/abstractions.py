import asyncio
from collections.abc import AsyncGenerator
from typing import Tuple

from structlog.stdlib import BoundLogger


class Marketplace:
    """
    Base class for the marketplaces classes.
    """

    def __init__(self, marketplace: str, logger: BoundLogger) -> None:
        self._marketplace = marketplace
        self._logger = logger

    async def fetch(
        self, urls: list[str]
    ) -> AsyncGenerator[Tuple[str | None, str], str | None]:
        """
        Navegate through urls to return the contents of each one.
        New urls can be processed on time using coroutines `asend()`.

        Yields
            - Tuple with
                - Text scrapped or None.
                - URL from text.
        Sends
            - URL to scrap or None.
        """

        await asyncio.sleep(1)
        _ = yield ("", "")
