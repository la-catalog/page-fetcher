import os
from page_fetcher.abstractions import MarketplaceAbstraction


class GoogleShopping(MarketplaceAbstraction):
    def __init__(self):
        os.system("playwright install")
        os.system("playwright install-deps")

    def fetch(self, url: str) -> list:
        pass