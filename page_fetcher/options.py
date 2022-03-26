from structlog.stdlib import BoundLogger

from page_fetcher.exceptions import UnknowMarketplaceError
from page_fetcher.abstractions import Marketplace
from page_fetcher.marketplaces.rihappy import Rihappy
from page_fetcher.marketplaces.google_shopping import GoogleShopping

options: dict[Marketplace] = {
    "google_shopping": GoogleShopping,
    "rihappy": Rihappy,
}


def get_marketplace_fetcher(marketplace: str, logger: BoundLogger) -> Marketplace:
    try:
        log = logger.bind(marketplace=marketplace)
        return options[marketplace](log)
    except KeyError as e:
        raise UnknowMarketplaceError(
            f"Marketplace '{marketplace}' is not defined in page_fetcher package"
        ) from e
