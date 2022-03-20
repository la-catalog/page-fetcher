from typing import Iterator
from la_catch import catch
from page_fetcher.logs import *
from page_fetcher.options import get_marketplace_fetcher
from page_fetcher.exceptions import TooManyRequestsError, NotFoundError
from page_fetcher.abstractions import FetcherAbstraction


class Fetcher(FetcherAbstraction):
    @catch(Exception, log_error)
    @catch(NotFoundError, log_not_found)
    @catch(TooManyRequestsError, log_too_many_requests)
    async def fetch(self, urls: list[str], marketplace: str) -> Iterator[str]:
        fetcher = get_marketplace_fetcher(marketplace)
        contents = await fetcher.fetch(urls)
        return contents

    async def cooldown(self, marketplace: str) -> None:
        fetcher = get_marketplace_fetcher(marketplace)
        await fetcher.cooldown()
