# ImportResolution

Per-row dedupe outcome in the import dry-run preview (aligned by row).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome** | [**OutcomeEnum**](OutcomeEnum.md) |  | 
**matched_by** | **str** |  | 
**matched_contact_uuid** | **UUID** |  | 
**is_ambiguous** | **bool** |  | 
**notes** | **List[str]** |  | 

## Example

```python
from dripdrop.models.import_resolution import ImportResolution

# TODO update the JSON string below
json = "{}"
# create an instance of ImportResolution from a JSON string
import_resolution_instance = ImportResolution.from_json(json)
# print the JSON string representation of the object
print(ImportResolution.to_json())

# convert the object into a dict
import_resolution_dict = import_resolution_instance.to_dict()
# create an instance of ImportResolution from a dict
import_resolution_from_dict = ImportResolution.from_dict(import_resolution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


