from page_fetcher.exceptions import UnknowMarketplaceError


class Options:
    def __init__(self):
        self._options = {}

    def get(self, marketplace):
        try:
            return self._options["marketplace"]
        except KeyError as e:
            raise UnknowMarketplaceError(
                f"Marketplace '{marketplace}' is not defined in page_fetcher package"
            ) from e
