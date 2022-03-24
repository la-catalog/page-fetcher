from page_fetcher.exceptions import StatusError
from page_fetcher.abstractions import FetcherAbstraction


def log_status_error(
    fetcher: FetcherAbstraction,
    url: str,
    marketplace: str,
    exception: StatusError,
) -> None:

    fetcher.logger.warning(
        message="Status error",
        data={
            "lib": "page_fetcher",
            "status": exception.status,
            "url": url,
            "marketplace": marketplace,
            "extra": exception.extra,
        },
        exception=exception,
    )

    if exception.status == 404:
        return

    if exception.status == 429:
        fetcher.cooldown(marketplace)

    raise


def log_error(
    fetcher: FetcherAbstraction,
    url: str,
    marketplace: str,
    exception: Exception,
) -> None:

    if not isinstance(exception, StatusError):
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
