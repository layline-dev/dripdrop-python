# ContactAlreadyExists


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**contact** | [**Contact**](Contact.md) |  | 

## Example

```python
from dripdrop.models.contact_already_exists import ContactAlreadyExists

# TODO update the JSON string below
json = "{}"
# create an instance of ContactAlreadyExists from a JSON string
contact_already_exists_instance = ContactAlreadyExists.from_json(json)
# print the JSON string representation of the object
print(ContactAlreadyExists.to_json())

# convert the object into a dict
contact_already_exists_dict = contact_already_exists_instance.to_dict()
# create an instance of ContactAlreadyExists from a dict
contact_already_exists_from_dict = ContactAlreadyExists.from_dict(contact_already_exists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


