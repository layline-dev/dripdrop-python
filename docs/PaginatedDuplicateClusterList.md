# PaginatedDuplicateClusterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DuplicateCluster]**](DuplicateCluster.md) |  | 

## Example

```python
from dripdrop.models.paginated_duplicate_cluster_list import PaginatedDuplicateClusterList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDuplicateClusterList from a JSON string
paginated_duplicate_cluster_list_instance = PaginatedDuplicateClusterList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDuplicateClusterList.to_json())

# convert the object into a dict
paginated_duplicate_cluster_list_dict = paginated_duplicate_cluster_list_instance.to_dict()
# create an instance of PaginatedDuplicateClusterList from a dict
paginated_duplicate_cluster_list_from_dict = PaginatedDuplicateClusterList.from_dict(paginated_duplicate_cluster_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


