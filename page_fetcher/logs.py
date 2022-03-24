from page_fetcher.exceptions import TooManyRequestsError, NotFoundError
from page_fetcher.abstractions import FetcherAbstraction


def log_too_many_requests(
    fetcher: FetcherAbstraction,
    url: str,
    marketplace: str,
    exception: TooManyRequestsError,
) -> None:
    fetcher.logger.warning(
        message="Too many requests",
        data={"lib": "page_fetcher", "url": url, "marketplace": marketplace},
        exception=exception,
    )

    fetcher.cooldown(marketplace)

    raise


def log_not_found(
    fetcher: FetcherAbstraction, url: str, marketplace: str, exception: NotFoundError
) -> None:
    fetcher.logger.warning(
        message="Not found",
        data={"lib": "page_fetcher", "url": url, "marketplace": marketplace},
        exception=exception,
    )

    return


def log_error(
    fetcher: FetcherAbstraction, url: str, marketplace: str, exception: Exception
) -> None:
    ignored_exceptions = (TooManyRequestsError, StopIteration)

    if not isinstance(exception, ignored_exceptions):
        fetcher.logger.error(
            message="Fetcher error",
            data={"lib": "page_fetcher", "url": url, "marketplace": marketplace},
            exception=exception,
        )

    raise
