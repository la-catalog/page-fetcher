from page_fetcher.exceptions import TooManyRequestsError, NotFoundError
from page_fetcher.abstractions import FetcherAbstraction


def log_too_many_requests(
    fetcher: FetcherAbstraction,
    url: str,
    marketplace: str,
    exception: TooManyRequestsError,
) -> None:
    fetcher.logger.info(
        message="Too many requests",
        data={"url": url, "marketplace": marketplace},
        exception=exception,
    )

    fetcher.cooldown(marketplace)

    raise


def log_not_found(
    fetcher: FetcherAbstraction, url: str, marketplace: str, exception: NotFoundError
) -> None:
    fetcher.logger.info(
        message="Not found",
        data={"url": url, "marketplace": marketplace},
        exception=exception,
    )

    return


def log_error(
    fetcher: FetcherAbstraction, url: str, marketplace: str, exception: Exception
) -> None:
    ignored_exceptions = (TooManyRequestsError, StopIteration)

    if not isinstance(exception, ignored_exceptions):
        fetcher.logger.info(
            message="Fetcher error",
            data={"url": url, "marketplace": marketplace},
            exception=exception,
        )

    raise
