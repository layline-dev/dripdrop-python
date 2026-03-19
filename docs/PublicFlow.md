# PublicFlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [readonly] 
**created** | **datetime** |  | [readonly] 
**modified** | **datetime** |  | [readonly] 
**name** | **str** |  | [readonly] 
**status** | [**FlowStatusEnum**](FlowStatusEnum.md) |  | [readonly] 

## Example

```python
from dripdrop.models.public_flow import PublicFlow

# TODO update the JSON string below
json = "{}"
# create an instance of PublicFlow from a JSON string
public_flow_instance = PublicFlow.from_json(json)
# print the JSON string representation of the object
print(PublicFlow.to_json())

# convert the object into a dict
public_flow_dict = public_flow_instance.to_dict()
# create an instance of PublicFlow from a dict
public_flow_from_dict = PublicFlow.from_dict(public_flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


