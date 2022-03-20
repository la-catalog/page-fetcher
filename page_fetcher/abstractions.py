from typing import Iterator

from page_fetcher.exceptions import NotFoundError, TooManyRequestsError


class Marketplace:
    """
    Base class for the marketplaces classes.
    """

    def fetch(self, urls: list[str]) -> Iterator[str]:
        """Navegate through urls to return the contents which are intresting to us."""

        return iter([])

    def cooldown(self) -> None:
        """
        Called when the marketplace complains that too many request
        were made, so it should give a little cooldown from requesting.
        """

        pass

    def _raise_for_status(self, status) -> None:
        """React appropriately to specifics responses status."""

        if status is 429:
            raise TooManyRequestsError()
        elif status is 404:
            raise NotFoundError()


class FetcherAbstraction:
    """
    Fetcher is responsible for scraping content from pages and dealing
    with unexpected response from the marketplaces.

    It should be focus in collecting the content and not parsing
    or analysing it. Sometimes it's necessary, but you should think before doing it.
    """

    def __init__(self, logger):
        self.logger = logger

    def fetch(self, urls: list[str], marketplace: str) -> Iterator[str]:
        """Pick the expected marketplace fetcher to call the fetch function."""

        return iter([])

    def cooldown(self) -> None:
        """Pick the expected marketplace fetcher to call the cooldown function."""

        pass
