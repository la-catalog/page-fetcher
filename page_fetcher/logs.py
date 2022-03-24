from page_fetcher.exceptions import (
    TooManyRequestsError,
    NotFoundError,
    UnexpectedStatusError,
)
from page_fetcher.abstractions import FetcherAbstraction


def log_not_found(
    fetcher: FetcherAbstraction,
    url: str,
    marketplace: str,
    exception: NotFoundError,
) -> None:

    fetcher.logger.warning(
        message="Not found",
        data={
            "lib": "page_fetcher",
            "url": url,
            "marketplace": marketplace,
            "extra": exception.extra,
        },
        exception=exception,
    )

    return


def log_too_many_requests(
    fetcher: FetcherAbstraction,
    url: str,
    marketplace: str,
    exception: TooManyRequestsError,
) -> None:

    fetcher.logger.warning(
        message="Too many requests",
        data={
            "lib": "page_fetcher",
            "url": url,
            "marketplace": marketplace,
            "extra": exception.extra,
        },
        exception=exception,
    )

    fetcher.cooldown(marketplace)

    raise


def log_unexpected_status(
    fetcher: FetcherAbstraction,
    url: str,
    marketplace: str,
    exception: UnexpectedStatusError,
) -> None:

    fetcher.logger.warning(
        message="Unexpected status",
        data={
            "lib": "page_fetcher",
            "url": url,
            "marketplace": marketplace,
            "extra": exception.extra,
        },
        exception=exception,
    )

    raise


def log_error(
    fetcher: FetcherAbstraction,
    url: str,
    marketplace: str,
    exception: Exception,
) -> None:

    ignored_exceptions = (TooManyRequestsError, StopIteration)

    if not isinstance(exception, ignored_exceptions):
        fetcher.logger.error(
            message="Fetcher error",
            data={
                "lib": "page_fetcher",
                "url": url,
                "marketplace": marketplace,
            },
            exception=exception,
        )

    raise
