[Payment Rails Python SDK](../README.md) > [batch_gateway](../classes/batch_gateway.md)



# Class: batch_gateway


Gateway class for batches
*__class__*: batch_gateway


## Index

### Methods

* [create](batch_gateway.md#create)
* [find](batch_gateway.md#find)
* [generateQuote](batch_gateway.md#generatequote)
* [paymentList](batch_gateway.md#paymentlist)
* [delete](batch_gateway.md#delete)
* [search](batch_gateway.md#search)
* [processBatch](batch_gateway.md#processBatch)
* [summary](batch_gateway.md#summary)
* [update](batch_gateway.md#update)



---
## Methods
<a id="create"></a>

###  create

► **create**(batch: *`Batch`*): `Batch`



*Defined in [batch_gateway.py:95](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L95)*



Creates a batch with optional payments. This is the interface that is provide by the [Create Batch](http://docs.paymentrails.com/api/#create-a-batch) API

        payload = {"type": "individual", "firstName": "Tom",
                   "lastName": "Jones", "email": "test.create@example.com"}
        response = self.client.recipient.create(payload)
        recipient_id = response.id

        payload = {"type": "bank-transfer", "primary": "true", "country": "CA", "currency": "USD",
                   "accountNum": "604542847", "bankId": "123", "branchId": "47261",  "accountHolderName": "Tom Jones"}
        response = self.client.recipient_account.create(recipient_id, payload)

        payload = {"payments": [{"recipient": {
            "id": recipient_id}, "sourceAmount": "65", "memo": "", "sourceCurrency": "USD"}]}
        response = self.client.batch.create(payload)



**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| batch | `Batch`   |  - |





**Returns:** `Batch`





___

<a id="find"></a>

###  find

► **find**(batchId: *`string`*): `Batch`



*Defined in [batch_gateway.py:67](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L67)*



Retrieves a batch based on the batch id

    batch = client.batch.find('B-xx999bb');


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| batchId | `string`   |  Payment Rails batch id (e.g. "B-xx999bb") |





**Returns:** `Batch`





___

<a id="generatequote"></a>

###  generateQuote

► **generateQuote**(batchId: *`string`*): `Batch`



*Defined in [batch_gateway.py:182](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L182)*



Generate a FX quote for this batch


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| batchId | `string`   |  Payment Rails payment id (e.g. "B-xx999bb") |





**Returns:** `Batch`





___

<a id="paymentlist"></a>

###  paymentList

► **paymentList**(batchId: *`string`*, page?: *`number`*, pageSize?: *`number`*): `Payment`[]>



*Defined in [batch_gateway.py:166](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L166)*



Return a paginated list of payments for this batch


**Parameters:**

| Param | Type | Default value | Description |
| ------ | ------ | ------ | ------ |
| batchId | `string`  | - |   Payment Rails payment id (e.g. "B-xx999bb") |
| page | `number`  | 1 |   starting a 1 |
| pageSize | `number`  | 10 |   in the range 0...1000 |





**Returns:** `Payment`[]





___

<a id="delete"></a>

###  delete

► **delete**(batchId: *`string`*): `Boolean`


*Defined in [batch_gateway.py:132](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L132)*



Delete the given batch

    success = client.batch.delete('B-xx999bb');


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| batchId | `string`   |  Payment Rails batch (e.g. "B-xx999bb") |
| batch | `Batch`   |  Payment Rails batch |




**Returns:** `Boolean`





___

<a id="search"></a>

###  search

► **search**(page?: *`number`*, pageSize?: *`number`*, term?: *`string`*): `Batch`[]



*Defined in [batch_gateway.py:146](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L146)*



Search for a batch matching the given term


**Parameters:**

| Param | Type | Default value | Description |
| ------ | ------ | ------ | ------ |
| page | `number`  | 1 |   - |
| pageSize | `number`  | 10 |   - |
| term | `string`  | &quot;&quot; |   string search term |





**Returns:** `Batch`[]





___

<a id="processBatch"></a>

###  processBatch

► **processBatch**(batchId: *`string`*): `Batch`



*Defined in [batch_gateway.py:194](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L194)*



Start processing this batch


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| batchId | `string`   |  Payment Rails batch id (e.g. "B-xx999bb") |





**Returns:** `Batch`





___

<a id="summary"></a>

###  summary

► **summary**(batchId: *`string`*): `String`



*Defined in [batch_gateway.py:206](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L206)*



Get a transaction totaled summary for this batch


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| batchId | `string`   |  Payment Rails payment id (e.g. "B-xx999bb") |





**Returns:** `String`





___

<a id="update"></a>

###  update

► **update**(batch: *`Batch`*): `boolean`



*Defined in [batch_gateway.py:117](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L117)*



Update the batch data, note you can only update the information of a batch not the payments via this API

    payload = {"payments": [{"recipient": {"id": "R-4625iLug2GKqKZG2WzAf3e"},
    "sourceAmount": "65", "memo": "", "sourceCurrency": "USD"}]}
    
    batch = client.batch.create(payload);


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| body | `Batch`   |  - |





**Returns:** `boolean`





___


