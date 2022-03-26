from typing import Iterator
from la_catch import catch

from page_fetcher.options import get_marketplace_fetcher
from page_fetcher.exceptions import PageNotFoundError
from page_fetcher.abstractions import FetcherAbstraction


class Fetcher(FetcherAbstraction):
    def log_error(self, urls: list[str], marketplace: str, exception: Exception) -> None:
        self._logger.exception(
            event="Fetcher error",
            urls=urls,
            marketplace=marketplace,
        )
    
    @catch(Exception, log_error)
    @catch(PageNotFoundError, ret=None)
    async def fetch(self, urls: list[str], marketplace: str) -> Iterator[str]:
        fetcher = get_marketplace_fetcher(marketplace, self._logger)
        return await fetcher.fetch(urls)
