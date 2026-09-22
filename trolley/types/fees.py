class RoutePricing:
    """
    A class representing route pricing for one fee currency.
    """

    _fields = (
        "currencyCode",
        "revenueStream",
    )

    @staticmethod
    def factory(attributes):
        return {field: attributes.get(field) for field in RoutePricing._fields}


class RevenueStream:
    """
    A class representing a Revenue Stream configuration.
    """

    _fields = (
        "currencyCode",
        "integration",
        "routeType",
        "merchantAmountType",
        "merchantAmount",
        "guardrails",
        "percentCap",
        "revenueShareId",
    )

    @staticmethod
    def factory(attributes):
        return {field: attributes.get(field) for field in RevenueStream._fields}
