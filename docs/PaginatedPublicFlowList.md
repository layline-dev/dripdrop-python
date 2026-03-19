# PaginatedPublicFlowList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PublicFlow]**](PublicFlow.md) |  | 

## Example

```python
from dripdrop.models.paginated_public_flow_list import PaginatedPublicFlowList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPublicFlowList from a JSON string
paginated_public_flow_list_instance = PaginatedPublicFlowList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPublicFlowList.to_json())

# convert the object into a dict
paginated_public_flow_list_dict = paginated_public_flow_list_instance.to_dict()
# create an instance of PaginatedPublicFlowList from a dict
paginated_public_flow_list_from_dict = PaginatedPublicFlowList.from_dict(paginated_public_flow_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


