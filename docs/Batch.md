# Batch

## About
The Batch class contains static utily methods for interfacing with the batch API. For more information see the [API documentation](http://docs.paymentrails.com/#payments)

## **Methods**
---
### **find**
Utility method to make GET requests to the batch API

Parameters | Return Type
--- | ---:
(batchId) | String


---
### **create**
Utility method to make POST requests to the batch API

Parameters | Return Type
--- | ---:
(body) | Batch
(body, batchId) | Batch

---
### **update**
Utility method to make PATCH requests to the batch API

Parameters | Return Type
--- | ---:
(batchId, body) | Boolean

---
### **delete**
Utility method to make DELETE requests to the batch API

Parameters | Return Type
--- | ---:
(batchId) | Boolean

---
### **search**
Utility method for querying batches

Parameters | Return Type
--- | ---:
(no-parameters) | List of Batches
(page) | List of Batches
(page, pageSize) | List of Batches
(page, pageSize, term) | List of Batches

---
### **generateQuote**
Utility method to generating a quote for a bacth

Parameters | Return Type
--- | ---:
(batchId) | Batch


---
### **processBatch**
Utility method to send a batch out for processing

Parameters | Return Type
--- | ---:
(batchId) | Batch


---
### **summary**
Utility method to get a batch summary

Parameters | Return Type
--- | ---:
(batchId) | BatchSummary
