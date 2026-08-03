# PublicContactDuplicatePreviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolutions** | [**List[ImportResolution]**](ImportResolution.md) |  | 

## Example

```python
from dripdrop.models.public_contact_duplicate_preview_response import PublicContactDuplicatePreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicContactDuplicatePreviewResponse from a JSON string
public_contact_duplicate_preview_response_instance = PublicContactDuplicatePreviewResponse.from_json(json)
# print the JSON string representation of the object
print(PublicContactDuplicatePreviewResponse.to_json())

# convert the object into a dict
public_contact_duplicate_preview_response_dict = public_contact_duplicate_preview_response_instance.to_dict()
# create an instance of PublicContactDuplicatePreviewResponse from a dict
public_contact_duplicate_preview_response_from_dict = PublicContactDuplicatePreviewResponse.from_dict(public_contact_duplicate_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


