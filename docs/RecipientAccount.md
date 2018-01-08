# Recipient Account

## About
The Recipient class contains static utily methods for interfacing with the recipient API. For more information see the [API documentation](http://docs.paymentrails.com/#recipients)

## **Methods**
---
### **find**
Utility method to make GET requests to the recipient API

Parameters | Return Type
---| ---:
(recipient_id, recipient_account_id) | RecipientAccount


---
### **post**
Utility method to make POST requests to the recipient API

Parameters | Return Type
--- | ---:
(recipient_id, body) | RecipientAccount

---
### **update**
Utility method to make PATCH requests to the recipient API

Parameters | Return Type
--- | ---:
(recipient_id, recipient_account_id, body) | Boolean

---
### **delete**
Utility method to make DELETE requests to the recipient API

Parameters | Return Type
--- | ---:
(recipient_id, recipient_account_id) | Boolean

