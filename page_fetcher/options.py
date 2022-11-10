from logger_utility import WritePoint

from page_fetcher.abstractions import Marketplace
from page_fetcher.exceptions import UnknowMarketplaceError
from page_fetcher.marketplaces.google_shopping import GoogleShopping
from page_fetcher.marketplaces.mercado_livre import MercadoLivre
from page_fetcher.marketplaces.rihappy import Rihappy

options: dict[str, type[Marketplace]] = {
    "google_shopping": GoogleShopping,
    "rihappy": Rihappy,
    "mercado_livre": MercadoLivre,
}


def get_marketplace_fetcher(marketplace: str, logger: WritePoint) -> Marketplace:
    try:
        marketplace_class = options[marketplace]
        return marketplace_class(marketplace=marketplace, logger=logger)
    except KeyError as e:
        raise UnknowMarketplaceError(
            f"Marketplace '{marketplace}' is not defined in page_fetcher package"
        ) from e
