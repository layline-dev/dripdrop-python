# dripdrop.EnrollmentsApi

All URIs are relative to *https://api.dripdrop.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](EnrollmentsApi.md#create) | **POST** /v1/enrollments/ | Enroll a contact
[**destroy**](EnrollmentsApi.md#destroy) | **DELETE** /v1/enrollments/{uuid}/ | Unenroll a contact
[**list**](EnrollmentsApi.md#list) | **GET** /v1/enrollments/ | List enrollments
[**partial_update**](EnrollmentsApi.md#partial_update) | **PATCH** /v1/enrollments/{uuid}/ | Patch an enrollment
[**update**](EnrollmentsApi.md#update) | **PUT** /v1/enrollments/{uuid}/ | Update an enrollment


# **create**
> PublicFlowEnrollment create(public_flow_enrollment)

Enroll a contact

Enroll a contact into a flow by providing flow_uuid and contact_uuid.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dripdrop
from dripdrop.models.public_flow_enrollment import PublicFlowEnrollment
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
    api_instance = dripdrop.EnrollmentsApi(api_client)
    public_flow_enrollment = dripdrop.PublicFlowEnrollment() # PublicFlowEnrollment | 

    try:
        # Enroll a contact
        api_response = api_instance.create(public_flow_enrollment)
        print("The response of EnrollmentsApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_flow_enrollment** | [**PublicFlowEnrollment**](PublicFlowEnrollment.md)|  | 

### Return type

[**PublicFlowEnrollment**](PublicFlowEnrollment.md)

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

Unenroll a contact

Remove a contact from a flow by enrollment UUID.

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
    api_instance = dripdrop.EnrollmentsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Unenroll a contact
        api_instance.destroy(uuid)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->destroy: %s\n" % e)
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
> PaginatedPublicFlowEnrollmentList list(contact_uuid=contact_uuid, flow_uuid=flow_uuid, ordering=ordering, page=page, page_size=page_size)

List enrollments

Retrieve all flow enrollments for your account. Optionally filter by flow and/or contact to look up an existing enrollment.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dripdrop
from dripdrop.models.paginated_public_flow_enrollment_list import PaginatedPublicFlowEnrollmentList
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
    api_instance = dripdrop.EnrollmentsApi(api_client)
    contact_uuid = 'contact_uuid_example' # str | Only return enrollments for this contact. (optional)
    flow_uuid = 'flow_uuid_example' # str | Only return enrollments in this flow. (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # List enrollments
        api_response = api_instance.list(contact_uuid=contact_uuid, flow_uuid=flow_uuid, ordering=ordering, page=page, page_size=page_size)
        print("The response of EnrollmentsApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_uuid** | **str**| Only return enrollments for this contact. | [optional] 
 **flow_uuid** | **str**| Only return enrollments in this flow. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedPublicFlowEnrollmentList**](PaginatedPublicFlowEnrollmentList.md)

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
> PublicFlowEnrollment partial_update(uuid, patched_public_flow_enrollment=patched_public_flow_enrollment)

Patch an enrollment

Update specific custom fields on an enrollment. Values are merged into the existing custom field data.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dripdrop
from dripdrop.models.patched_public_flow_enrollment import PatchedPublicFlowEnrollment
from dripdrop.models.public_flow_enrollment import PublicFlowEnrollment
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
    api_instance = dripdrop.EnrollmentsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    patched_public_flow_enrollment = dripdrop.PatchedPublicFlowEnrollment() # PatchedPublicFlowEnrollment |  (optional)

    try:
        # Patch an enrollment
        api_response = api_instance.partial_update(uuid, patched_public_flow_enrollment=patched_public_flow_enrollment)
        print("The response of EnrollmentsApi->partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 
 **patched_public_flow_enrollment** | [**PatchedPublicFlowEnrollment**](PatchedPublicFlowEnrollment.md)|  | [optional] 

### Return type

[**PublicFlowEnrollment**](PublicFlowEnrollment.md)

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

# **update**
> PublicFlowEnrollment update(uuid, public_flow_enrollment)

Update an enrollment

Update an enrollment's custom fields. The flow and contact an enrollment belongs to cannot be changed.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dripdrop
from dripdrop.models.public_flow_enrollment import PublicFlowEnrollment
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
    api_instance = dripdrop.EnrollmentsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    public_flow_enrollment = dripdrop.PublicFlowEnrollment() # PublicFlowEnrollment | 

    try:
        # Update an enrollment
        api_response = api_instance.update(uuid, public_flow_enrollment)
        print("The response of EnrollmentsApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 
 **public_flow_enrollment** | [**PublicFlowEnrollment**](PublicFlowEnrollment.md)|  | 

### Return type

[**PublicFlowEnrollment**](PublicFlowEnrollment.md)

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

