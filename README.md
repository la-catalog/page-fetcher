# page-fetcher
Use esse pacote para pegar a página HTML de um marketplace.  

Esse pacote apenas existe para evitar escrever a mesma lógica de fetch em diversos cron jobs. Não existe regra sobre o que usar para pegar a página HTML, então use a ferramenta que preferir (requests/aiohttp/selenium/pyppeteer/playwright).  

# install
`pdm add git+https://github.com/la-catalog/page-fetcher.git`  

# usage

### page_fetcher.Fetcher.fetch(urls, marketplaces)
O uso normal do pacote envolve você apenas passar uma lista de urls a serem scrapeados e a configuração de marketplace a ser usada. O retorno é um *AsyncGenerator* para se processar as páginas retornadas aos poucos.  

```python
import asyncio
from page_fetcher import Fetcher


async def main():
    fetcher = Fetcher()
    pages = await fetcher.fetch(
        urls=["https://www.google.com/shopping/product/r/BR/16567145044483249038"],
        marketplace="google_shopping"
    )

    async for page, url in pages:
        # do something with the html page
        print(page)


asyncio.run(main())
```

Nem sempre se possui todos os urls no início da chamda da função, por isso é possível enviar para o *AsyncGenerator* mais urls a serem scrapeados com `asend()`.  

```python
import re
import asyncio
from page_fetcher import Fetcher


async def main():
    fetcher = Fetcher()
    pages = await fetcher.fetch(
        urls=["https://www.amazon.com.br/dp/B09XFLCKCZ"],
        marketplace="amazon"
    )

    async for page, url in pages:
        # find another url
        ASIN = re.search("data-asin=([A-Z0-9]*)")

        another_url = f"https://www.amazon.com.br/dp/{ASIN}"
        another_page, another_url = pages.asend(another_url)

        # do something with the html page
        print(another_page)


asyncio.run(main())
```

# new marketplace


# references
[PEP 525 - Asynchronous Generators](https://peps.python.org/pep-0525/)  
[Yield expressions](https://docs.python.org/3/reference/expressions.html#yield-expressions)  
[Asynchronous generator functions](https://docs.python.org/3/reference/expressions.html#asynchronous-generator-functions)  