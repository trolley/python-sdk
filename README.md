[![Latest Stable Version](https://img.shields.io/pypi/v/paymentrails.svg)](https://pypip.python.org/pypi/paymentrails)


# Payment Rails Python SDK

A native Python SDK for the Payment Rails API


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

Configuration.set_public_key("public_key")
Configuration.set_private_key("private_key")
response = Recipient.find('R-91XPYX3V2MM1G')
print(response.id)
```


## Documentation for API Endpoints

All URIs are available at http://docs.paymentrails.com/
 

All URIs are relative to *https://api.paymentrails.com/v1*

Class | Method | HTTP request
------------ | ------------- | -------------
*Recipient | [**find**](docs/Recipient.md#find) | **FIND** /recipient/
*Recipient | [**create**](docs/Recipient.md#create) | **CREATE** /recipient/
*Recipient | [**update**](docs/Recipient.md#update) | **UPDATE** /recipient/
*Recipient | [**delete**](docs/Recipient.md#delete) | **DELETE** /recipient/
*Recipient | [**search**](docs/Recipient.md#search) | **FIND** /recipient/
*RecipientAccounts | [**find**](docs/RecipientAccounts.md#find) | **FIND** /recipient/<recipient_id>/accounts/recipientAccountId
*RecipientAccounts | [**create**](docs/RecipientAccounts.md#create) | **CREATE** /recipient/<recipient_id>/accounts
*RecipientAccounts | [**update**](docs/RecipientAccounts.md#update) | **UPDATE** /recipient/<recipient_id>/accounts/recipientAccountId
*RecipientAccounts | [**delete**](docs/RecipientAccounts.md#remove) | **DELETE** /recipient/<recipient_id>/accounts/recipientAccountId
*Batch | [**find**](docs/Batch.md#find) | **FIND** /batch/
*Batch | [**create**](docs/Batch.md#create) | **CREATE** /batch/
*Batch | [**update**](docs/Batch.md#update) | **UPDATE** /batch/
*Batch | [**delete**](docs/Batch.md#delete) | **DELETE** /batch/
*Batch | [**search**](docs/Batch.md#search) | **FIND** /batch/
*Batch | [**generateQuote**](docs/Batch.md#generateQuote) | **CREATE** /batch/
*Batch | [**processBatch**](docs/Batch.md#processBatch) | **CREATE** /batch/
*Batch | [**summary**](docs/Batch.md#summary) | **FIND** /batch/
*Payment | [**find**](docs/Payment.md#find) | **FIND** /payments/
*Payment | [**create**](docs/Payment.md#create) | **CREATE** /batch/<batch_id>/payments
*Payment | [**update**](docs/Payment.md#update) | **UPDATE** /batch/<batch_id>/payments
*Payment | [**delete**](docs/Payment.md#delete) | **DELETE** /batch/<batch_id>/payments
*Payment | [**search**](docs/Payment.md#search) | **FIND** /payments/
*Balances | [**find**](docs/Balances.md#find) | **FIND** /balances/











## Documentation for Authorization

### merchantKey

- **Type**: Authorization
- **Authorization parts**: Access code, Secret code
- **Location**: HTTP header
