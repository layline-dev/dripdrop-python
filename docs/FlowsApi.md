# dripdrop.FlowsApi

All URIs are relative to *https://api.dripdrop.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact_and_enroll_create**](FlowsApi.md#create_contact_and_enroll_create) | **POST** /v1/flows/{uuid}/create-contact-and-enroll/ | Create contact and enroll in flow
[**list**](FlowsApi.md#list) | **GET** /v1/flows/ | List flows
[**retrieve**](FlowsApi.md#retrieve) | **GET** /v1/flows/{uuid}/ | Get a flow


# **create_contact_and_enroll_create**
> CreateContactAndEnrollSuccess create_contact_and_enroll_create(uuid, create_contact_and_enroll)

Create contact and enroll in flow

Create a new contact and enroll them in this flow. Returns an error if a contact with the provided email or phone already exists.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dripdrop
from dripdrop.models.create_contact_and_enroll import CreateContactAndEnroll
from dripdrop.models.create_contact_and_enroll_success import CreateContactAndEnrollSuccess
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
    api_instance = dripdrop.FlowsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    create_contact_and_enroll = dripdrop.CreateContactAndEnroll() # CreateContactAndEnroll | 

    try:
        # Create contact and enroll in flow
        api_response = api_instance.create_contact_and_enroll_create(uuid, create_contact_and_enroll)
        print("The response of FlowsApi->create_contact_and_enroll_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->create_contact_and_enroll_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 
 **create_contact_and_enroll** | [**CreateContactAndEnroll**](CreateContactAndEnroll.md)|  | 

### Return type

[**CreateContactAndEnrollSuccess**](CreateContactAndEnrollSuccess.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Validation error |  -  |
**404** | Flow not found |  -  |
**409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedPublicFlowList list(ordering=ordering, page=page, page_size=page_size)

List flows

Retrieve all flows for your account.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dripdrop
from dripdrop.models.paginated_public_flow_list import PaginatedPublicFlowList
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
    api_instance = dripdrop.FlowsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # List flows
        api_response = api_instance.list(ordering=ordering, page=page, page_size=page_size)
        print("The response of FlowsApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedPublicFlowList**](PaginatedPublicFlowList.md)

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

# **retrieve**
> PublicFlow retrieve(uuid)

Get a flow

Retrieve a single flow by UUID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dripdrop
from dripdrop.models.public_flow import PublicFlow
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
    api_instance = dripdrop.FlowsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a flow
        api_response = api_instance.retrieve(uuid)
        print("The response of FlowsApi->retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 

### Return type

[**PublicFlow**](PublicFlow.md)

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

