[Payment Rails Python SDK](../README.md) > [batch_gateway](../classes/batch_gateway.md)



# Class: batch_gateway


Gateway class for batches
*__class__*: batch_gateway


## Index

### Methods

* [create](batch_gateway.md#create)
* [find](batch_gateway.md#find)
* [generate_quote](batch_gateway.md#generate_quote)
* [delete](batch_gateway.md#delete)
* [search](batch_gateway.md#search)
* [process_batch](batch_gateway.md#process_batch)
* [summary](batch_gateway.md#summary)
* [update](batch_gateway.md#update)



---
## Methods
<a id="create"></a>

###  create

► **create**(batch: *`Batch`*): `Batch`



*Defined in [batch_gateway.py:27](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L27)*



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



*Defined in [batch_gateway.py:17](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L17)*



Retrieves a batch based on the batch id

    batch = client.batch.find('B-xx999bb');


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| batchId | `string`   |  Payment Rails batch id (e.g. "B-xx999bb") |





**Returns:** `Batch`





___

<a id="generate_quote"></a>

###  generate_quote

► **generate_quote**(batchId: *`string`*): `Batch`



*Defined in [batch_gateway.py:80](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L80)*



Generate a FX quote for this batch


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| batchId | `string`   |  Payment Rails payment id (e.g. "B-xx999bb") |





**Returns:** `Batch`


___

<a id="delete"></a>

###  delete

► **delete**(batchId: *`string`*): `Boolean`


*Defined in [batch_gateway.py:47](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L47)*



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



*Defined in [batch_gateway.py:54](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L54)*



Search for a batch matching the given term


**Parameters:**

| Param | Type | Default value | Description |
| ------ | ------ | ------ | ------ |
| page | `number`  | 1 |   - |
| pageSize | `number`  | 10 |   - |
| term | `string`  | &quot;&quot; |   string search term |





**Returns:** `Batch`[]





___

<a id="process_batch"></a>

###  process_batch

► **process_batch**(batchId: *`string`*): `Batch`



*Defined in [batch_gateway.py:90](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L90)*



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



*Defined in [batch_gateway.py:68](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L68)*



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



*Defined in [batch_gateway.py:37](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/batch_gateway.py#L37)*



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


