class Batch:
    """
    A class representing Batch object.
    """

    _attributes = {
        "id": "",
        "amount": "",
        "completedAt": "",
        "createdAt": "",
        "currency": "",
        "description": "",
        "sentAt": "",
        "status": "",
        "tags": "",
        "totalPayments": "",
        "updatedAt": "",
        "quoteExpiredAt": "",
        "payments": "",
    }

    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""
        fields = [
            "id",
            "amount",
            "completedAt",
            "createdAt",
            "currency",
            "description",
            "sentAt",
            "status",
            "tags",
            "totalPayments",
            "updatedAt",
            "quoteExpiredAt",
            "payments",
        ]

        for field in fields:
            if attributes.get('batch') is None:
                Batch._attributes[field] = attributes.get(field)
            elif attributes['batch'].get(field) is not None:
                Batch._attributes[field] = attributes['batch'][field]

        return Batch._attributes

    @staticmethod
    def factory(attributes):
        """Creates an instance of Batch and returns it. """
        instance = Batch._initialize(attributes)
        return instance

    @staticmethod
    def find(batch_id):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).batch.find(batch_id)

    @staticmethod
    def create(body):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).batch.create(body)

    @staticmethod
    def update(batch_id, body):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).batch.update(batch_id, body)

    @staticmethod
    def delete(batch_id):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).batch.delete(batch_id)

    @staticmethod
    def search(page=1, page_size=10, term=""):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).batch.search_by_page(term, page, page_size)

    @staticmethod
    def summary(batch_id):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).batch.summary(batch_id)

    @staticmethod
    def generate_quote(batch_id):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).batch.generate_quote(batch_id)

    @staticmethod
    def process_batch(batch_id):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).batch.process_batch(batch_id)
