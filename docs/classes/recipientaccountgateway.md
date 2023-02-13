[Trolley Python SDK](../README.md) > [recipient_account_gateway](../classes/recipientaccountgateway.md)



# Class: recipient_account_gateway

## Index

### Methods

* [findAll](recipientaccountgateway.md#findAll)
* [create](recipientaccountgateway.md#create)
* [find](recipientaccountgateway.md#find)
* [remove](recipientaccountgateway.md#remove)
* [update](recipientaccountgateway.md#update)



---


## Methods
<a id="findAll"></a>

###  findAll

► **findAll**(recipientId: *`string`*): `List<RecipientAccount>`(recipientaccount.md)[]>



*Defined in [recipient_account_gateway.py:33](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/PaymentRails_recipient_account_gateway.py#L33)*



Fetch all of the accounts for a given Trolley recipient

    accounts = client.recipient_account.findAll('R-1234');

*__throws__*: {NotFound} if recipient doesn't exist



**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| recipientId | `string`   |  The Trolley recipient ID (e.g. R-xyzzy) |





**Returns:** `List<RecipientAccount>(recipientaccount.md)[]>





___

<a id="create"></a>

###  create

► **create**(recipientId: *`string`*, body: *`string`*): `RecipientAccount`(recipientaccount.md)>



*Defined in [recipient_account_gateway.py:79](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/PaymentRails_recipient_account_gateway.py#L79)*



Create a new recipient account

    payload = {"type": "bank-transfer", "primary": "true", "country": "CA", "currency": "CAD",
    "accountNum": "604622847", "bankId": "123", "branchId": "47261",  "accountHolderName": "John Smith"} 

    recipient_account = client.recipient_account.create("R-1234", payload);



**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| recipientId | `string`   |  The Trolley recipient ID (e.g. R-xyzzy) |
| body | `string`   |  Account information |





**Returns:** `RecipientAccount`(recipientaccount.md)>





___

<a id="find"></a>

###  find

► **find**(recipientId: *`string`*, accountId: *`string`*): `RecipientAccount`(recipientaccount.md)>



*Defined in [recipient_account_gateway.py:52](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/PaymentRails_recipient_account_gateway.py#L52)*



Fetch a specific account for a given Trolley recipient

    account = client.recipient_account.find('R-1234', 'A-789');
*__throws__*: {NotFound} if account or recipient don't exist



**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| recipientId | `string`   |  The Trolley recipient ID (e.g. R-xyzzy) |
| accountId | `string`   |  The Trolley account ID (e.g. A-xyzzy) |





**Returns:** `RecipientAccount`(recipientaccount.md)>





___

<a id="remove"></a>

###  remove

► **remove**(recipientId: *`string`*, accountId: *`string`*): `boolean`
► **remove**(recipientId: *`string`*, recipient_account: *`string`*): `boolean`


*Defined in [recipient_account_gateway.py:121](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/PaymentRails_recipient_account_gateway.py#L121)*



Delete the given recipient account. This will only return success, otherwise it will throw an exception (e.g. NotFound)

    success = client.recipient_account.remove('R-1234', 'A-789');


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| recipientId | `string`   |  The Trolley recipient ID (e.g. R-xyzzy) |
| accountId | `string`   |  The Trolley account ID (e.g. A-xyzzy) |





**Returns:** `boolean`





___

<a id="update"></a>

###  update

► **update**(recipientId: *`string`*, accountId: *`string`*, body: *`string`*): `RecipientAccount`(recipientaccount.md)>



*Defined in [recipient_account_gateway.py:102](https://github.com/PaymentRails/python-sdk/tree/master/paymentrails/PaymentRails_recipient_account_gateway.py#L102)*



Update a recipient account. Note: Updating an account will create a new account ID if it contains any property that isn't just "primary"

    payload = {"accountHolderName": "Tom Jones"}
    account = client.recipient_account.update('R-1234', payload);


**Parameters:**

| Param | Type | Description |
| ------ | ------ | ------ |
| recipientId | `string`   |  The Trolley recipient ID (e.g. R-xyzzy) |
| accountId | `string`   |  The Trolley account ID (e.g. A-xyzzy) |
| body | `any`   |  Account information |





**Returns:** `RecipientAccount`(recipientaccount.md)>





___


