# flightctl.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_config**](AuthenticationApi.md#auth_config) | **GET** /api/v1/auth/config | 
[**auth_validate**](AuthenticationApi.md#auth_validate) | **GET** /api/v1/auth/validate | 


# **auth_config**
> AuthConfig auth_config()



Get authentication configuration.

### Example


```python
import flightctl
from flightctl.models.auth_config import AuthConfig
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.AuthenticationApi(api_client)

    try:
        api_response = api_instance.auth_config()
        print("The response of AuthenticationApi->auth_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthConfig**](AuthConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**418** | Auth not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_validate**
> Status auth_validate(authorization=authorization)



Validate an authentication token.

### Example


```python
import flightctl
from flightctl.models.status import Status
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.AuthenticationApi(api_client)
    authorization = 'authorization_example' # str | The authentication token to validate. (optional)

    try:
        api_response = api_instance.auth_validate(authorization=authorization)
        print("The response of AuthenticationApi->auth_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| The authentication token to validate. | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token valid |  -  |
**400** | Bad Request |  -  |
**401** | Token invalid |  -  |
**418** | Auth not configured |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

