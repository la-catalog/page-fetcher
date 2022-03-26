from page_fetcher.exceptions import StatusError
from page_fetcher.abstractions import FetcherAbstraction


def log_status_error(
    fetcher: FetcherAbstraction,
    urls: str,
    marketplace: str,
    exception: StatusError,
) -> None:

    fetcher.logger.warning(
        event="Status error",
        data={
            "status": exception.status,
            "urls": urls,
            "marketplace": marketplace,
            "extra": exception.extra,
        }
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
        fetcher.logger.exception(
            message="Fetcher error",
            data={
                "url": url,
                "marketplace": marketplace,
            }
        )

    raise
