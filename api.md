# ProjectResource

Types:

```python
from braintrust_sdk_kotlin.types import Project, ProjectListResponse
```

Methods:

- <code title="post /v1/project">client.project.<a href="./src/braintrust_sdk_kotlin/resources/project/project.py">create</a>(\*\*<a href="src/braintrust_sdk_kotlin/types/project_create_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/project.py">Project</a></code>
- <code title="get /v1/project/{project_id}">client.project.<a href="./src/braintrust_sdk_kotlin/resources/project/project.py">retrieve</a>(project_id) -> <a href="./src/braintrust_sdk_kotlin/types/project.py">Project</a></code>
- <code title="patch /v1/project/{project_id}">client.project.<a href="./src/braintrust_sdk_kotlin/resources/project/project.py">update</a>(project_id, \*\*<a href="src/braintrust_sdk_kotlin/types/project_update_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/project.py">Project</a></code>
- <code title="get /v1/project">client.project.<a href="./src/braintrust_sdk_kotlin/resources/project/project.py">list</a>(\*\*<a href="src/braintrust_sdk_kotlin/types/project_list_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /v1/project/{project_id}">client.project.<a href="./src/braintrust_sdk_kotlin/resources/project/project.py">delete</a>(project_id) -> <a href="./src/braintrust_sdk_kotlin/types/project.py">Project</a></code>
- <code title="put /v1/project">client.project.<a href="./src/braintrust_sdk_kotlin/resources/project/project.py">create_or_replace</a>(\*\*<a href="src/braintrust_sdk_kotlin/types/project_create_or_replace_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/project.py">Project</a></code>

# ProjectLogs

Types:

```python
from braintrust_sdk_kotlin.types import (
    ProjectLogFetchResponse,
    ProjectLogInsertResponse,
    ProjectLogInsertFetchResponse,
)
```

Methods:

- <code title="get /v1/project_logs/{project_id}/fetch">client.project_logs.<a href="./src/braintrust_sdk_kotlin/resources/project_logs.py">fetch</a>(project_id, \*\*<a href="src/braintrust_sdk_kotlin/types/project_log_fetch_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/project_log_fetch_response.py">ProjectLogFetchResponse</a></code>
- <code title="post /v1/project_logs/{project_id}/insert">client.project_logs.<a href="./src/braintrust_sdk_kotlin/resources/project_logs.py">insert</a>(project_id, \*\*<a href="src/braintrust_sdk_kotlin/types/project_log_insert_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/project_log_insert_response.py">ProjectLogInsertResponse</a></code>
- <code title="post /v1/project_logs/{project_id}/fetch">client.project_logs.<a href="./src/braintrust_sdk_kotlin/resources/project_logs.py">insert_fetch</a>(project_id, \*\*<a href="src/braintrust_sdk_kotlin/types/project_log_insert_fetch_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/project_log_insert_fetch_response.py">ProjectLogInsertFetchResponse</a></code>
- <code title="post /v1/project_logs/{project_id}/feedback">client.project_logs.<a href="./src/braintrust_sdk_kotlin/resources/project_logs.py">log_feedback</a>(project_id, \*\*<a href="src/braintrust_sdk_kotlin/types/project_log_log_feedback_params.py">params</a>) -> None</code>

# ExperimentResource

Types:

```python
from braintrust_sdk_kotlin.types import (
    Experiment,
    ExperimentFetchEventsResponse,
    ExperimentInsertResponse,
)
```

Methods:

- <code title="post /v1/experiment">client.experiment.<a href="./src/braintrust_sdk_kotlin/resources/experiment.py">create</a>(\*\*<a href="src/braintrust_sdk_kotlin/types/experiment_create_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/experiment.py">Experiment</a></code>
- <code title="get /v1/experiment/{experiment_id}">client.experiment.<a href="./src/braintrust_sdk_kotlin/resources/experiment.py">retrieve</a>(experiment_id) -> <a href="./src/braintrust_sdk_kotlin/types/experiment.py">Experiment</a></code>
- <code title="put /v1/experiment">client.experiment.<a href="./src/braintrust_sdk_kotlin/resources/experiment.py">update</a>(\*\*<a href="src/braintrust_sdk_kotlin/types/experiment_update_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/experiment.py">Experiment</a></code>
- <code title="delete /v1/experiment/{experiment_id}">client.experiment.<a href="./src/braintrust_sdk_kotlin/resources/experiment.py">delete</a>(experiment_id) -> <a href="./src/braintrust_sdk_kotlin/types/experiment.py">Experiment</a></code>
- <code title="post /v1/experiment/{experiment_id}/feedback">client.experiment.<a href="./src/braintrust_sdk_kotlin/resources/experiment.py">feedback</a>(experiment_id, \*\*<a href="src/braintrust_sdk_kotlin/types/experiment_feedback_params.py">params</a>) -> None</code>
- <code title="get /v1/experiment/{experiment_id}/fetch">client.experiment.<a href="./src/braintrust_sdk_kotlin/resources/experiment.py">fetch_events</a>(experiment_id, \*\*<a href="src/braintrust_sdk_kotlin/types/experiment_fetch_events_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/experiment_fetch_events_response.py">ExperimentFetchEventsResponse</a></code>
- <code title="post /v1/experiment/{experiment_id}/insert">client.experiment.<a href="./src/braintrust_sdk_kotlin/resources/experiment.py">insert</a>(experiment_id, \*\*<a href="src/braintrust_sdk_kotlin/types/experiment_insert_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/experiment_insert_response.py">ExperimentInsertResponse</a></code>
- <code title="patch /v1/experiment/{experiment_id}">client.experiment.<a href="./src/braintrust_sdk_kotlin/resources/experiment.py">update_partial</a>(experiment_id, \*\*<a href="src/braintrust_sdk_kotlin/types/experiment_update_partial_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/experiment.py">Experiment</a></code>

# Experiments

Types:

```python
from braintrust_sdk_kotlin.types import ExperimentListResponse
```

Methods:

- <code title="get /v1/experiment">client.experiments.<a href="./src/braintrust_sdk_kotlin/resources/experiments.py">list</a>(\*\*<a href="src/braintrust_sdk_kotlin/types/experiment_list_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/experiment_list_response.py">ExperimentListResponse</a></code>

# Datasets

Types:

```python
from braintrust_sdk_kotlin.types import (
    Dataset,
    DatasetListResponse,
    DatasetFetchResponse,
    DatasetInsertResponse,
)
```

Methods:

- <code title="put /v1/dataset">client.datasets.<a href="./src/braintrust_sdk_kotlin/resources/datasets.py">create</a>(\*\*<a href="src/braintrust_sdk_kotlin/types/dataset_create_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/dataset.py">Dataset</a></code>
- <code title="get /v1/dataset/{dataset_id}">client.datasets.<a href="./src/braintrust_sdk_kotlin/resources/datasets.py">retrieve</a>(dataset_id) -> <a href="./src/braintrust_sdk_kotlin/types/dataset.py">Dataset</a></code>
- <code title="patch /v1/dataset/{dataset_id}">client.datasets.<a href="./src/braintrust_sdk_kotlin/resources/datasets.py">update</a>(dataset_id, \*\*<a href="src/braintrust_sdk_kotlin/types/dataset_update_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/dataset.py">Dataset</a></code>
- <code title="get /v1/dataset">client.datasets.<a href="./src/braintrust_sdk_kotlin/resources/datasets.py">list</a>(\*\*<a href="src/braintrust_sdk_kotlin/types/dataset_list_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="post /v1/dataset/{dataset_id}/feedback">client.datasets.<a href="./src/braintrust_sdk_kotlin/resources/datasets.py">feedback</a>(dataset_id, \*\*<a href="src/braintrust_sdk_kotlin/types/dataset_feedback_params.py">params</a>) -> None</code>
- <code title="get /v1/dataset/{dataset_id}/fetch">client.datasets.<a href="./src/braintrust_sdk_kotlin/resources/datasets.py">fetch</a>(dataset_id, \*\*<a href="src/braintrust_sdk_kotlin/types/dataset_fetch_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/dataset_fetch_response.py">DatasetFetchResponse</a></code>
- <code title="post /v1/dataset/{dataset_id}/insert">client.datasets.<a href="./src/braintrust_sdk_kotlin/resources/datasets.py">insert</a>(dataset_id, \*\*<a href="src/braintrust_sdk_kotlin/types/dataset_insert_params.py">params</a>) -> <a href="./src/braintrust_sdk_kotlin/types/dataset_insert_response.py">DatasetInsertResponse</a></code>

# TopLevel

Methods:

- <code title="delete /v1/dataset/{dataset_id}">client.top_level.<a href="./src/braintrust_sdk_kotlin/resources/top_level.py">datasets</a>(dataset_id) -> <a href="./src/braintrust_sdk_kotlin/types/dataset.py">Dataset</a></code>

# V1

Types:

```python
from braintrust_sdk_kotlin.types import V1HelloWorldResponse
```

Methods:

- <code title="get /v1">client.v1.<a href="./src/braintrust_sdk_kotlin/resources/v1.py">hello_world</a>() -> str</code>
