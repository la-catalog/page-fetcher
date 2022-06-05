from collections.abc import AsyncGenerator
from datetime import datetime
from typing import Any, Tuple

from la_catch import catch
from la_stopwatch import Stopwatch
from structlog.stdlib import BoundLogger, get_logger

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

    def _on_fetch_error(
        self,
        urls: list[str],
        marketplace: str,
        exception: Exception,
        *args,
        **kwargs,
    ) -> None:
        self._logger.exception(
            event="Fetcher error",
            urls=urls,
            marketplace=marketplace,
        )

        raise

    def _on_fetch_finish(
        self,
        urls: list[str],
        marketplace: str,
        duration: datetime,
        *args,
        **kwargs,
    ) -> None:
        self._logger.info(
            event="Fetcher finish",
            urls=urls,
            marketplace=marketplace,
            duration=str(duration),
        )

    @catch(Exception, _on_fetch_error)
    @Stopwatch(_on_fetch_finish)
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
