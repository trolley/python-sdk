[![Latest Stable Version](https://img.shields.io/pypi/v/paymentrails.svg)](https://pypi.python.org/pypi/paymentrails)


# Payment Rails[^1] Python SDK

A native Python SDK for the Payment Rails API

[^1]: [Payment Rails is now Trolley](https://www.trolley.com/payment-rails-is-now-trolley-series-a), we'll be updating our SDKs to support the new domain during the first half of 2022.

## Installation

#

#### For [Python](https://www.python.org/)

#
#### To install the reference:

## Dependencies

* Python
* [requests](http://docs.python-requests.org/en/latest/)

## Getting Started

```python
from paymentrails.configuration import Configuration
from paymentrails.recipients import Recipients

client = Configuration.gateway("YOUR-PUBLIC-API","YOUR-PRIVATE-API","production")
response = client.recipient.find("R-WJniNq7PUXyboAJetimmJ4")

print(response.id)
```



## Documentation for API Endpoints

All URIs are available at http://docs.paymentrails.com/
 
All URIs are relative to *https://api.paymentrails.com/v1*


### Usage

Methods should all have Python Doc comments to help you understand their usage. As mentioned the [full API documentation](http://docs.paymentrails.com)
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
