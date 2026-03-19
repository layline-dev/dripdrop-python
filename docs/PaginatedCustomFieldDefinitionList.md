# PaginatedCustomFieldDefinitionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[CustomFieldDefinition]**](CustomFieldDefinition.md) |  | 

## Example

```python
from dripdrop.models.paginated_custom_field_definition_list import PaginatedCustomFieldDefinitionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCustomFieldDefinitionList from a JSON string
paginated_custom_field_definition_list_instance = PaginatedCustomFieldDefinitionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCustomFieldDefinitionList.to_json())

# convert the object into a dict
paginated_custom_field_definition_list_dict = paginated_custom_field_definition_list_instance.to_dict()
# create an instance of PaginatedCustomFieldDefinitionList from a dict
paginated_custom_field_definition_list_from_dict = PaginatedCustomFieldDefinitionList.from_dict(paginated_custom_field_definition_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


