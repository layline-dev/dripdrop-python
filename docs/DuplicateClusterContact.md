# DuplicateClusterContact

One contact inside a duplicate cluster (report + guard payload).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 

## Example

```python
from dripdrop.models.duplicate_cluster_contact import DuplicateClusterContact

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateClusterContact from a JSON string
duplicate_cluster_contact_instance = DuplicateClusterContact.from_json(json)
# print the JSON string representation of the object
print(DuplicateClusterContact.to_json())

# convert the object into a dict
duplicate_cluster_contact_dict = duplicate_cluster_contact_instance.to_dict()
# create an instance of DuplicateClusterContact from a dict
duplicate_cluster_contact_from_dict = DuplicateClusterContact.from_dict(duplicate_cluster_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


