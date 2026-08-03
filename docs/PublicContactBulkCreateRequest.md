# PublicContactBulkCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**List[Contact]**](Contact.md) |  | 
**on_duplicate** | [**OnDuplicateEnum**](OnDuplicateEnum.md) |  | [optional] 

## Example

```python
from dripdrop.models.public_contact_bulk_create_request import PublicContactBulkCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublicContactBulkCreateRequest from a JSON string
public_contact_bulk_create_request_instance = PublicContactBulkCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PublicContactBulkCreateRequest.to_json())

# convert the object into a dict
public_contact_bulk_create_request_dict = public_contact_bulk_create_request_instance.to_dict()
# create an instance of PublicContactBulkCreateRequest from a dict
public_contact_bulk_create_request_from_dict = PublicContactBulkCreateRequest.from_dict(public_contact_bulk_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


