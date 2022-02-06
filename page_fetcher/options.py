from page_fetcher.exceptions import UnknowMarketplaceError
from page_fetcher.abstractions import MarketplaceAbstraction
from page_fetcher.marketplaces.google_shopping import GoogleShopping

options = {
    "google shopping": GoogleShopping
}


def get_marketplace_fetcher(marketplace: str) -> MarketplaceAbstraction:
    try:
        return options["marketplace"]()
    except KeyError as e:
        raise UnknowMarketplaceError(
            f"Marketplace '{marketplace}' is not defined in page_fetcher package"
        ) from e
