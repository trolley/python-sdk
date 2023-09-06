[![Latest Stable Version](https://img.shields.io/pypi/v/trolleyhq.svg)](https://pypi.python.org/pypi/trolleyhq)


# Trolley Python SDK

A native Python SDK for the Trolley API

## Installation

#

#### For [Python](https://www.python.org/)

#
#### To install the reference:

## Dependencies

* Python
* [requests](http://docs.python-requests.org/en/latest/)
* [Mock](https://pypi.org/project/mock/) - For unit tests

## Running Tests

```
// unit tests
$ python -m unittest test/unit/testBalances.py

//integration tests
$ python test/integration/RecipientTest.py
```

## Getting Started

```python
from trolley.configuration import Configuration
from trolley.recipients import Recipients

client = Configuration.gateway("ACCESS_KEY","SECRET_KEY")
response = client.recipient.find("R-WJniNq7PUXyboAJetimmJ4")

print(response.id)
```

## Documentation for API Endpoints

All URIs are available at https://docs.trolley.com/
 
All URIs are relative to *https://api.trolley.com/v1*

### Usage

Methods should all have Python Doc comments to help you understand their usage. As mentioned the [full API documentation](https://docs.trolley.com)
is the best source of information about the API.

For more information please read the our docs at [https://docs.trolley.com](https://docs.trolley.com).  
The [Python API docs](https://github.com/PaymentRails/python-sdk/tree/master/docs/) can be found in this repo. The best starting point is:

| Data Type | SDK Documentation |
| ----- | ----- |
| Batch | [API Docs for Batch](https://github.com/PaymentRails/python-sdk/tree/master/docs/classes/batchgateway.md) |
| Payment | [API Docs for Payment](https://github.com/PaymentRails/python-sdk/tree/master/docs/classes/paymentgateway.md) |
| Recipient | [API Docs for Recipient](https://github.com/PaymentRails/python-sdk/tree/master/docs/classes/recipientgateway.md) |
| Recipient Account | [API Docs for Recipient Account](https://github.com/PaymentRails/python-sdk/tree/master/docs/classes/recipientaccountgateway.md) |







## Documentation for Authorization

### merchantKey

- **Type**: Authorization
- **Authorization parts**: public key, secret key
- **Location**: HTTP header
