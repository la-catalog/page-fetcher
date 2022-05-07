import asyncio
from collections.abc import AsyncGenerator

from structlog.stdlib import BoundLogger

from page_fetcher.exceptions import PageNotFoundError


class Marketplace:
    """
    Base class for the marketplaces classes.
    """

    def __init__(self, logger: BoundLogger) -> None:
        self._logger = logger

    async def fetch(self, urls: list[str]) -> AsyncGenerator[str, str | None]:
        """
        Navegate through urls to return the contents of each one.
        New urls can be processed on time using coroutines `send()`.
        """

        _ = yield await asyncio.sleep(0)

    async def _raise_for_status(self, status: int) -> None:
        """Deal with some expected code status."""

        if status is 404:
            raise PageNotFoundError()
        elif status is 429:
            await self._cooldown()

    async def _cooldown(self) -> None:
        """
        Called when the marketplace complains that too many request
        were made, so it should give a little cooldown from requesting.
        """

        pass
