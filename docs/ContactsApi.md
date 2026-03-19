# dripdrop.ContactsApi

All URIs are relative to *https://api.dripdrop.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ContactsApi.md#create) | **POST** /v1/contacts/ | Create a contact
[**destroy**](ContactsApi.md#destroy) | **DELETE** /v1/contacts/{uuid}/ | Delete a contact
[**list**](ContactsApi.md#list) | **GET** /v1/contacts/ | List contacts
[**partial_update**](ContactsApi.md#partial_update) | **PATCH** /v1/contacts/{uuid}/ | Patch a contact
[**retrieve**](ContactsApi.md#retrieve) | **GET** /v1/contacts/{uuid}/ | Get a contact
[**update**](ContactsApi.md#update) | **PUT** /v1/contacts/{uuid}/ | Update a contact


# **create**
> Contact create(contact)

Create a contact

Create a new contact with optional email and phone number.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dripdrop
from dripdrop.models.contact import Contact
from dripdrop.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dripdrop.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = dripdrop.Configuration(
    host = "https://api.dripdrop.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dripdrop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dripdrop.ContactsApi(api_client)
    contact = dripdrop.Contact() # Contact | 

    try:
        # Create a contact
        api_response = api_instance.create(contact)
        print("The response of ContactsApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact** | [**Contact**](Contact.md)|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> destroy(uuid)

Delete a contact

Permanently delete a contact.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dripdrop
from dripdrop.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dripdrop.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = dripdrop.Configuration(
    host = "https://api.dripdrop.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dripdrop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dripdrop.ContactsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a contact
        api_instance.destroy(uuid)
    except Exception as e:
        print("Exception when calling ContactsApi->destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedContactList list(ordering=ordering, page=page, page_size=page_size, search=search)

List contacts

Retrieve a paginated list of contacts for your account.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dripdrop
from dripdrop.models.paginated_contact_list import PaginatedContactList
from dripdrop.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dripdrop.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = dripdrop.Configuration(
    host = "https://api.dripdrop.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dripdrop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dripdrop.ContactsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        # List contacts
        api_response = api_instance.list(ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of ContactsApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedContactList**](PaginatedContactList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update**
> Contact partial_update(uuid, patched_contact=patched_contact)

Patch a contact

Update specific fields on an existing contact.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dripdrop
from dripdrop.models.contact import Contact
from dripdrop.models.patched_contact import PatchedContact
from dripdrop.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dripdrop.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = dripdrop.Configuration(
    host = "https://api.dripdrop.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dripdrop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dripdrop.ContactsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    patched_contact = dripdrop.PatchedContact() # PatchedContact |  (optional)

    try:
        # Patch a contact
        api_response = api_instance.partial_update(uuid, patched_contact=patched_contact)
        print("The response of ContactsApi->partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 
 **patched_contact** | [**PatchedContact**](PatchedContact.md)|  | [optional] 

### Return type

[**Contact**](Contact.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve**
> Contact retrieve(uuid)

Get a contact

Retrieve a single contact by UUID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dripdrop
from dripdrop.models.contact import Contact
from dripdrop.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dripdrop.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = dripdrop.Configuration(
    host = "https://api.dripdrop.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dripdrop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dripdrop.ContactsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a contact
        api_response = api_instance.retrieve(uuid)
        print("The response of ContactsApi->retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Contact update(uuid, contact)

Update a contact

Replace all fields on an existing contact.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dripdrop
from dripdrop.models.contact import Contact
from dripdrop.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dripdrop.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = dripdrop.Configuration(
    host = "https://api.dripdrop.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dripdrop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dripdrop.ContactsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    contact = dripdrop.Contact() # Contact | 

    try:
        # Update a contact
        api_response = api_instance.update(uuid, contact)
        print("The response of ContactsApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 
 **contact** | [**Contact**](Contact.md)|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

