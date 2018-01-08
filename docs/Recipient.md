# Recipient

## About
The Recipient class contains static utily methods for interfacing with the recipient API. For more information see the [API documentation](http://docs.paymentrails.com/#recipients)

## **Methods**
---
### **find**
Utility method to make GET requests to the recipient API

Parameters | Return Type
---| ---:
(recipientId) | Recipient
(recipientId, term) | Recipient


---
### **post**
Utility method to make POST requests to the recipient API

Parameters | Return Type
--- | ---:
(body) | Recipient

---
### **update**
Utility method to make PATCH requests to the recipient API

Parameters | Return Type
--- | ---:
(recipientId, body) | Boolean

---
### **delete**
Utility method to make DELETE requests to the recipient API

Parameters | Return Type
--- | ---:
(recipientId) | Boolean

---
### **search**
Utility method for querying recipients

Parameters | Return Type
--- | ---:
(no-parameters) | List of Recipients
(page) | List of Recipients
(page, pageSize) | List of Recipients
(page, pageSize, term) | List of Recipients