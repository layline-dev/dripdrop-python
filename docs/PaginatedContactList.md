# PaginatedContactList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Contact]**](Contact.md) |  | 

## Example

```python
from dripdrop.models.paginated_contact_list import PaginatedContactList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedContactList from a JSON string
paginated_contact_list_instance = PaginatedContactList.from_json(json)
# print the JSON string representation of the object
print(PaginatedContactList.to_json())

# convert the object into a dict
paginated_contact_list_dict = paginated_contact_list_instance.to_dict()
# create an instance of PaginatedContactList from a dict
paginated_contact_list_from_dict = PaginatedContactList.from_dict(paginated_contact_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


