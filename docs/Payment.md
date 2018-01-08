# Payment

## About
The Payment class contains static utily methods for interfacing with the payment API. For more information see the [API documentation](http://docs.paymentrails.com/#payments)

## **Methods**
---
### **find**
Utility method to make GET requests to the payment API

Parameters | Return Type
--- | ---:
(paymentId) | Payment


---
### **create**
Utility method to make POST requests to the payment API

Parameters | Return Type
--- | ---:
(body, batchId) | Payment

---
### **update**
Utility method to make PATCH requests to the payment API

Parameters | Return Type
--- | ---:
(paymentId, body) | Boolean

---
### **delete**
Utility method to make DELETE requests to the payment API

Parameters | Return Type
--- | ---:
(paymentId) | Boolean

---
### **search**
Utility method for querying payments

Parameters | Return Type
--- | ---:
(no-parameters) | List of Payments
(page) | List of Payments
(page, pageSize) | List of Payments
(page, pageSize, term) | List of Payments