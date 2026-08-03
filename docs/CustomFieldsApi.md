# dripdrop.CustomFieldsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_fields_create**](CustomFieldsApi.md#custom_fields_create) | **POST** /v1/custom-fields/ | Create a custom field definition
[**custom_fields_destroy**](CustomFieldsApi.md#custom_fields_destroy) | **DELETE** /v1/custom-fields/{uuid}/ | Delete a custom field definition
[**custom_fields_list**](CustomFieldsApi.md#custom_fields_list) | **GET** /v1/custom-fields/ | List custom field definitions
[**custom_fields_partial_update**](CustomFieldsApi.md#custom_fields_partial_update) | **PATCH** /v1/custom-fields/{uuid}/ | Patch a custom field definition
[**custom_fields_retrieve**](CustomFieldsApi.md#custom_fields_retrieve) | **GET** /v1/custom-fields/{uuid}/ | Get a custom field definition
[**custom_fields_update**](CustomFieldsApi.md#custom_fields_update) | **PUT** /v1/custom-fields/{uuid}/ | Update a custom field definition


# **custom_fields_create**
> CustomFieldDefinition custom_fields_create(custom_field_definition)

Create a custom field definition

Create a new custom field definition for a supported model.

### Example


```python
import dripdrop
from dripdrop.models.custom_field_definition import CustomFieldDefinition
from dripdrop.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dripdrop.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dripdrop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dripdrop.CustomFieldsApi(api_client)
    custom_field_definition = dripdrop.CustomFieldDefinition() # CustomFieldDefinition | 

    try:
        # Create a custom field definition
        api_response = api_instance.custom_fields_create(custom_field_definition)
        print("The response of CustomFieldsApi->custom_fields_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->custom_fields_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_definition** | [**CustomFieldDefinition**](CustomFieldDefinition.md)|  | 

### Return type

[**CustomFieldDefinition**](CustomFieldDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_destroy**
> custom_fields_destroy(uuid)

Delete a custom field definition

Permanently delete a custom field definition.

### Example


```python
import dripdrop
from dripdrop.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dripdrop.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dripdrop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dripdrop.CustomFieldsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a custom field definition
        api_instance.custom_fields_destroy(uuid)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->custom_fields_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_list**
> PaginatedCustomFieldDefinitionList custom_fields_list(ordering=ordering, page=page, page_size=page_size, search=search)

List custom field definitions

Retrieve custom field definitions for your account. Optionally filter by target_model query parameter.

### Example


```python
import dripdrop
from dripdrop.models.paginated_custom_field_definition_list import PaginatedCustomFieldDefinitionList
from dripdrop.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dripdrop.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dripdrop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dripdrop.CustomFieldsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        # List custom field definitions
        api_response = api_instance.custom_fields_list(ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of CustomFieldsApi->custom_fields_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->custom_fields_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedCustomFieldDefinitionList**](PaginatedCustomFieldDefinitionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_partial_update**
> CustomFieldDefinition custom_fields_partial_update(uuid, patched_custom_field_definition=patched_custom_field_definition)

Patch a custom field definition

Update specific fields on an existing custom field definition.

### Example


```python
import dripdrop
from dripdrop.models.custom_field_definition import CustomFieldDefinition
from dripdrop.models.patched_custom_field_definition import PatchedCustomFieldDefinition
from dripdrop.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dripdrop.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dripdrop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dripdrop.CustomFieldsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    patched_custom_field_definition = dripdrop.PatchedCustomFieldDefinition() # PatchedCustomFieldDefinition |  (optional)

    try:
        # Patch a custom field definition
        api_response = api_instance.custom_fields_partial_update(uuid, patched_custom_field_definition=patched_custom_field_definition)
        print("The response of CustomFieldsApi->custom_fields_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->custom_fields_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 
 **patched_custom_field_definition** | [**PatchedCustomFieldDefinition**](PatchedCustomFieldDefinition.md)|  | [optional] 

### Return type

[**CustomFieldDefinition**](CustomFieldDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_retrieve**
> CustomFieldDefinition custom_fields_retrieve(uuid)

Get a custom field definition

Retrieve a single custom field definition by UUID.

### Example


```python
import dripdrop
from dripdrop.models.custom_field_definition import CustomFieldDefinition
from dripdrop.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dripdrop.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dripdrop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dripdrop.CustomFieldsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a custom field definition
        api_response = api_instance.custom_fields_retrieve(uuid)
        print("The response of CustomFieldsApi->custom_fields_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->custom_fields_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 

### Return type

[**CustomFieldDefinition**](CustomFieldDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_update**
> CustomFieldDefinition custom_fields_update(uuid, custom_field_definition)

Update a custom field definition

Replace all fields on an existing custom field definition.

### Example


```python
import dripdrop
from dripdrop.models.custom_field_definition import CustomFieldDefinition
from dripdrop.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dripdrop.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dripdrop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dripdrop.CustomFieldsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    custom_field_definition = dripdrop.CustomFieldDefinition() # CustomFieldDefinition | 

    try:
        # Update a custom field definition
        api_response = api_instance.custom_fields_update(uuid, custom_field_definition)
        print("The response of CustomFieldsApi->custom_fields_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->custom_fields_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 
 **custom_field_definition** | [**CustomFieldDefinition**](CustomFieldDefinition.md)|  | 

### Return type

[**CustomFieldDefinition**](CustomFieldDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

