from page_fetcher.exceptions import UnknowMarketplaceError
from page_fetcher.abstractions import Marketplace
from page_fetcher.marketplaces.rihappy import Rihappy
from page_fetcher.marketplaces.google_shopping import GoogleShopping

options = {
    "google shopping": GoogleShopping,
    "rihappy": Rihappy,
}


def get_marketplace_fetcher(marketplace: str) -> Marketplace:
    try:
        return options[marketplace]()
    except KeyError as e:
        raise UnknowMarketplaceError(
            f"Marketplace '{marketplace}' is not defined in page_fetcher package"
        ) from e
