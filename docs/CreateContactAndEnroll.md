# CreateContactAndEnroll


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**custom_fields** | **Dict[str, object]** |  | [optional] 
**enrollment_custom_fields** | **Dict[str, object]** | Custom field values for the enrollment this call creates, keyed by field UUID or key. The definitions must target flows.flowenrollment; &#x60;custom_fields&#x60; targets the contact. | [optional] 
**on_match** | [**OnMatchEnum**](OnMatchEnum.md) | Set to &#39;create&#39; to create a new contact even when one already matches the account&#39;s dedupe strategy. Omit to return 409 on a match (default).  * &#x60;create&#x60; - create | [optional] 

## Example

```python
from dripdrop.models.create_contact_and_enroll import CreateContactAndEnroll

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactAndEnroll from a JSON string
create_contact_and_enroll_instance = CreateContactAndEnroll.from_json(json)
# print the JSON string representation of the object
print(CreateContactAndEnroll.to_json())

# convert the object into a dict
create_contact_and_enroll_dict = create_contact_and_enroll_instance.to_dict()
# create an instance of CreateContactAndEnroll from a dict
create_contact_and_enroll_from_dict = CreateContactAndEnroll.from_dict(create_contact_and_enroll_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


