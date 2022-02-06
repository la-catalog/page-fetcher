from page_fetcher.exceptions import UnknowMarketplaceError


options = {}


def get_marketplace_fetcher(marketplace: str):
    try:
        return options["marketplace"]
    except KeyError as e:
        raise UnknowMarketplaceError(
            f"Marketplace '{marketplace}' is not defined in page_fetcher package"
        ) from e
