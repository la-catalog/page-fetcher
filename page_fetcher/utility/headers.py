from accept_gen import generate_accept
from accept_encoding_gen import generate_accept_encoding

class Headers:
    def __init__(self):
        self._headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
            "accept_encoding": "gzip, deflate, br",
            "accept_language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        }

    def __str__(self):
        return str(self._headers)

    def fake_chrome(self, version):
        self._headers |= {
            "accept_encoding": generate_accept_encoding("chrome", version),
            "accept": generate_accept("chrome", version),
        }
