[Payment Rails Python SDK](../README.md) > [recipient_gateway](../classes/recipientgateway.md)



# Class: RecipientGateway

## Index

### Methods

* [create](recipient_gateway.md#create)
* [find](recipient_gateway.md#find)
* [remove](recipient_gateway.md#remove)
* [search](recipient_gateway.md#search)
* [update](recipient_gateway.md#update)



---

## Methods
<a id="create"></a>

###  create

► **create**(body: *[Recipient](../types/recipient.md)*): `Recipient`



*Defined in [recipient_gateway.py:82](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/recipient_gateway.py#L82)*



Create a given recipient
     
    payload = {"type": "individual", "firstName": "John", "lastName": "Smith", "email": "test@example.com"}
    recipient = client.recipient.create(payload)


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| body | [Recipient](../types/recipient.md)   |  The recipient information to create |



**Returns:** `Recipient`



___

<a id="find"></a>

###  find

► **find**(recipientId: *`string`*): `Recipient`


*Defined in [recipient_gateway.py:58](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/recipient_gateway.py#L58)*



Find a specific recipient by their Payment Rails recipient ID

    recipient = client.recipient.find("R-fj57vn7emfiwdm8cjmd")


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| recipientId | `string`   |  The Payment Rails recipient ID (e.g. R-xyzzy) |



**Returns:** `Recipient`





___

<a id="delete"></a>

###  delete

► **delete**(recipientId: *`string`*): `boolean`
► **delete**(recipient: *`Recipient`*): `boolean`



*Defined in [recipient_gateway.py:115](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/recipient_gateway.py#L115)*



Delete the given recipient.

    status = client.recipient.delete('R-123');


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| recipientId | `string`   |  The Payment Rails recipient ID (e.g. R-xyzzy) |




**Returns:** `boolean`





___

<a id="search"></a>

###  search

► **search**(page: *`number`*, pageSize: *`number`*, term: *`string`*): `Recipient`[]



*Defined in [recipient_gateway.py:123](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/recipient_gateway.py#L123)*



**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| page | `number`   |  - |
| pageSize | `number`   |  - |
| term | `string`   |  - |





**Returns:** `Recipient`[]





___

<a id="update"></a>

###  update

► **update**(body: *[Recipient](../types/recipient.md)*): `boolean`



*Defined in [recipient_gateway.py:100](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/recipient_gateway.py#L100)*



Update the given recipient

    Recipient recipient = new Recipient(null, "individual", null, "tom.jones@example.com", null, "Tom", "Jones", null, null, null, "1990-04-29", null, null, null, null);
    recipient =  client.recipient.update(recipient);


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| body | [Recipient](../types/recipient.md)   |  the changes to make to the recipient |





**Returns:** `boolean`





___


