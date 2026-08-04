# PublicContactBulkCreateConflict


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**conflicts** | **List[Dict[str, object]]** |  | 

## Example

```python
from dripdrop.models.public_contact_bulk_create_conflict import PublicContactBulkCreateConflict

# TODO update the JSON string below
json = "{}"
# create an instance of PublicContactBulkCreateConflict from a JSON string
public_contact_bulk_create_conflict_instance = PublicContactBulkCreateConflict.from_json(json)
# print the JSON string representation of the object
print(PublicContactBulkCreateConflict.to_json())

# convert the object into a dict
public_contact_bulk_create_conflict_dict = public_contact_bulk_create_conflict_instance.to_dict()
# create an instance of PublicContactBulkCreateConflict from a dict
public_contact_bulk_create_conflict_from_dict = PublicContactBulkCreateConflict.from_dict(public_contact_bulk_create_conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


