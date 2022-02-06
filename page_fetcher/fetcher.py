from la_catch import catch
from page_fetcher.logs import log_not_found, log_too_many_requests
from page_fetcher.options import get_marketplace_fetcher
from page_fetcher.exceptions import TooManyRequestsError, NotFoundError
from page_fetcher.abstractions import FetcherAbstraction


class Fetcher(FetcherAbstraction):
    @catch(NotFoundError, log_not_found)
    @catch(TooManyRequestsError, log_too_many_requests)
    def fetch(self, urls: list[str], marketplace: str) -> list[str]:
        marketplace_fetcher = get_marketplace_fetcher(marketplace)
        return marketplace_fetcher.fetch(urls)

    def cooldown(self, marketplace: str) -> None:
        marketplace_fetcher = get_marketplace_fetcher(marketplace)
        marketplace_fetcher.cooldown()
