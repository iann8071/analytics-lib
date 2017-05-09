from decimal import Decimal

class MRange:

    @classmethod
    def create(cls, _from, to, diff):
        _from = Decimal(_from)
        to = Decimal(to)
        diff = Decimal(diff)
        result = []
        while _from < to:
            result.append(_from)
            _from += diff
        return result