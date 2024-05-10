# TopLevel

Types:

```python
from braintrust.types import TopLevelHelloWorldResponse
```

Methods:

- <code title="get /v1">client.top_level.<a href="./src/braintrust/resources/top_level.py">hello_world</a>() -> str</code>

# Project

Types:

```python
from braintrust.types import Project
```

Methods:

- <code title="post /v1/project">client.project.<a href="./src/braintrust/resources/project/project.py">create</a>(\*\*<a href="src/braintrust/types/project_create_params.py">params</a>) -> <a href="./src/braintrust/types/project/project.py">Project</a></code>
- <code title="get /v1/project/{project_id}">client.project.<a href="./src/braintrust/resources/project/project.py">retrieve</a>(project_id) -> <a href="./src/braintrust/types/project/project.py">Project</a></code>
- <code title="patch /v1/project/{project_id}">client.project.<a href="./src/braintrust/resources/project/project.py">update</a>(project_id, \*\*<a href="src/braintrust/types/project_update_params.py">params</a>) -> <a href="./src/braintrust/types/project/project.py">Project</a></code>
- <code title="get /v1/project">client.project.<a href="./src/braintrust/resources/project/project.py">list</a>(\*\*<a href="src/braintrust/types/project_list_params.py">params</a>) -> <a href="./src/braintrust/types/project/project.py">SyncListObjects[Project]</a></code>
- <code title="delete /v1/project/{project_id}">client.project.<a href="./src/braintrust/resources/project/project.py">delete</a>(project_id) -> <a href="./src/braintrust/types/project/project.py">Project</a></code>
- <code title="put /v1/project">client.project.<a href="./src/braintrust/resources/project/project.py">replace</a>(\*\*<a href="src/braintrust/types/project_replace_params.py">params</a>) -> <a href="./src/braintrust/types/project/project.py">Project</a></code>

## Logs

Types:

```python
from braintrust.types.project import LogFetchResponse, LogFetchPostResponse, LogInsertResponse
```

Methods:

- <code title="post /v1/project_logs/{project_id}/feedback">client.project.logs.<a href="./src/braintrust/resources/project/logs.py">feedback</a>(project_id, \*\*<a href="src/braintrust/types/project/log_feedback_params.py">params</a>) -> None</code>
- <code title="get /v1/project_logs/{project_id}/fetch">client.project.logs.<a href="./src/braintrust/resources/project/logs.py">fetch</a>(project_id, \*\*<a href="src/braintrust/types/project/log_fetch_params.py">params</a>) -> <a href="./src/braintrust/types/project/log_fetch_response.py">LogFetchResponse</a></code>
- <code title="post /v1/project_logs/{project_id}/fetch">client.project.logs.<a href="./src/braintrust/resources/project/logs.py">fetch_post</a>(project_id, \*\*<a href="src/braintrust/types/project/log_fetch_post_params.py">params</a>) -> <a href="./src/braintrust/types/project/log_fetch_post_response.py">LogFetchPostResponse</a></code>
- <code title="post /v1/project_logs/{project_id}/insert">client.project.logs.<a href="./src/braintrust/resources/project/logs.py">insert</a>(project_id, \*\*<a href="src/braintrust/types/project/log_insert_params.py">params</a>) -> <a href="./src/braintrust/types/project/log_insert_response.py">LogInsertResponse</a></code>

# Experiment

Types:

```python
from braintrust.types import Experiment, ExperimentFetchResponse, ExperimentFetchPostResponse, ExperimentInsertResponse, ExperimentSummarizeResponse
```

Methods:

