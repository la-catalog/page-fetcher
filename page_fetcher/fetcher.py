from typing import Iterator
from la_catch import catch

from page_fetcher.logs import log_error, log_status_error
from page_fetcher.options import get_marketplace_fetcher
from page_fetcher.exceptions import StatusError
from page_fetcher.abstractions import FetcherAbstraction


class Fetcher(FetcherAbstraction):
    @catch(Exception, log_error)
    @catch(StatusError, log_status_error)
    async def fetch(self, urls: list[str], marketplace: str) -> Iterator[str]:
        fetcher = get_marketplace_fetcher(marketplace)
        contents = await fetcher.fetch(urls)
        return contents

    async def cooldown(self, marketplace: str) -> None:
        fetcher = get_marketplace_fetcher(marketplace)
        await fetcher.cooldown()
