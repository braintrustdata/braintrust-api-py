# ProjectResource

Types:

```python
from braintrust.types import Project, ProjectListResponse
```

Methods:

- <code title="post /v1/project">client.project.<a href="./src/braintrust/resources/project/project.py">create</a>(\*\*<a href="src/braintrust/types/project_create_params.py">params</a>) -> <a href="./src/braintrust/types/project.py">Project</a></code>
- <code title="get /v1/project/{project_id}">client.project.<a href="./src/braintrust/resources/project/project.py">retrieve</a>(project_id) -> <a href="./src/braintrust/types/project.py">Project</a></code>
- <code title="patch /v1/project/{project_id}">client.project.<a href="./src/braintrust/resources/project/project.py">update</a>(project_id, \*\*<a href="src/braintrust/types/project_update_params.py">params</a>) -> <a href="./src/braintrust/types/project.py">Project</a></code>
- <code title="get /v1/project">client.project.<a href="./src/braintrust/resources/project/project.py">list</a>(\*\*<a href="src/braintrust/types/project_list_params.py">params</a>) -> <a href="./src/braintrust/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /v1/project/{project_id}">client.project.<a href="./src/braintrust/resources/project/project.py">delete</a>(project_id) -> <a href="./src/braintrust/types/project.py">Project</a></code>
- <code title="put /v1/project">client.project.<a href="./src/braintrust/resources/project/project.py">replace</a>(\*\*<a href="src/braintrust/types/project_replace_params.py">params</a>) -> <a href="./src/braintrust/types/project.py">Project</a></code>

# Logs

Types:

```python
from braintrust.types import LogFetchResponse, LogFetchPostResponse, LogInsertResponse
```

Methods:

- <code title="post /v1/project_logs/{project_id}/feedback">client.logs.<a href="./src/braintrust/resources/logs.py">feedback</a>(project_id, \*\*<a href="src/braintrust/types/log_feedback_params.py">params</a>) -> None</code>
- <code title="get /v1/project_logs/{project_id}/fetch">client.logs.<a href="./src/braintrust/resources/logs.py">fetch</a>(project_id, \*\*<a href="src/braintrust/types/log_fetch_params.py">params</a>) -> <a href="./src/braintrust/types/log_fetch_response.py">LogFetchResponse</a></code>
- <code title="post /v1/project_logs/{project_id}/fetch">client.logs.<a href="./src/braintrust/resources/logs.py">fetch_post</a>(project_id, \*\*<a href="src/braintrust/types/log_fetch_post_params.py">params</a>) -> <a href="./src/braintrust/types/log_fetch_post_response.py">LogFetchPostResponse</a></code>
- <code title="post /v1/project_logs/{project_id}/insert">client.logs.<a href="./src/braintrust/resources/logs.py">insert</a>(project_id, \*\*<a href="src/braintrust/types/log_insert_params.py">params</a>) -> <a href="./src/braintrust/types/log_insert_response.py">LogInsertResponse</a></code>

# ExperimentResource

Types:

```python
from braintrust.types import (
    Experiment,
    ExperimentListResponse,
    ExperimentFetchResponse,
    ExperimentFetchPostResponse,
    ExperimentInsertResponse,
)
```

Methods:

