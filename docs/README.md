


#  Trolley Python SDK

## Index

### Packages

* [Exceptions](packages/exceptions.md)


### Classes

* [BalancesGateway](classes/balancesgateway.md)
* [BatchGateway](classes/batchgateway.md)
* [Configuration](classes/configuration.md)
* [Gateway](classes/gateway.md)
* [PaymentGateway](classes/paymentgateway.md)
* [RecipientAccount](classes/recipientaccount.md)
* [RecipientAccountGateway](classes/recipientaccountgateway.md)
* [RecipientGateway](classes/recipientgateway.md)


### Types

* [Batch](types/batch.md)
* [ConfigurationParams](types/configurationparams.md)
* [Payment](types/payment.md)
* [Recipient](types/recipient.md)


---


Create a client for the Trolley Python API


	client = Configuration.gateway("YOUR-PUBLIC-API","YOUR-PRIVATE-API","production")

**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| publicKey | [String]   |  The public key |
| secretKey | [String]   |  The secret key |
| enviroment | [String]   |  The enviroment that should be used |





**Returns:** [Gateway](classes/gateway.md)





___


