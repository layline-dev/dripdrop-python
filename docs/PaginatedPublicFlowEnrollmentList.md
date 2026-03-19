# PaginatedPublicFlowEnrollmentList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PublicFlowEnrollment]**](PublicFlowEnrollment.md) |  | 

## Example

```python
from dripdrop.models.paginated_public_flow_enrollment_list import PaginatedPublicFlowEnrollmentList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPublicFlowEnrollmentList from a JSON string
paginated_public_flow_enrollment_list_instance = PaginatedPublicFlowEnrollmentList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPublicFlowEnrollmentList.to_json())

# convert the object into a dict
paginated_public_flow_enrollment_list_dict = paginated_public_flow_enrollment_list_instance.to_dict()
# create an instance of PaginatedPublicFlowEnrollmentList from a dict
paginated_public_flow_enrollment_list_from_dict = PaginatedPublicFlowEnrollmentList.from_dict(paginated_public_flow_enrollment_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


