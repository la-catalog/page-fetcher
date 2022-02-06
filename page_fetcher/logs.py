from page_fetcher.fetcher import Fetcher
from page_fetcher.exceptions import TooManyRequestsError, NotFoundError


def log_too_many_requests(
    fetcher: Fetcher, url: str, marketplace: str, exception: TooManyRequestsError
) -> None:
    fetcher.logger.info(
        message="Too many requests",
        data={"url": url, "marketplace": marketplace},
        exception=exception,
    )

    fetcher.cooldown(marketplace)

    raise


def log_not_found(
    fetcher: Fetcher, url: str, marketplace: str, exception: NotFoundError
) -> None:
    fetcher.logger.info(
        message="Not found",
        data={"url": url, "marketplace": marketplace},
        exception=exception,
    )

    raise
