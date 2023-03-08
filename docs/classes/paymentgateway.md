[Trolley Python SDK](../README.md) > [PaymentGateway](../classes/paymentgateway.md)



# Class: PaymentGateway

## Index

### Methods

* [create](paymentgateway.md#create)
* [find](paymentgateway.md#find)
* [remove](paymentgateway.md#remove)
* [search](paymentgateway.md#search)
* [update](paymentgateway.md#update)



---
## Methods
<a id="create"></a>

###  create

► **create**(batchId: *`string`*, body: *`string`*): `Payment`



*Defined in [PaymentGateway.py:55](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/PaymentRails_Gateway.py#L55)*



Create a new payment in a batch

    payload = {"payments": [{"recipient": {"id": "R-4625iLug2GKqKZG2WzAf3e"},
    "sourceAmount": "65", "memo": "", "sourceCurrency": "USD"}]}
    client.payment.create("B-decj8wnef7euc8d",payload)

**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| batchId | `string`   |  Trolley payment id (e.g. "B-xx999bb") |
| body | `string`   |  Payment information |





**Returns:** ` Payment`





___

<a id="find"></a>

###  find

► **find**(paymentId: *`string`*): ` Payment`



*Defined in [PaymentGateway.py:34](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/PaymentRails_Gateway.py#L34)*



Find a specific payment

    payment = client.payment.find('P-aabbccc');


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| paymentId | `string`   |  Trolley payment id (e.g. "P-aabccc") |





**Returns:** ` Payment`





___

<a id="remove"></a>

###  remove

► **remove**(paymentId: *`string`*, batchId: *`string`*): `boolean`



*Defined in [PaymentGateway.py:90](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/PaymentRails_Gateway.py#L90)*



Delete a given payment -- Note you can only delete non processed payments

    success = client.payment.remove('P-aabbccc', 'B-xx99bb');


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| paymentId | `string`   |  Trolley payment id (e.g. "P-aabccc") |
| batchId | `string`   |  Trolley payment id (e.g. "B-xx999bb") |





**Returns:** `boolean`





___

<a id="search"></a>

###  search

► **search**(batchId: *`string`*, page?: *`number`*, pageSize?: *`number`*, term?: *`string`*): `List<Payment>`



*Defined in [PaymentGateway.py:105](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/PaymentRails_Gateway.py#L105)*



Search for payments in a given batch


**Parameters:**

| Param | Type | Default value | Description |
| ------ | ------ | ------ | ------ |
| batchId | `string`  | - |   Trolley payment id (e.g. "B-xx999bb") |
| page | `number`  | 1 |   Page number (1 based) |
| pageSize | `number`  | 10 |   Page size (0...1000) |
| term | `string`  | &quot;&quot; |   Any search terms to look for |





**Returns:** `List<Payment>`





___

<a id="update"></a>

###  update

► **update**(paymentId: *`string`*, batchId: *`string`*, body: *`string`*): `boolean`



*Defined in [PaymentGateway.py:74](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/PaymentRails_Gateway.py#L74)*



Update a given payment
    payload =  {"update_payments": [ {"id": "P-RV84yv4HVYJDK6DG6DjRNG", "sourceAmount": "999"}]}
    success = client.payment.update('P-RV84yv4HVYJDK6DG6DjRNG', 'B-few4t5ygaefSERGfgr', payload)


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| paymentId | `string`   |  Trolley payment id (e.g. "P-aabccc") |
| batchId | `string`   |  Trolley payment id (e.g. "B-xx999bb") |
| body | `string`   |  Payment update information |





**Returns:** `boolean`





___


