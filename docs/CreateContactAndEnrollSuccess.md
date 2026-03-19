# CreateContactAndEnrollSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**contact** | [**Contact**](Contact.md) |  | 
**enrollment** | [**PublicFlowEnrollment**](PublicFlowEnrollment.md) |  | 

## Example

```python
from dripdrop.models.create_contact_and_enroll_success import CreateContactAndEnrollSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactAndEnrollSuccess from a JSON string
create_contact_and_enroll_success_instance = CreateContactAndEnrollSuccess.from_json(json)
# print the JSON string representation of the object
print(CreateContactAndEnrollSuccess.to_json())

# convert the object into a dict
create_contact_and_enroll_success_dict = create_contact_and_enroll_success_instance.to_dict()
# create an instance of CreateContactAndEnrollSuccess from a dict
create_contact_and_enroll_success_from_dict = CreateContactAndEnrollSuccess.from_dict(create_contact_and_enroll_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