- <code title="post /v1/experiment">client.experiment.<a href="./src/braintrust/resources/experiment.py">create</a>(\*\*<a href="src/braintrust/types/experiment_create_params.py">params</a>) -> <a href="./src/braintrust/types/experiment.py">Experiment</a></code>
- <code title="get /v1/experiment/{experiment_id}">client.experiment.<a href="./src/braintrust/resources/experiment.py">retrieve</a>(experiment_id) -> <a href="./src/braintrust/types/experiment.py">Experiment</a></code>
- <code title="patch /v1/experiment/{experiment_id}">client.experiment.<a href="./src/braintrust/resources/experiment.py">update</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_update_params.py">params</a>) -> <a href="./src/braintrust/types/experiment.py">Experiment</a></code>
- <code title="get /v1/experiment">client.experiment.<a href="./src/braintrust/resources/experiment.py">list</a>(\*\*<a href="src/braintrust/types/experiment_list_params.py">params</a>) -> <a href="./src/braintrust/types/experiment.py">SyncListObjects[Experiment]</a></code>
- <code title="delete /v1/experiment/{experiment_id}">client.experiment.<a href="./src/braintrust/resources/experiment.py">delete</a>(experiment_id) -> <a href="./src/braintrust/types/experiment.py">Experiment</a></code>
- <code title="post /v1/experiment/{experiment_id}/feedback">client.experiment.<a href="./src/braintrust/resources/experiment.py">feedback</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_feedback_params.py">params</a>) -> None</code>
- <code title="get /v1/experiment/{experiment_id}/fetch">client.experiment.<a href="./src/braintrust/resources/experiment.py">fetch</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_fetch_params.py">params</a>) -> <a href="./src/braintrust/types/experiment_fetch_response.py">ExperimentFetchResponse</a></code>
- <code title="post /v1/experiment/{experiment_id}/fetch">client.experiment.<a href="./src/braintrust/resources/experiment.py">fetch_post</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_fetch_post_params.py">params</a>) -> <a href="./src/braintrust/types/experiment_fetch_post_response.py">ExperimentFetchPostResponse</a></code>
- <code title="post /v1/experiment/{experiment_id}/insert">client.experiment.<a href="./src/braintrust/resources/experiment.py">insert</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_insert_params.py">params</a>) -> <a href="./src/braintrust/types/experiment_insert_response.py">ExperimentInsertResponse</a></code>
- <code title="put /v1/experiment">client.experiment.<a href="./src/braintrust/resources/experiment.py">replace</a>(\*\*<a href="src/braintrust/types/experiment_replace_params.py">params</a>) -> <a href="./src/braintrust/types/experiment.py">Experiment</a></code>
- <code title="get /v1/experiment/{experiment_id}/summarize">client.experiment.<a href="./src/braintrust/resources/experiment.py">summarize</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_summarize_params.py">params</a>) -> <a href="./src/braintrust/types/experiment_summarize_response.py">ExperimentSummarizeResponse</a></code>

# Dataset

Types:

```python
from braintrust.types import Dataset, DatasetFetchResponse, DatasetFetchPostResponse, DatasetInsertResponse, DatasetSummarizeResponse
```

Methods:

- <code title="post /v1/dataset">client.dataset.<a href="./src/braintrust/resources/dataset.py">create</a>(\*\*<a href="src/braintrust/types/dataset_create_params.py">params</a>) -> <a href="./src/braintrust/types/dataset.py">Dataset</a></code>
- <code title="get /v1/dataset/{dataset_id}">client.dataset.<a href="./src/braintrust/resources/dataset.py">retrieve</a>(dataset_id) -> <a href="./src/braintrust/types/dataset.py">Dataset</a></code>
- <code title="patch /v1/dataset/{dataset_id}">client.dataset.<a href="./src/braintrust/resources/dataset.py">update</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_update_params.py">params</a>) -> <a href="./src/braintrust/types/dataset.py">Dataset</a></code>
- <code title="get /v1/dataset">client.dataset.<a href="./src/braintrust/resources/dataset.py">list</a>(\*\*<a href="src/braintrust/types/dataset_list_params.py">params</a>) -> <a href="./src/braintrust/types/dataset.py">SyncListObjects[Dataset]</a></code>
- <code title="delete /v1/dataset/{dataset_id}">client.dataset.<a href="./src/braintrust/resources/dataset.py">delete</a>(dataset_id) -> <a href="./src/braintrust/types/dataset.py">Dataset</a></code>
- <code title="post /v1/dataset/{dataset_id}/feedback">client.dataset.<a href="./src/braintrust/resources/dataset.py">feedback</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_feedback_params.py">params</a>) -> None</code>
- <code title="get /v1/dataset/{dataset_id}/fetch">client.dataset.<a href="./src/braintrust/resources/dataset.py">fetch</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_fetch_params.py">params</a>) -> <a href="./src/braintrust/types/dataset_fetch_response.py">DatasetFetchResponse</a></code>
- <code title="post /v1/dataset/{dataset_id}/fetch">client.dataset.<a href="./src/braintrust/resources/dataset.py">fetch_post</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_fetch_post_params.py">params</a>) -> <a href="./src/braintrust/types/dataset_fetch_post_response.py">DatasetFetchPostResponse</a></code>
- <code title="post /v1/dataset/{dataset_id}/insert">client.dataset.<a href="./src/braintrust/resources/dataset.py">insert</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_insert_params.py">params</a>) -> <a href="./src/braintrust/types/dataset_insert_response.py">DatasetInsertResponse</a></code>
- <code title="put /v1/dataset">client.dataset.<a href="./src/braintrust/resources/dataset.py">replace</a>(\*\*<a href="src/braintrust/types/dataset_replace_params.py">params</a>) -> <a href="./src/braintrust/types/dataset.py">Dataset</a></code>
- <code title="get /v1/dataset/{dataset_id}/summarize">client.dataset.<a href="./src/braintrust/resources/dataset.py">summarize</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_summarize_params.py">params</a>) -> <a href="./src/braintrust/types/dataset_summarize_response.py">DatasetSummarizeResponse</a></code>

