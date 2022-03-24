from typing import Iterator

from page_fetcher.exceptions import StatusError


class Marketplace:
    """
    Base class for the marketplaces classes.
    """

    async def fetch(self, urls: list[str]) -> Iterator[str]:
        """Navegate through urls to return the contents which are intresting to us."""

        return iter([])

    async def cooldown(self) -> None:
        """
        Called when the marketplace complains that too many request
        were made, so it should give a little cooldown from requesting.
        """

        pass

    def _raise_for_status(self, status, extra={}) -> None:
        """Raise error if status is not OK."""

        if status is 200:
            return

        raise StatusError(status, extra)


class FetcherAbstraction:
    """
    Fetcher is responsible for scraping content from pages and dealing
    with unexpected response from the marketplaces.

    It should be focus in collecting the content and not parsing
    or analysing it. Sometimes it's necessary, but you should think before doing it.
    """

    def __init__(self, logger):
        self.logger = logger

    async def fetch(self, urls: list[str], marketplace: str) -> Iterator[str]:
        """Pick the expected marketplace fetcher to call the fetch function."""

        return iter([])

    async def cooldown(self) -> None:
        """Pick the expected marketplace fetcher to call the cooldown function."""

        pass
