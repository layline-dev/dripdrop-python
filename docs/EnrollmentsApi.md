# dripdrop.EnrollmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrollments_create**](EnrollmentsApi.md#enrollments_create) | **POST** /v1/enrollments/ | Enroll a contact
[**enrollments_destroy**](EnrollmentsApi.md#enrollments_destroy) | **DELETE** /v1/enrollments/{uuid}/ | Unenroll a contact
[**enrollments_list**](EnrollmentsApi.md#enrollments_list) | **GET** /v1/enrollments/ | List enrollments


# **enrollments_create**
> PublicFlowEnrollment enrollments_create(public_flow_enrollment)

Enroll a contact

Enroll a contact into a flow by providing flow_uuid and contact_uuid.

### Example


```python
import dripdrop
from dripdrop.models.public_flow_enrollment import PublicFlowEnrollment
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
    api_instance = dripdrop.EnrollmentsApi(api_client)
    public_flow_enrollment = dripdrop.PublicFlowEnrollment() # PublicFlowEnrollment | 

    try:
        # Enroll a contact
        api_response = api_instance.enrollments_create(public_flow_enrollment)
        print("The response of EnrollmentsApi->enrollments_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->enrollments_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_flow_enrollment** | [**PublicFlowEnrollment**](PublicFlowEnrollment.md)|  | 

### Return type

[**PublicFlowEnrollment**](PublicFlowEnrollment.md)

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

# **enrollments_destroy**
> enrollments_destroy(uuid)

Unenroll a contact

Remove a contact from a flow by enrollment UUID.

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
    api_instance = dripdrop.EnrollmentsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Unenroll a contact
        api_instance.enrollments_destroy(uuid)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->enrollments_destroy: %s\n" % e)
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

# **enrollments_list**
> PaginatedPublicFlowEnrollmentList enrollments_list(ordering=ordering, page=page, page_size=page_size)

List enrollments

Retrieve all flow enrollments for your account.

### Example


```python
import dripdrop
from dripdrop.models.paginated_public_flow_enrollment_list import PaginatedPublicFlowEnrollmentList
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
    api_instance = dripdrop.EnrollmentsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # List enrollments
        api_response = api_instance.enrollments_list(ordering=ordering, page=page, page_size=page_size)
        print("The response of EnrollmentsApi->enrollments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->enrollments_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedPublicFlowEnrollmentList**](PaginatedPublicFlowEnrollmentList.md)

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

