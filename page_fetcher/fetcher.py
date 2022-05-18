from collections.abc import AsyncGenerator
from typing import Any, Tuple

from la_catch import catch
from structlog.stdlib import BoundLogger, get_logger

from page_fetcher.exceptions import PageNotFoundError
from page_fetcher.options import get_marketplace_fetcher


class Fetcher:
    """
    Fetcher is responsible for scraping content from pages and dealing
    with unexpected response from the marketplaces.

    It should be focus on collecting content and not parsing
    or analysing it.
    """

    def __init__(self, logger: BoundLogger = get_logger()) -> None:
        self._logger = logger.bind(lib="page_fetcher")

    def _log_error(
        self, urls: list[str], marketplace: str, exception: Exception
    ) -> None:
        self._logger.exception(
            event="Fetcher error",
            urls=urls,
            marketplace=marketplace,
        )

    @catch(Exception, _log_error)
    @catch(PageNotFoundError, ret=None)
    async def fetch(
        self,
        urls: list[str],
        marketplace: str,
        *args: tuple[Any],
        **kwargs: dict[str, Any],
    ) -> AsyncGenerator[Tuple[str | None, str], str | None]:
        """Call the fetch function from the respective marketplace."""

        fetcher = get_marketplace_fetcher(marketplace, self._logger)
        return fetcher.fetch(urls, *args, **kwargs)
