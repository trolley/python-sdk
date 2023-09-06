
class Log:
    """
    A class that facilitates Client requests to
    the Trolley API in regards to Recipient Log.
    """

    _attributes = {
        "via": "",
        "ipAddress": "",
        "userId": "",
        "type": "",
        "fields": "",
        "createdAt": ""
    }

    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""

        fields = [
            "via",
            "ipAddress",
            "userId",
            "type",
            "fields",
            "createdAt"
        ]

        for field in fields:
            if attributes.get('recipientLog') is None:
                Log._attributes[field] = attributes.get(field)
            elif attributes['recipientLog'].get(field) is not None:
                Log._attributes[field] = attributes['recipient'][field]

        return Log._attributes

    @staticmethod
    def factory(attributes):
        """Creates an instance of Log and returns it. """
        instance = Log._initialize(attributes)
        return instance
