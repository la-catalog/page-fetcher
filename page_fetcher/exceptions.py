class UnknowMarketplaceError(Exception):
    pass


class StatusError(Exception):
    def __init__(self, status: int, extra: dict):
        self.status = status
        self.extra = extra
