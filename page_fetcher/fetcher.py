from typing import AsyncGenerator
from la_catch import catch
from structlog.stdlib import BoundLogger

from page_fetcher.options import get_marketplace_fetcher
from page_fetcher.exceptions import PageNotFoundError


class Fetcher:
    """
    Fetcher is responsible for scraping content from pages and dealing
    with unexpected response from the marketplaces.

    It should be focus in collecting the content and not parsing
    or analysing it.
    """

    def __init__(self, logger: BoundLogger):
        self._logger = logger.bind(lib="page_fetcher")

    def _log_error(self, urls: list[str], marketplace: str, exception: Exception) -> None:
        self._logger.exception(
            event="Fetcher error",
            urls=urls,
            marketplace=marketplace,
        )
    
    @catch(Exception, _log_error)
    @catch(PageNotFoundError, ret=None)
    async def fetch(self, urls: list[str], marketplace: str) -> AsyncGenerator[str, str | None]:
        """Call the fetch function from the respective marketplace."""

        fetcher = get_marketplace_fetcher(marketplace, self._logger)
        return await fetcher.fetch(urls)
