# dripdrop.FlowsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flows_create_contact_and_enroll_create**](FlowsApi.md#flows_create_contact_and_enroll_create) | **POST** /v1/flows/{uuid}/create-contact-and-enroll/ | Create contact and enroll in flow
[**flows_list**](FlowsApi.md#flows_list) | **GET** /v1/flows/ | List flows
[**flows_retrieve**](FlowsApi.md#flows_retrieve) | **GET** /v1/flows/{uuid}/ | Get a flow


# **flows_create_contact_and_enroll_create**
> CreateContactAndEnrollSuccess flows_create_contact_and_enroll_create(uuid, create_contact_and_enroll)

Create contact and enroll in flow

Create a new contact and enroll them in this flow. Returns an error if a contact with the provided email or phone already exists.

### Example


```python
import dripdrop
from dripdrop.models.create_contact_and_enroll import CreateContactAndEnroll
from dripdrop.models.create_contact_and_enroll_success import CreateContactAndEnrollSuccess
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
    api_instance = dripdrop.FlowsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    create_contact_and_enroll = dripdrop.CreateContactAndEnroll() # CreateContactAndEnroll | 

    try:
        # Create contact and enroll in flow
        api_response = api_instance.flows_create_contact_and_enroll_create(uuid, create_contact_and_enroll)
        print("The response of FlowsApi->flows_create_contact_and_enroll_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_create_contact_and_enroll_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 
 **create_contact_and_enroll** | [**CreateContactAndEnroll**](CreateContactAndEnroll.md)|  | 

### Return type

[**CreateContactAndEnrollSuccess**](CreateContactAndEnrollSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Validation error |  -  |
**404** | Flow not found |  -  |
**429** | Contact limit for your plan has been reached |  -  |
**409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flows_list**
> PaginatedPublicFlowList flows_list(ordering=ordering, page=page, page_size=page_size)

List flows

Retrieve all flows for your account.

### Example


```python
import dripdrop
from dripdrop.models.paginated_public_flow_list import PaginatedPublicFlowList
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
    api_instance = dripdrop.FlowsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # List flows
        api_response = api_instance.flows_list(ordering=ordering, page=page, page_size=page_size)
        print("The response of FlowsApi->flows_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_list: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flows_retrieve**
> PublicFlow flows_retrieve(uuid)

Get a flow

Retrieve a single flow by UUID.

### Example


```python
import dripdrop
from dripdrop.models.public_flow import PublicFlow
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
    api_instance = dripdrop.FlowsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a flow
        api_response = api_instance.flows_retrieve(uuid)
        print("The response of FlowsApi->flows_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 

### Return type

[**PublicFlow**](PublicFlow.md)

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

