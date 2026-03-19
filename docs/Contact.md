# Contact

Serializer mixin that adds tag support to any model serializer.  The target model must have a ManyToManyField named `tags` pointing to tags.Tag.  Write request format: {\"tags\": [\"<tag-uuid>\", ...]} Read response format: {\"tags\": [{\"uuid\": \"...\", \"name\": \"...\", ...}, ...]}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [readonly] 
**created** | **datetime** |  | [readonly] 
**modified** | **datetime** |  | [readonly] 
**first_name** | **str** |  | 
**last_name** | **str** |  | [optional] 
**primary_email** | [**EmailAddress**](EmailAddress.md) |  | [optional] 
**primary_phone** | [**PhoneNumber**](PhoneNumber.md) |  | [optional] 
**custom_fields** | **Dict[str, object]** |  | [optional] 
**tags** | **List[UUID]** |  | [optional] 

## Example

```python
from dripdrop.models.contact import Contact

# TODO update the JSON string below
json = "{}"
# create an instance of Contact from a JSON string
contact_instance = Contact.from_json(json)
# print the JSON string representation of the object
print(Contact.to_json())

# convert the object into a dict
contact_dict = contact_instance.to_dict()
# create an instance of Contact from a dict
contact_from_dict = Contact.from_dict(contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


