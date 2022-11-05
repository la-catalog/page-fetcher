import asyncio
from collections.abc import AsyncGenerator
from typing import Tuple

from aiohttp import ClientSession
from la_headers import generate_random_headers
from page_models import URL

from page_fetcher.abstractions import Marketplace


class MercadoLivre(Marketplace):
    async def fetch(
        self, urls: list[URL]
    ) -> AsyncGenerator[Tuple[str | None, URL], URL | None]:
        headers = generate_random_headers(os=["linux"], browser=["chrome"])

        async with ClientSession(headers=headers) as session:
            for url in urls:
                while url:
                    async with session.get(url) as response:
                        self._logger.info(
                            event="Response received",
                            status=response.status,
                            url=url,
                            marketplace=self._marketplace,
                        )

                        if response.status == 429:
                            self._logger.debug(event=f"Start cooldown")
                            await asyncio.sleep(1)

                        response.raise_for_status()

                        text = await response.text()
                        url = yield (text, url)
