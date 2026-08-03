# PublicContactBulkCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | [**List[Contact]**](Contact.md) |  | 
**skipped** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from dripdrop.models.public_contact_bulk_create_response import PublicContactBulkCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicContactBulkCreateResponse from a JSON string
public_contact_bulk_create_response_instance = PublicContactBulkCreateResponse.from_json(json)
# print the JSON string representation of the object
print(PublicContactBulkCreateResponse.to_json())

# convert the object into a dict
public_contact_bulk_create_response_dict = public_contact_bulk_create_response_instance.to_dict()
# create an instance of PublicContactBulkCreateResponse from a dict
public_contact_bulk_create_response_from_dict = PublicContactBulkCreateResponse.from_dict(public_contact_bulk_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


