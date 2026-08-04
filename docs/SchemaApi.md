# dripdrop.SchemaApi

All URIs are relative to *https://api.dripdrop.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve**](SchemaApi.md#retrieve) | **GET** /schema/ | 


# **retrieve**
> Dict[str, object] retrieve(format=format, lang=lang)

OpenApi3 schema for this API. Format can be selected via content negotiation.

- YAML: application/vnd.oai.openapi
- JSON: application/vnd.oai.openapi+json

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
    api_instance = dripdrop.SchemaApi(api_client)
    format = 'format_example' # str |  (optional)
    lang = 'lang_example' # str |  (optional)

    try:
        api_response = api_instance.retrieve(format=format, lang=lang)
        print("The response of SchemaApi->retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] 
 **lang** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.oai.openapi, application/yaml, application/vnd.oai.openapi+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

