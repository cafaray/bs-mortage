# swagger_client.DefaultApi

All URIs are relative to *http://cosafinity-prod.apigee.net/v1/employees*

Method | HTTP request | Description
------------- | ------------- | -------------
[**employee_uuid_delete**](DefaultApi.md#employee_uuid_delete) | **DELETE** /{employee-uuid} | Delete an Employee with given UUID
[**employee_uuid_get**](DefaultApi.md#employee_uuid_get) | **GET** /{employee-uuid} | Get an Employee with given UUID.
[**employee_uuid_put**](DefaultApi.md#employee_uuid_put) | **PUT** /{employee-uuid} | Update an Employee with given UUID
[**root_get**](DefaultApi.md#root_get) | **GET** / | Get all Employees
[**root_post**](DefaultApi.md#root_post) | **POST** / | Create a new Employee


# **employee_uuid_delete**
> Employee employee_uuid_delete(employee_uuid)

Delete an Employee with given UUID

This endpoint will delete an existing Employee.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
employee_uuid = 56 # int | UUID of a Employee

try:
    # Delete an Employee with given UUID
    api_response = api_instance.employee_uuid_delete(employee_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->employee_uuid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_uuid** | **int**| UUID of a Employee | 

### Return type

[**Employee**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employee_uuid_get**
> Employee employee_uuid_get(employee_uuid)

Get an Employee with given UUID.

This endpoint returns a Employee from a given UUID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
employee_uuid = 56 # int | UUID of a Employee

try:
    # Get an Employee with given UUID.
    api_response = api_instance.employee_uuid_get(employee_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->employee_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_uuid** | **int**| UUID of a Employee | 

### Return type

[**Employee**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employee_uuid_put**
> Employee employee_uuid_put(employee_uuid, body)

Update an Employee with given UUID

This endpoint will update an existing Employee.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
employee_uuid = 56 # int | UUID of a Employee
body = swagger_client.Employee() # Employee | an Employee oject

try:
    # Update an Employee with given UUID
    api_response = api_instance.employee_uuid_put(employee_uuid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->employee_uuid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_uuid** | **int**| UUID of a Employee | 
 **body** | [**Employee**](Employee.md)| an Employee oject | 

### Return type

[**Employee**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> EmployeesArray root_get()

Get all Employees

This endpoint returns a list of all Employees as an array.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get all Employees
    api_response = api_instance.root_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->root_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EmployeesArray**](EmployeesArray.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_post**
> Employee root_post(body)

Create a new Employee

This endpoint will create a new Employee.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Employee() # Employee | an Employee oject

try:
    # Create a new Employee
    api_response = api_instance.root_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->root_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Employee**](Employee.md)| an Employee oject | 

### Return type

[**Employee**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

