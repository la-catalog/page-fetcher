from page_fetcher.options import Options
from page_fetcher.exceptions import TooManyRequestsError, NotFoundError

class Fetcher:
    def __init__(self, logger):
        self._logger = logger
    
    def fetch(self, url : str, marketplace : str, *args, **kwargs) -> str:
        try:
            return self._fetch(url, marketplace, *args, **kwargs)
        except TooManyRequestsError:
            self._log_too_many_requests(url, marketplace)
            self._cooldown(marketplace)
            raise
        except NotFoundError:
            self._log_not_found(url, marketplace)
            raise
    
    def _fetch(self, url : str, marketplace : str, *args, **kwargs) -> str:
        marketplace = Options.get(marketplace)
        return marketplace.fetch(url, *args, **kwargs)
    
    def _cooldown(self, marketplace : str) -> None:
        marketplace = Options.get(marketplace)
        marketplace.cooldown()
    
    def _log_too_many_requests(self, url : str, marketplace : str) -> None:
        self._logger.info(
            message="Too many requests",
            data={
                "url": url,
                "marketplace": marketplace
            }
        )
    
    def _log_not_found(self, url : str, marketplace : str) -> None:
        self._logger.info(
            message="Not found",
            data={
                "url": url,
                "marketplace": marketplace
            }
        )
