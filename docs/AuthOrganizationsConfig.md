# AuthOrganizationsConfig

Auth related organizations configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | If true, support for IdP provided organizations is enabled. | [default to False]

## Example

```python
from flightctl.models.auth_organizations_config import AuthOrganizationsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AuthOrganizationsConfig from a JSON string
auth_organizations_config_instance = AuthOrganizationsConfig.from_json(json)
# print the JSON string representation of the object
print(AuthOrganizationsConfig.to_json())

# convert the object into a dict
auth_organizations_config_dict = auth_organizations_config_instance.to_dict()
# create an instance of AuthOrganizationsConfig from a dict
auth_organizations_config_from_dict = AuthOrganizationsConfig.from_dict(auth_organizations_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


