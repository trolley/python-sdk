from enum import Enum

class InvoiceLine:

    class categories:
        services        =  'services' 	        # Services
        rent            =  'rent'  	            # Rent
        royalties       =  'royalties' 	        # Royalties
        royalties_film  =  'royalties_film'	    # Royalties Film & TV
        prizes          =  'prizes' 	        # Prize payment
        education       =  'education' 	        # Education
        refunds         =  'refunds' 	        # Refunds

    _attributes = {
        'id' : "",
        'status' : "",
        'unitAmount' : "",
        'taxAmount' : "",
        'totalAmount' : "",
        'dueAmount' : "",
        'paidAmount' : "",
        'category' : "",
        'royalties' : "",
        'description' : "",
        'externalId' : "",
        'taxReportable' : "",
        'forceUsTaxActivity' : "",
        'tags' : ""
    }

    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""

        fields = [
            'id',
            'status',
            'unitAmount',
            'taxAmount',
            'totalAmount',
            'dueAmount',
            'paidAmount',
            'category',
            'royalties',
            'description',
            'externalId',
            'taxReportable',
            'forceUsTaxActivity',
            'tags'
        ]

        for field in fields:
            if attributes.get('invoiceLine') is None:
                InvoiceLine._attributes[field] = attributes.get(field)
            elif attributes['invoiceLine'].get(field) is not None:
                InvoiceLine._attributes[field] = attributes['invoiceLine'][field]

        return InvoiceLine._attributes

    @staticmethod
    def factory(attributes):
        """Creates an instance of Payment and returns it. """
        instance = InvoiceLine._initialize(attributes)
        return instance
