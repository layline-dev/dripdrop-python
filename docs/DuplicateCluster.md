# DuplicateCluster

Serializes a dedup.DuplicateCluster (key + the contacts sharing it) for the duplicate report and the setting-change guard's blocked payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_type** | **str** |  | 
**key_value** | **str** |  | 
**contacts** | [**List[DuplicateClusterContact]**](DuplicateClusterContact.md) |  | [readonly] 

## Example

```python
from dripdrop.models.duplicate_cluster import DuplicateCluster

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateCluster from a JSON string
duplicate_cluster_instance = DuplicateCluster.from_json(json)
# print the JSON string representation of the object
print(DuplicateCluster.to_json())

# convert the object into a dict
duplicate_cluster_dict = duplicate_cluster_instance.to_dict()
# create an instance of DuplicateCluster from a dict
duplicate_cluster_from_dict = DuplicateCluster.from_dict(duplicate_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


