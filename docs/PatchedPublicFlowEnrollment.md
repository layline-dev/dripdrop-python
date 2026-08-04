# PatchedPublicFlowEnrollment

Serializer mixin that adds custom field support to any model serializer.  The target model must have a `custom_data` JSONField.  Usage:     class ContactSerializer(CustomFieldSerializerMixin, BaseNestedModelSerializer):         class Meta:             model = Contact             fields = [..., \"custom_fields\"]  Read response format:     \"custom_fields\": {         \"<field_uuid>\": {             \"value\": <the_value>,             \"name\": \"Company\",             \"field_type\": \"char\",             \"required\": false         }     }  Write request format:     \"custom_fields\": {         \"<field_uuid>\": <value>     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [optional] [readonly] 
**created** | **datetime** |  | [optional] [readonly] 
**modified** | **datetime** |  | [optional] [readonly] 
**status** | [**FlowEnrollmentStatusesEnum**](FlowEnrollmentStatusesEnum.md) |  | [optional] [readonly] 
**flow_uuid** | **UUID** |  | [optional] 
**contact_uuid** | **UUID** |  | [optional] 
**custom_fields** | **Dict[str, object]** |  | [optional] 

## Example

```python
from dripdrop.models.patched_public_flow_enrollment import PatchedPublicFlowEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPublicFlowEnrollment from a JSON string
patched_public_flow_enrollment_instance = PatchedPublicFlowEnrollment.from_json(json)
# print the JSON string representation of the object
print(PatchedPublicFlowEnrollment.to_json())

# convert the object into a dict
patched_public_flow_enrollment_dict = patched_public_flow_enrollment_instance.to_dict()
# create an instance of PatchedPublicFlowEnrollment from a dict
patched_public_flow_enrollment_from_dict = PatchedPublicFlowEnrollment.from_dict(patched_public_flow_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


