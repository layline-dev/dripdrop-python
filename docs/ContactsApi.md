# dripdrop.ContactsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contacts_bulk_create**](ContactsApi.md#contacts_bulk_create) | **POST** /v1/contacts/bulk/ | Bulk create contacts
[**contacts_create**](ContactsApi.md#contacts_create) | **POST** /v1/contacts/ | Create a contact
[**contacts_destroy**](ContactsApi.md#contacts_destroy) | **DELETE** /v1/contacts/{uuid}/ | Delete a contact
[**contacts_duplicates_create**](ContactsApi.md#contacts_duplicates_create) | **POST** /v1/contacts/duplicates/ | Preview duplicates for incoming contacts
[**contacts_duplicates_list**](ContactsApi.md#contacts_duplicates_list) | **GET** /v1/contacts/duplicates/ | List duplicate contact clusters
[**contacts_list**](ContactsApi.md#contacts_list) | **GET** /v1/contacts/ | List contacts
[**contacts_partial_update**](ContactsApi.md#contacts_partial_update) | **PATCH** /v1/contacts/{uuid}/ | Patch a contact
[**contacts_retrieve**](ContactsApi.md#contacts_retrieve) | **GET** /v1/contacts/{uuid}/ | Get a contact
[**contacts_update**](ContactsApi.md#contacts_update) | **PUT** /v1/contacts/{uuid}/ | Update a contact


# **contacts_bulk_create**
> PublicContactBulkCreateResponse contacts_bulk_create(public_contact_bulk_create_request)

Bulk create contacts

Create up to 500 contacts in one request. Validation is all-or-nothing: if any contact fails validation, nothing is created and the errors identify each failing contact by its index.

Duplicate handling follows your account's dedupe strategy and the `on_duplicate` flag:
- `error` (default): if any row matches an existing contact or an earlier row in the same request, nothing is created and a 409 lists the conflicting rows.
- `skip`: the non-duplicate rows are created and the duplicates are reported in `skipped`.

Only rows that will actually be created are counted against your plan's contact quota.

### Example


```python
import dripdrop
from dripdrop.models.public_contact_bulk_create_request import PublicContactBulkCreateRequest
from dripdrop.models.public_contact_bulk_create_response import PublicContactBulkCreateResponse
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
    api_instance = dripdrop.ContactsApi(api_client)
    public_contact_bulk_create_request = dripdrop.PublicContactBulkCreateRequest() # PublicContactBulkCreateRequest | 

    try:
        # Bulk create contacts
        api_response = api_instance.contacts_bulk_create(public_contact_bulk_create_request)
        print("The response of ContactsApi->contacts_bulk_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_bulk_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_contact_bulk_create_request** | [**PublicContactBulkCreateRequest**](PublicContactBulkCreateRequest.md)|  | 

### Return type

[**PublicContactBulkCreateResponse**](PublicContactBulkCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_create**
> Contact contacts_create(contact)

Create a contact

Create a new contact with optional email and phone number.

### Example


```python
import dripdrop
from dripdrop.models.contact import Contact
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
    api_instance = dripdrop.ContactsApi(api_client)
    contact = dripdrop.Contact() # Contact | 

    try:
        # Create a contact
        api_response = api_instance.contacts_create(contact)
        print("The response of ContactsApi->contacts_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact** | [**Contact**](Contact.md)|  | 

### Return type

[**Contact**](Contact.md)

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

# **contacts_destroy**
> contacts_destroy(uuid)

Delete a contact

Permanently delete a contact.

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
    api_instance = dripdrop.ContactsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a contact
        api_instance.contacts_destroy(uuid)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_destroy: %s\n" % e)
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

# **contacts_duplicates_create**
> PublicContactDuplicatePreviewResponse contacts_duplicates_create(public_contact_duplicate_preview_request)

Preview duplicates for incoming contacts

Dry run: given a list of contacts, report per-row whether each would be created or skipped as a duplicate under your account's dedupe strategy — against both existing contacts and the other rows in the request. Nothing is created.

### Example


```python
import dripdrop
from dripdrop.models.public_contact_duplicate_preview_request import PublicContactDuplicatePreviewRequest
from dripdrop.models.public_contact_duplicate_preview_response import PublicContactDuplicatePreviewResponse
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
    api_instance = dripdrop.ContactsApi(api_client)
    public_contact_duplicate_preview_request = dripdrop.PublicContactDuplicatePreviewRequest() # PublicContactDuplicatePreviewRequest | 

    try:
        # Preview duplicates for incoming contacts
        api_response = api_instance.contacts_duplicates_create(public_contact_duplicate_preview_request)
        print("The response of ContactsApi->contacts_duplicates_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_duplicates_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_contact_duplicate_preview_request** | [**PublicContactDuplicatePreviewRequest**](PublicContactDuplicatePreviewRequest.md)|  | 

### Return type

[**PublicContactDuplicatePreviewResponse**](PublicContactDuplicatePreviewResponse.md)

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

# **contacts_duplicates_list**
> PaginatedDuplicateClusterList contacts_duplicates_list(ordering=ordering, page=page, page_size=page_size, search=search)

List duplicate contact clusters

Report of contacts that already share a dedupe key (email / phone), grouped into clusters, scanned by your account's dedupe strategy. When the strategy is `none` it falls back to email+phone so the report is still useful for cleanup.

### Example


```python
import dripdrop
from dripdrop.models.paginated_duplicate_cluster_list import PaginatedDuplicateClusterList
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
    api_instance = dripdrop.ContactsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        # List duplicate contact clusters
        api_response = api_instance.contacts_duplicates_list(ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of ContactsApi->contacts_duplicates_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_duplicates_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedDuplicateClusterList**](PaginatedDuplicateClusterList.md)

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

# **contacts_list**
> PaginatedContactList contacts_list(ordering=ordering, page=page, page_size=page_size, search=search)

List contacts

Retrieve a paginated list of contacts for your account.

### Example


```python
import dripdrop
from dripdrop.models.paginated_contact_list import PaginatedContactList
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
    api_instance = dripdrop.ContactsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        # List contacts
        api_response = api_instance.contacts_list(ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of ContactsApi->contacts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_list: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_partial_update**
> Contact contacts_partial_update(uuid, patched_contact=patched_contact)

Patch a contact

Update specific fields on an existing contact.

### Example


```python
import dripdrop
from dripdrop.models.contact import Contact
from dripdrop.models.patched_contact import PatchedContact
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
    api_instance = dripdrop.ContactsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    patched_contact = dripdrop.PatchedContact() # PatchedContact |  (optional)

    try:
        # Patch a contact
        api_response = api_instance.contacts_partial_update(uuid, patched_contact=patched_contact)
        print("The response of ContactsApi->contacts_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 
 **patched_contact** | [**PatchedContact**](PatchedContact.md)|  | [optional] 

### Return type

[**Contact**](Contact.md)

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

# **contacts_retrieve**
> Contact contacts_retrieve(uuid)

Get a contact

Retrieve a single contact by UUID.

### Example


```python
import dripdrop
from dripdrop.models.contact import Contact
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
    api_instance = dripdrop.ContactsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a contact
        api_response = api_instance.contacts_retrieve(uuid)
        print("The response of ContactsApi->contacts_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 

### Return type

[**Contact**](Contact.md)

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

# **contacts_update**
> Contact contacts_update(uuid, contact)

Update a contact

Replace all fields on an existing contact.

### Example


```python
import dripdrop
from dripdrop.models.contact import Contact
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
    api_instance = dripdrop.ContactsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    contact = dripdrop.Contact() # Contact | 

    try:
        # Update a contact
        api_response = api_instance.contacts_update(uuid, contact)
        print("The response of ContactsApi->contacts_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 
 **contact** | [**Contact**](Contact.md)|  | 

### Return type

[**Contact**](Contact.md)

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

