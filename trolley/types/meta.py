class Meta:
    """
    A class representing generic meta object returned by
    the Trolley API in response to index methods/requests, containing
    pagination information.
    """

    _attributes = {
        'page': "",
        'pages': "",
        'records': ""
    }

    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""

        fields = [
            'page',
            'pages',
            'records',
        ]

        for field in fields:
            if attributes.get('meta') is None:
                Meta._attributes[field] = attributes.get(field)
            elif attributes['meta'].get(field) is not None:
                Meta._attributes[field] = attributes['meta'][field]

        return Meta._attributes

    @staticmethod
    def factory(attributes):
        """Creates an instance of Meta and returns it. """
        instance = Meta._initialize(attributes)
        return instance
