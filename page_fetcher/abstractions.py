from typing import Iterator
from structlog.stdlib import BoundLogger

from page_fetcher.exceptions import PageNotFoundError


class Marketplace:
    """
    Base class for the marketplaces classes.
    """

    def __init__(self, logger: BoundLogger):
        self._logger = logger

    async def fetch(self, urls: list[str]) -> Iterator[str]:
        """Navegate through urls to return the contents which are intresting to us."""

        return iter([])

    async def cooldown(self) -> None:
        """
        Called when the marketplace complains that too many request
        were made, so it should give a little cooldown from requesting.
        """

        pass

    async def raise_for_status(self, status: int) -> None:
        """Deal with some expected code status."""

        if status is 404:
            raise PageNotFoundError()
        elif status is 429:
            await self.cooldown()


class FetcherAbstraction:
    """
    Fetcher is responsible for scraping content from pages and dealing
    with unexpected response from the marketplaces.

    It should be focus in collecting the content and not parsing
    or analysing it. Sometimes it's necessary, but you should think before doing it.
    """

    def __init__(self, logger: BoundLogger):
        self._logger = logger.bind(lib="page_fetcher")

    async def fetch(self, urls: list[str], marketplace: str) -> Iterator[str]:
        """Pick the expected marketplace fetcher to call the fetch function."""

        return iter([])
