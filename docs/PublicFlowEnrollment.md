# PublicFlowEnrollment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [readonly] 
**created** | **datetime** |  | [readonly] 
**modified** | **datetime** |  | [readonly] 
**status** | [**FlowEnrollmentStatusesEnum**](FlowEnrollmentStatusesEnum.md) |  | [readonly] 
**flow_uuid** | **UUID** |  | 
**contact_uuid** | **UUID** |  | 

## Example

```python
from dripdrop.models.public_flow_enrollment import PublicFlowEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of PublicFlowEnrollment from a JSON string
public_flow_enrollment_instance = PublicFlowEnrollment.from_json(json)
# print the JSON string representation of the object
print(PublicFlowEnrollment.to_json())

# convert the object into a dict
public_flow_enrollment_dict = public_flow_enrollment_instance.to_dict()
# create an instance of PublicFlowEnrollment from a dict
public_flow_enrollment_from_dict = PublicFlowEnrollment.from_dict(public_flow_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


