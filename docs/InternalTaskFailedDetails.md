# InternalTaskFailedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**task_type** | **str** | The type of internal task that failed. | 
**error_message** | **str** | The error message describing the failure. | 
**retry_count** | **int** | Number of times the task has been retried. | [optional] 
**task_parameters** | **Dict[str, str]** | Parameters needed to retry the task. | [optional] 

## Example

```python
from flightctl.models.internal_task_failed_details import InternalTaskFailedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTaskFailedDetails from a JSON string
internal_task_failed_details_instance = InternalTaskFailedDetails.from_json(json)
# print the JSON string representation of the object
print(InternalTaskFailedDetails.to_json())

# convert the object into a dict
internal_task_failed_details_dict = internal_task_failed_details_instance.to_dict()
# create an instance of InternalTaskFailedDetails from a dict
internal_task_failed_details_from_dict = InternalTaskFailedDetails.from_dict(internal_task_failed_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


