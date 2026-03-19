# PatchedCustomFieldDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [optional] [readonly] 
**created** | **datetime** |  | [optional] [readonly] 
**modified** | **datetime** |  | [optional] [readonly] 
**display_name** | **str** | Human-readable label for the custom field | [optional] 
**key** | **str** | Machine-friendly identifier (e.g., &#39;company_name&#39;). Auto-generated from display name if omitted. | [optional] 
**field_type** | [**FieldTypeEnum**](FieldTypeEnum.md) |  | [optional] 
**target_model** | **str** | Target model in &#39;app_label.model&#39; format (e.g., &#39;contacts.contact&#39;) | [optional] 
**target_model_display** | **str** |  | [optional] [readonly] 
**required** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**options** | **object** | Configuration for the field (e.g., choices for &#39;choice&#39; type, max_length for &#39;char&#39;) | [optional] 
**sort_order** | **int** |  | [optional] 
**is_archived** | **bool** |  | [optional] 
**is_in_use** | **bool** |  | [optional] [readonly] 

## Example

```python
from dripdrop.models.patched_custom_field_definition import PatchedCustomFieldDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedCustomFieldDefinition from a JSON string
patched_custom_field_definition_instance = PatchedCustomFieldDefinition.from_json(json)
# print the JSON string representation of the object
print(PatchedCustomFieldDefinition.to_json())

# convert the object into a dict
patched_custom_field_definition_dict = patched_custom_field_definition_instance.to_dict()
# create an instance of PatchedCustomFieldDefinition from a dict
patched_custom_field_definition_from_dict = PatchedCustomFieldDefinition.from_dict(patched_custom_field_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


