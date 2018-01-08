from paymentrails.configuration import Configuration


class Batch:
    """
    A class that facilitates Client requests to
    the PaymentRails API in regards to Batches.
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
        "totalPayments": "",
        "updatedAt": "",
    }

    @staticmethod
    def find(batch_id):
        """
        Retrieve a batch
            A batch_id is required::
            Batch.find('B-fjeracjmuflh')
        """
        return Configuration.gateway().batch.find(batch_id)

    @staticmethod
    def create(body):
        """
        Create a batch
            A body is required::
            Batch.create(
                {"payments":[{"recipient":{"id":"R-SBAHDK3DK6M7SUEM"},
                "sourceAmount":"65","memo":"","sourceCurrency":"CAD"}]})
        """
        return Configuration.gateway().batch.create(body)

    @staticmethod
    def update(batch_id, body):
        """
        Update a batch
            A batch_id and body are required::
            Batch.update('B-fjeracjmuflh',{"payments":[{"recipient":{"id":"R-3DF7FAF680739541",
            "email":"jsmith@example.com"},"sourceAmount":65,"memo":"Salary",
            "sourceCurrency":"CAD"}]})
        """
        return Configuration.gateway().batch.update(batch_id, body)

    @staticmethod
    def delete(batch_id):
        """
        Delete a batch
            A batch_id is required::
            Batch.delete('B-fjeracjmuflh')
        """
        return Configuration.gateway().batch.delete(batch_id)

    @staticmethod
    def search(page=1, page_number=10, term=""):
        """
        Query for a batch
            Batch.search(1,10,'test')
        """
        return Configuration.gateway().batch.search(page, page_number, term)

    @staticmethod
    def summary(batch_id):
        """
        Retrieve a summary about a specific batch
            A batch_id is required::
            Batch.summary('B-fjeracjmuflh')
        """
        return Configuration.gateway().batch.summary(batch_id)

    @staticmethod
    def generate_quote(batch_id):
        """
        Generate a quote for a batch
            A batch_id is required::
            Batch.generate_quote('B-fjeracjmuflh')
        """
        return Configuration.gateway().batch.generate_quote(batch_id)

    @staticmethod
    def process_batch(batch_id):
        """
        Process a batch
            A batch_id is required::
            Batch.process_batch('B-fjeracjmuflh')
        """
        return Configuration.gateway().batch.process_batch(batch_id)

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
            "totalPayments",
            "updatedAt",
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
