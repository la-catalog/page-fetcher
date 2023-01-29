from collections.abc import AsyncGenerator
from typing import Any, Tuple

from la_catch import Catch
from logger_utility import WritePoint

from page_fetcher.options import get_marketplace_fetcher


class Fetcher:
    """
    Fetcher is responsible for scraping content from pages and dealing
    with unexpected response from the marketplaces.

    It should be focus on collecting content and not parsing
    or analysing it.
    """

    def __init__(self, logger: WritePoint) -> None:
        self._logger = logger.copy().tag("package", "page_fetcher")

    def _on_fetch_error(
        self,
        urls: list[str],
        marketplace: str,
        exception: Exception,
        *args,
        **kwargs,
    ) -> None:
        self._logger.copy().tag("event", "fetcher error").tag(
            "marketplace", marketplace
        ).field("urls", urls).field("exception", str(exception)).print()

        raise

    @Catch(Exception, _on_fetch_error)
    async def fetch(
        self,
        urls: list[str],
        marketplace: str,
        *args: tuple[Any],
        **kwargs: dict[str, Any],
    ) -> AsyncGenerator[Tuple[str | None, str], str | None]:
        """Call the fetch function from the respective marketplace."""

        logger = self._logger.copy().tag("marketplace", marketplace)
        fetcher = get_marketplace_fetcher(marketplace, logger)
        return fetcher.fetch(urls, *args, **kwargs)