# Prompt

Types:

```python
from braintrust.types import Prompt
```

Methods:

- <code title="post /v1/prompt">client.prompt.<a href="./src/braintrust/resources/prompt.py">create</a>(\*\*<a href="src/braintrust/types/prompt_create_params.py">params</a>) -> <a href="./src/braintrust/types/prompt.py">Prompt</a></code>
- <code title="get /v1/prompt/{prompt_id}">client.prompt.<a href="./src/braintrust/resources/prompt.py">retrieve</a>(prompt_id) -> <a href="./src/braintrust/types/prompt.py">Prompt</a></code>
- <code title="patch /v1/prompt/{prompt_id}">client.prompt.<a href="./src/braintrust/resources/prompt.py">update</a>(prompt_id, \*\*<a href="src/braintrust/types/prompt_update_params.py">params</a>) -> <a href="./src/braintrust/types/prompt.py">Prompt</a></code>
- <code title="get /v1/prompt">client.prompt.<a href="./src/braintrust/resources/prompt.py">list</a>(\*\*<a href="src/braintrust/types/prompt_list_params.py">params</a>) -> <a href="./src/braintrust/types/prompt.py">SyncListObjects[Prompt]</a></code>
- <code title="delete /v1/prompt/{prompt_id}">client.prompt.<a href="./src/braintrust/resources/prompt.py">delete</a>(prompt_id) -> <a href="./src/braintrust/types/prompt.py">Prompt</a></code>
- <code title="post /v1/prompt/{prompt_id}/feedback">client.prompt.<a href="./src/braintrust/resources/prompt.py">feedback</a>(prompt_id, \*\*<a href="src/braintrust/types/prompt_feedback_params.py">params</a>) -> None</code>
- <code title="put /v1/prompt">client.prompt.<a href="./src/braintrust/resources/prompt.py">replace</a>(\*\*<a href="src/braintrust/types/prompt_replace_params.py">params</a>) -> <a href="./src/braintrust/types/prompt.py">Prompt</a></code>

# Role

Types:

```python
from braintrust.types import Role
```

Methods:

