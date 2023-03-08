[![Latest Stable Version](https://img.shields.io/pypi/v/paymentrails.svg)](https://pypi.python.org/pypi/paymentrails)


# Trolley Python SDK (Previously Payment Rails[^1])

A native Python SDK for the Trolley API

[^1]: [Payment Rails is now Trolley](https://www.trolley.com/payment-rails-is-now-trolley-series-a). We're in the process of updating our SDKs to support the new domain. In this transition phase, you might still see "PaymentRails" at some places.

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
from paymentrails.configuration import Configuration
from paymentrails.recipients import Recipients

client = Configuration.gateway("YOUR-PUBLIC-API","YOUR-PRIVATE-API","production")
response = client.recipient.find("R-WJniNq7PUXyboAJetimmJ4")

print(response.id)
```



## Documentation for API Endpoints

All URIs are available at https://docs.trolley.com/
 
All URIs are relative to *https://api.trolley.com/v1*


### Usage

Methods should all have Python Doc comments to help you understand their usage. As mentioned the [full API documentation](https://docs.trolley.com)
is the best source of information about the API.

For more information please read the [Python API docs](https://github.com/PaymentRails/python-sdk/tree/master/docs/) is available. The best starting point is:

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
