class UnknowMarketplaceError(Exception):
    pass


class TooManyRequestsError(Exception):
    def __init__(self, extra: dict):
        self.extra = extra


class NotFoundError(Exception):
    def __init__(self, extra: dict):
        self.extra = extra


class UnexpectedStatusError(Exception):
    def __init__(self, extra: dict):
        self.extra = extra
