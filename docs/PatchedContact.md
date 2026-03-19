# PatchedContact

Serializer mixin that adds tag support to any model serializer.  The target model must have a ManyToManyField named `tags` pointing to tags.Tag.  Write request format: {\"tags\": [\"<tag-uuid>\", ...]} Read response format: {\"tags\": [{\"uuid\": \"...\", \"name\": \"...\", ...}, ...]}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [optional] [readonly] 
**created** | **datetime** |  | [optional] [readonly] 
**modified** | **datetime** |  | [optional] [readonly] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**primary_email** | [**EmailAddress**](EmailAddress.md) |  | [optional] 
**primary_phone** | [**PhoneNumber**](PhoneNumber.md) |  | [optional] 
**custom_fields** | **Dict[str, object]** |  | [optional] 
**tags** | **List[UUID]** |  | [optional] 

## Example

```python
from dripdrop.models.patched_contact import PatchedContact

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedContact from a JSON string
patched_contact_instance = PatchedContact.from_json(json)
# print the JSON string representation of the object
print(PatchedContact.to_json())

# convert the object into a dict
patched_contact_dict = patched_contact_instance.to_dict()
# create an instance of PatchedContact from a dict
patched_contact_from_dict = PatchedContact.from_dict(patched_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


