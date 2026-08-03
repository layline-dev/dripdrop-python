# PublicContactDuplicatePreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**List[Contact]**](Contact.md) |  | 

## Example

```python
from dripdrop.models.public_contact_duplicate_preview_request import PublicContactDuplicatePreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublicContactDuplicatePreviewRequest from a JSON string
public_contact_duplicate_preview_request_instance = PublicContactDuplicatePreviewRequest.from_json(json)
# print the JSON string representation of the object
print(PublicContactDuplicatePreviewRequest.to_json())

# convert the object into a dict
public_contact_duplicate_preview_request_dict = public_contact_duplicate_preview_request_instance.to_dict()
# create an instance of PublicContactDuplicatePreviewRequest from a dict
public_contact_duplicate_preview_request_from_dict = PublicContactDuplicatePreviewRequest.from_dict(public_contact_duplicate_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