- <code title="post /v1/experiment">client.experiment.<a href="./src/braintrust/resources/experiment.py">create</a>(\*\*<a href="src/braintrust/types/experiment_create_params.py">params</a>) -> <a href="./src/braintrust/types/experiment.py">Experiment</a></code>
- <code title="get /v1/experiment/{experiment_id}">client.experiment.<a href="./src/braintrust/resources/experiment.py">retrieve</a>(experiment_id) -> <a href="./src/braintrust/types/experiment.py">Experiment</a></code>
- <code title="patch /v1/experiment/{experiment_id}">client.experiment.<a href="./src/braintrust/resources/experiment.py">update</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_update_params.py">params</a>) -> <a href="./src/braintrust/types/experiment.py">Experiment</a></code>
- <code title="get /v1/experiment">client.experiment.<a href="./src/braintrust/resources/experiment.py">list</a>(\*\*<a href="src/braintrust/types/experiment_list_params.py">params</a>) -> <a href="./src/braintrust/types/experiment_list_response.py">ExperimentListResponse</a></code>
- <code title="delete /v1/experiment/{experiment_id}">client.experiment.<a href="./src/braintrust/resources/experiment.py">delete</a>(experiment_id) -> <a href="./src/braintrust/types/experiment.py">Experiment</a></code>
- <code title="post /v1/experiment/{experiment_id}/feedback">client.experiment.<a href="./src/braintrust/resources/experiment.py">feedback</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_feedback_params.py">params</a>) -> None</code>
- <code title="get /v1/experiment/{experiment_id}/fetch">client.experiment.<a href="./src/braintrust/resources/experiment.py">fetch</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_fetch_params.py">params</a>) -> <a href="./src/braintrust/types/experiment_fetch_response.py">ExperimentFetchResponse</a></code>
- <code title="post /v1/experiment/{experiment_id}/fetch">client.experiment.<a href="./src/braintrust/resources/experiment.py">fetch_post</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_fetch_post_params.py">params</a>) -> <a href="./src/braintrust/types/experiment_fetch_post_response.py">ExperimentFetchPostResponse</a></code>
- <code title="post /v1/experiment/{experiment_id}/insert">client.experiment.<a href="./src/braintrust/resources/experiment.py">insert</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_insert_params.py">params</a>) -> <a href="./src/braintrust/types/experiment_insert_response.py">ExperimentInsertResponse</a></code>
- <code title="put /v1/experiment">client.experiment.<a href="./src/braintrust/resources/experiment.py">replace</a>(\*\*<a href="src/braintrust/types/experiment_replace_params.py">params</a>) -> <a href="./src/braintrust/types/experiment.py">Experiment</a></code>

# DatasetResource

Types:

```python
from braintrust.types import (
    Dataset,
    DatasetListResponse,
    DatasetFetchResponse,
    DatasetFetchPostResponse,
    DatasetInsertResponse,
)
```

Methods:

- <code title="post /v1/dataset">client.dataset.<a href="./src/braintrust/resources/dataset.py">create</a>(\*\*<a href="src/braintrust/types/dataset_create_params.py">params</a>) -> <a href="./src/braintrust/types/dataset.py">Dataset</a></code>
- <code title="get /v1/dataset/{dataset_id}">client.dataset.<a href="./src/braintrust/resources/dataset.py">retrieve</a>(dataset_id) -> <a href="./src/braintrust/types/dataset.py">Dataset</a></code>
- <code title="patch /v1/dataset/{dataset_id}">client.dataset.<a href="./src/braintrust/resources/dataset.py">update</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_update_params.py">params</a>) -> <a href="./src/braintrust/types/dataset.py">Dataset</a></code>
- <code title="get /v1/dataset">client.dataset.<a href="./src/braintrust/resources/dataset.py">list</a>(\*\*<a href="src/braintrust/types/dataset_list_params.py">params</a>) -> <a href="./src/braintrust/types/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="delete /v1/dataset/{dataset_id}">client.dataset.<a href="./src/braintrust/resources/dataset.py">delete</a>(dataset_id) -> <a href="./src/braintrust/types/dataset.py">Dataset</a></code>
- <code title="post /v1/dataset/{dataset_id}/feedback">client.dataset.<a href="./src/braintrust/resources/dataset.py">feedback</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_feedback_params.py">params</a>) -> None</code>
- <code title="get /v1/dataset/{dataset_id}/fetch">client.dataset.<a href="./src/braintrust/resources/dataset.py">fetch</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_fetch_params.py">params</a>) -> <a href="./src/braintrust/types/dataset_fetch_response.py">DatasetFetchResponse</a></code>
- <code title="post /v1/dataset/{dataset_id}/fetch">client.dataset.<a href="./src/braintrust/resources/dataset.py">fetch_post</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_fetch_post_params.py">params</a>) -> <a href="./src/braintrust/types/dataset_fetch_post_response.py">DatasetFetchPostResponse</a></code>
- <code title="post /v1/dataset/{dataset_id}/insert">client.dataset.<a href="./src/braintrust/resources/dataset.py">insert</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_insert_params.py">params</a>) -> <a href="./src/braintrust/types/dataset_insert_response.py">DatasetInsertResponse</a></code>
- <code title="put /v1/dataset">client.dataset.<a href="./src/braintrust/resources/dataset.py">replace</a>(\*\*<a href="src/braintrust/types/dataset_replace_params.py">params</a>) -> <a href="./src/braintrust/types/dataset.py">Dataset</a></code>

# TopLevel

Types:

```python
from braintrust.types import TopLevelHelloWorldResponse
```

Methods:

- <code title="get /v1">client.top_level.<a href="./src/braintrust/resources/top_level.py">hello_world</a>() -> str</code>