- <code title="post /v1/role">client.role.<a href="./src/braintrust/resources/role.py">create</a>(\*\*<a href="src/braintrust/types/role_create_params.py">params</a>) -> <a href="./src/braintrust/types/role.py">Role</a></code>
- <code title="get /v1/role/{role_id}">client.role.<a href="./src/braintrust/resources/role.py">retrieve</a>(role_id) -> <a href="./src/braintrust/types/role.py">Role</a></code>
- <code title="patch /v1/role/{role_id}">client.role.<a href="./src/braintrust/resources/role.py">update</a>(role_id, \*\*<a href="src/braintrust/types/role_update_params.py">params</a>) -> <a href="./src/braintrust/types/role.py">Role</a></code>
- <code title="get /v1/role">client.role.<a href="./src/braintrust/resources/role.py">list</a>(\*\*<a href="src/braintrust/types/role_list_params.py">params</a>) -> <a href="./src/braintrust/types/role.py">SyncListObjects[Role]</a></code>
- <code title="delete /v1/role/{role_id}">client.role.<a href="./src/braintrust/resources/role.py">delete</a>(role_id) -> <a href="./src/braintrust/types/role.py">Role</a></code>
- <code title="put /v1/role">client.role.<a href="./src/braintrust/resources/role.py">replace</a>(\*\*<a href="src/braintrust/types/role_replace_params.py">params</a>) -> <a href="./src/braintrust/types/role.py">Role</a></code>

# Group

Types:

```python
from braintrust.types import Group
```

Methods:

- <code title="post /v1/group">client.group.<a href="./src/braintrust/resources/group.py">create</a>(\*\*<a href="src/braintrust/types/group_create_params.py">params</a>) -> <a href="./src/braintrust/types/group.py">Group</a></code>
- <code title="get /v1/group/{group_id}">client.group.<a href="./src/braintrust/resources/group.py">retrieve</a>(group_id) -> <a href="./src/braintrust/types/group.py">Group</a></code>
- <code title="patch /v1/group/{group_id}">client.group.<a href="./src/braintrust/resources/group.py">update</a>(group_id, \*\*<a href="src/braintrust/types/group_update_params.py">params</a>) -> <a href="./src/braintrust/types/group.py">Group</a></code>
- <code title="get /v1/group">client.group.<a href="./src/braintrust/resources/group.py">list</a>(\*\*<a href="src/braintrust/types/group_list_params.py">params</a>) -> <a href="./src/braintrust/types/group.py">SyncListObjects[Group]</a></code>
- <code title="delete /v1/group/{group_id}">client.group.<a href="./src/braintrust/resources/group.py">delete</a>(group_id) -> <a href="./src/braintrust/types/group.py">Group</a></code>
- <code title="put /v1/group">client.group.<a href="./src/braintrust/resources/group.py">replace</a>(\*\*<a href="src/braintrust/types/group_replace_params.py">params</a>) -> <a href="./src/braintrust/types/group.py">Group</a></code>

# ACL

Types:

```python
from braintrust.types import ACL
```

Methods:

- <code title="post /v1/acl">client.acl.<a href="./src/braintrust/resources/acl.py">create</a>(\*\*<a href="src/braintrust/types/acl_create_params.py">params</a>) -> <a href="./src/braintrust/types/acl.py">ACL</a></code>
- <code title="get /v1/acl/{acl_id}">client.acl.<a href="./src/braintrust/resources/acl.py">retrieve</a>(acl_id) -> <a href="./src/braintrust/types/acl.py">ACL</a></code>
- <code title="get /v1/acl">client.acl.<a href="./src/braintrust/resources/acl.py">list</a>(\*\*<a href="src/braintrust/types/acl_list_params.py">params</a>) -> <a href="./src/braintrust/types/acl.py">SyncListObjects[ACL]</a></code>
- <code title="delete /v1/acl/{acl_id}">client.acl.<a href="./src/braintrust/resources/acl.py">delete</a>(acl_id) -> <a href="./src/braintrust/types/acl.py">ACL</a></code>
- <code title="put /v1/acl">client.acl.<a href="./src/braintrust/resources/acl.py">replace</a>(\*\*<a href="src/braintrust/types/acl_replace_params.py">params</a>) -> <a href="./src/braintrust/types/acl.py">ACL</a></code>

# User

Types:

```python
from braintrust.types import User
```

Methods:

- <code title="get /v1/user/{user_id}">client.user.<a href="./src/braintrust/resources/user.py">retrieve</a>(user_id) -> <a href="./src/braintrust/types/user.py">User</a></code>
- <code title="get /v1/user">client.user.<a href="./src/braintrust/resources/user.py">list</a>(\*\*<a href="src/braintrust/types/user_list_params.py">params</a>) -> <a href="./src/braintrust/types/user.py">SyncListObjects[User]</a></code>
