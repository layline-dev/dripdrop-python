# CustomFieldDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [readonly] 
**created** | **datetime** |  | [readonly] 
**modified** | **datetime** |  | [readonly] 
**display_name** | **str** | Human-readable label for the custom field | 
**key** | **str** | Machine-friendly identifier (e.g., &#39;company_name&#39;). Auto-generated from display name if omitted. | [optional] 
**field_type** | [**FieldTypeEnum**](FieldTypeEnum.md) |  | 
**target_model** | **str** | Target model in &#39;app_label.model&#39; format (e.g., &#39;contacts.contact&#39;) | 
**target_model_display** | **str** |  | [readonly] 
**required** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**options** | **object** | Configuration for the field (e.g., choices for &#39;choice&#39; type, max_length for &#39;char&#39;) | [optional] 
**sort_order** | **int** |  | [optional] 
**is_archived** | **bool** |  | [optional] 
**is_in_use** | **bool** |  | [readonly] 

## Example

```python
from dripdrop.models.custom_field_definition import CustomFieldDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldDefinition from a JSON string
custom_field_definition_instance = CustomFieldDefinition.from_json(json)
# print the JSON string representation of the object
print(CustomFieldDefinition.to_json())

# convert the object into a dict
custom_field_definition_dict = custom_field_definition_instance.to_dict()
# create an instance of CustomFieldDefinition from a dict
custom_field_definition_from_dict = CustomFieldDefinition.from_dict(custom_field_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


