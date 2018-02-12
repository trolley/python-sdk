[Payment Rails Python SDK](../README.md) > [balances_gateway](../classes/balances_gateway.md)



# Class: BalancesGateway

## Index

### Methods

* [find](balancesgateway.md#find)



---


## Methods

___

<a id="find"></a>

###  find

► **find**(kind: *"paypal"⎮"paymentrails"*): `Balance`



*Defined in [balances_gateway.py:49](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/balances_gateway.py#L49)*



Fetch the account balance for the given account type

    balances = client.balances.find("paymentrails")


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| kind | "paypal"⎮"paymentrails"   |  The account type to get the balances for |





**Returns:**  `Balances`





___


