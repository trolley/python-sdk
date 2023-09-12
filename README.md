[![Latest Stable Version](https://img.shields.io/pypi/v/trolleyhq.svg)](https://pypi.python.org/pypi/trolleyhq)

# Trolley Python SDK

A native [Python](https://www.python.org/) SDK for the Trolley API



## Installation

Use pip to install the latest version of the package

```
$ pip install trolleyhq
```



#### Dependencies

* Python
* [requests](http://docs.python-requests.org/en/latest/)
* [Mock](https://pypi.org/project/mock/) - For unit tests



## Getting Started

```python
from trolley.configuration import Configuration
from trolley.recipients import Recipients

client = Configuration.gateway("ACCESS_KEY","SECRET_KEY")
response = client.recipient.find("R-WJniNq7PUAJetimmJ4")

print(response.id)
```



## Running Tests

```
// unit tests
$ python -m unittest test/unit/testBalances.py

//integration tests
$ python test/integration/RecipientTest.py
```



## Documentation

Documentation about how to use our Python SDK is available at https://docs.trolley.com/

Besides that, methods should all have Python Doc comments to help you understand their usage.
