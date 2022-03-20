import asyncio
import requests
from la_headers import generate_headers

from page_fetcher.abstractions import Marketplace

class Rihappy(Marketplace):
    async def fetch(self, urls: list[str]) -> list[str]:
        headers = generate_headers("chrome", "99.0", "Linux", "desktop", "default")

        response = requests.get("https://www.rihappy.com.br/obexx-camera-robo-1080p-wifi-com-dispensador-de-petiscos-c-1002247924/p", headers=headers)
        
        return [response.text]
    
    async def cooldown(self) -> None:
        print("Rihappy: cooldown start")
        await asyncio.sleep(1)
        print("Rihappy: cooldown end")
        