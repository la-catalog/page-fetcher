from user_agent import generate_navigator

from page_fetcher.utility.weight import generate_quality_values
from page_fetcher.template import Template

class Amazon(Template):
    def fetch(self, url : str) -> str:
        return ""
    
    def cooldown(self) -> None:
        return None

    def _headers(self) -> dict:
        navigator = generate_navigator()

        return {
            "User-Agent": navigator["user_agent"],
            "Accept": generate_quality_values(
                priority=[
                    "application/signed-exchange;v=b3",
                    "application/xml",
                    "*/*",
                ],
                weightless=[
                    "text/html",
                    "application/xhtml+xml",
                    "image/avif",
                    "image/webp",
                    "image/apng",
                ],
            ),
            "Accept-Enconding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
        }