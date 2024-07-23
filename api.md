# TopLevel

Types:

```python
from braintrust.types import TopLevelHelloWorldResponse
```

Methods:

- <code title="get /v1">client.top_level.<a href="./src/braintrust/resources/top_level.py">hello_world</a>() -> str</code>

# Projects

Types:

```python
from braintrust.types import Project
```

Methods:

- <code title="post /v1/project">client.projects.<a href="./src/braintrust/resources/projects/projects.py">create</a>(\*\*<a href="src/braintrust/types/project_create_params.py">params</a>) -> <a href="./src/braintrust/types/project.py">Project</a></code>
- <code title="get /v1/project/{project_id}">client.projects.<a href="./src/braintrust/resources/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/braintrust/types/project.py">Project</a></code>
- <code title="patch /v1/project/{project_id}">client.projects.<a href="./src/braintrust/resources/projects/projects.py">update</a>(project_id, \*\*<a href="src/braintrust/types/project_update_params.py">params</a>) -> <a href="./src/braintrust/types/project.py">Project</a></code>
- <code title="get /v1/project">client.projects.<a href="./src/braintrust/resources/projects/projects.py">list</a>(\*\*<a href="src/braintrust/types/project_list_params.py">params</a>) -> <a href="./src/braintrust/types/project.py">SyncListObjects[Project]</a></code>
- <code title="delete /v1/project/{project_id}">client.projects.<a href="./src/braintrust/resources/projects/projects.py">delete</a>(project_id) -> <a href="./src/braintrust/types/project.py">Project</a></code>

## Logs

Types:

```python
from braintrust.types.projects import LogFetchResponse, LogFetchPostResponse, LogInsertResponse
```

Methods:

- <code title="post /v1/project_logs/{project_id}/feedback">client.projects.logs.<a href="./src/braintrust/resources/projects/logs.py">feedback</a>(project_id, \*\*<a href="src/braintrust/types/projects/log_feedback_params.py">params</a>) -> None</code>
- <code title="get /v1/project_logs/{project_id}/fetch">client.projects.logs.<a href="./src/braintrust/resources/projects/logs.py">fetch</a>(project_id, \*\*<a href="src/braintrust/types/projects/log_fetch_params.py">params</a>) -> <a href="./src/braintrust/types/projects/log_fetch_response.py">LogFetchResponse</a></code>
- <code title="post /v1/project_logs/{project_id}/fetch">client.projects.logs.<a href="./src/braintrust/resources/projects/logs.py">fetch_post</a>(project_id, \*\*<a href="src/braintrust/types/projects/log_fetch_post_params.py">params</a>) -> <a href="./src/braintrust/types/projects/log_fetch_post_response.py">LogFetchPostResponse</a></code>
- <code title="post /v1/project_logs/{project_id}/insert">client.projects.logs.<a href="./src/braintrust/resources/projects/logs.py">insert</a>(project_id, \*\*<a href="src/braintrust/types/projects/log_insert_params.py">params</a>) -> <a href="./src/braintrust/types/projects/log_insert_response.py">LogInsertResponse</a></code>

# Experiments

Types:

```python
from braintrust.types import (
    Experiment,
    ExperimentFetchResponse,
    ExperimentFetchPostResponse,
    ExperimentInsertResponse,
    ExperimentSummarizeResponse,
)
```

Methods:

- <code title="post /v1/experiment">client.experiments.<a href="./src/braintrust/resources/experiments.py">create</a>(\*\*<a href="src/braintrust/types/experiment_create_params.py">params</a>) -> <a href="./src/braintrust/types/experiment.py">Experiment</a></code>
- <code title="get /v1/experiment/{experiment_id}">client.experiments.<a href="./src/braintrust/resources/experiments.py">retrieve</a>(experiment_id) -> <a href="./src/braintrust/types/experiment.py">Experiment</a></code>
- <code title="patch /v1/experiment/{experiment_id}">client.experiments.<a href="./src/braintrust/resources/experiments.py">update</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_update_params.py">params</a>) -> <a href="./src/braintrust/types/experiment.py">Experiment</a></code>
- <code title="get /v1/experiment">client.experiments.<a href="./src/braintrust/resources/experiments.py">list</a>(\*\*<a href="src/braintrust/types/experiment_list_params.py">params</a>) -> <a href="./src/braintrust/types/experiment.py">SyncListObjects[Experiment]</a></code>
- <code title="delete /v1/experiment/{experiment_id}">client.experiments.<a href="./src/braintrust/resources/experiments.py">delete</a>(experiment_id) -> <a href="./src/braintrust/types/experiment.py">Experiment</a></code>
- <code title="post /v1/experiment/{experiment_id}/feedback">client.experiments.<a href="./src/braintrust/resources/experiments.py">feedback</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_feedback_params.py">params</a>) -> None</code>
- <code title="get /v1/experiment/{experiment_id}/fetch">client.experiments.<a href="./src/braintrust/resources/experiments.py">fetch</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_fetch_params.py">params</a>) -> <a href="./src/braintrust/types/experiment_fetch_response.py">ExperimentFetchResponse</a></code>
- <code title="post /v1/experiment/{experiment_id}/fetch">client.experiments.<a href="./src/braintrust/resources/experiments.py">fetch_post</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_fetch_post_params.py">params</a>) -> <a href="./src/braintrust/types/experiment_fetch_post_response.py">ExperimentFetchPostResponse</a></code>
- <code title="post /v1/experiment/{experiment_id}/insert">client.experiments.<a href="./src/braintrust/resources/experiments.py">insert</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_insert_params.py">params</a>) -> <a href="./src/braintrust/types/experiment_insert_response.py">ExperimentInsertResponse</a></code>
- <code title="get /v1/experiment/{experiment_id}/summarize">client.experiments.<a href="./src/braintrust/resources/experiments.py">summarize</a>(experiment_id, \*\*<a href="src/braintrust/types/experiment_summarize_params.py">params</a>) -> <a href="./src/braintrust/types/experiment_summarize_response.py">ExperimentSummarizeResponse</a></code>

# Datasets

Types:

```python
from braintrust.types import (
    Dataset,
    DatasetFetchResponse,
    DatasetFetchPostResponse,
    DatasetInsertResponse,
    DatasetSummarizeResponse,
)
```

Methods:

- <code title="post /v1/dataset">client.datasets.<a href="./src/braintrust/resources/datasets.py">create</a>(\*\*<a href="src/braintrust/types/dataset_create_params.py">params</a>) -> <a href="./src/braintrust/types/dataset.py">Dataset</a></code>
- <code title="get /v1/dataset/{dataset_id}">client.datasets.<a href="./src/braintrust/resources/datasets.py">retrieve</a>(dataset_id) -> <a href="./src/braintrust/types/dataset.py">Dataset</a></code>
- <code title="patch /v1/dataset/{dataset_id}">client.datasets.<a href="./src/braintrust/resources/datasets.py">update</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_update_params.py">params</a>) -> <a href="./src/braintrust/types/dataset.py">Dataset</a></code>
- <code title="get /v1/dataset">client.datasets.<a href="./src/braintrust/resources/datasets.py">list</a>(\*\*<a href="src/braintrust/types/dataset_list_params.py">params</a>) -> <a href="./src/braintrust/types/dataset.py">SyncListObjects[Dataset]</a></code>
- <code title="delete /v1/dataset/{dataset_id}">client.datasets.<a href="./src/braintrust/resources/datasets.py">delete</a>(dataset_id) -> <a href="./src/braintrust/types/dataset.py">Dataset</a></code>
- <code title="post /v1/dataset/{dataset_id}/feedback">client.datasets.<a href="./src/braintrust/resources/datasets.py">feedback</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_feedback_params.py">params</a>) -> None</code>
- <code title="get /v1/dataset/{dataset_id}/fetch">client.datasets.<a href="./src/braintrust/resources/datasets.py">fetch</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_fetch_params.py">params</a>) -> <a href="./src/braintrust/types/dataset_fetch_response.py">DatasetFetchResponse</a></code>
- <code title="post /v1/dataset/{dataset_id}/fetch">client.datasets.<a href="./src/braintrust/resources/datasets.py">fetch_post</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_fetch_post_params.py">params</a>) -> <a href="./src/braintrust/types/dataset_fetch_post_response.py">DatasetFetchPostResponse</a></code>
- <code title="post /v1/dataset/{dataset_id}/insert">client.datasets.<a href="./src/braintrust/resources/datasets.py">insert</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_insert_params.py">params</a>) -> <a href="./src/braintrust/types/dataset_insert_response.py">DatasetInsertResponse</a></code>
- <code title="get /v1/dataset/{dataset_id}/summarize">client.datasets.<a href="./src/braintrust/resources/datasets.py">summarize</a>(dataset_id, \*\*<a href="src/braintrust/types/dataset_summarize_params.py">params</a>) -> <a href="./src/braintrust/types/dataset_summarize_response.py">DatasetSummarizeResponse</a></code>

# Prompts

Types:

```python
from braintrust.types import Prompt
```

Methods:

- <code title="post /v1/prompt">client.prompts.<a href="./src/braintrust/resources/prompts.py">create</a>(\*\*<a href="src/braintrust/types/prompt_create_params.py">params</a>) -> <a href="./src/braintrust/types/prompt.py">Prompt</a></code>
- <code title="get /v1/prompt/{prompt_id}">client.prompts.<a href="./src/braintrust/resources/prompts.py">retrieve</a>(prompt_id) -> <a href="./src/braintrust/types/prompt.py">Prompt</a></code>
- <code title="patch /v1/prompt/{prompt_id}">client.prompts.<a href="./src/braintrust/resources/prompts.py">update</a>(prompt_id, \*\*<a href="src/braintrust/types/prompt_update_params.py">params</a>) -> <a href="./src/braintrust/types/prompt.py">Prompt</a></code>
- <code title="get /v1/prompt">client.prompts.<a href="./src/braintrust/resources/prompts.py">list</a>(\*\*<a href="src/braintrust/types/prompt_list_params.py">params</a>) -> <a href="./src/braintrust/types/prompt.py">SyncListObjects[Prompt]</a></code>
- <code title="delete /v1/prompt/{prompt_id}">client.prompts.<a href="./src/braintrust/resources/prompts.py">delete</a>(prompt_id) -> <a href="./src/braintrust/types/prompt.py">Prompt</a></code>
- <code title="post /v1/prompt/{prompt_id}/feedback">client.prompts.<a href="./src/braintrust/resources/prompts.py">feedback</a>(prompt_id, \*\*<a href="src/braintrust/types/prompt_feedback_params.py">params</a>) -> None</code>
- <code title="put /v1/prompt">client.prompts.<a href="./src/braintrust/resources/prompts.py">replace</a>(\*\*<a href="src/braintrust/types/prompt_replace_params.py">params</a>) -> <a href="./src/braintrust/types/prompt.py">Prompt</a></code>

# Roles

Types:

```python
from braintrust.types import Role
```

Methods:

- <code title="post /v1/role">client.roles.<a href="./src/braintrust/resources/roles.py">create</a>(\*\*<a href="src/braintrust/types/role_create_params.py">params</a>) -> <a href="./src/braintrust/types/role.py">Role</a></code>
- <code title="get /v1/role/{role_id}">client.roles.<a href="./src/braintrust/resources/roles.py">retrieve</a>(role_id) -> <a href="./src/braintrust/types/role.py">Role</a></code>
- <code title="patch /v1/role/{role_id}">client.roles.<a href="./src/braintrust/resources/roles.py">update</a>(role_id, \*\*<a href="src/braintrust/types/role_update_params.py">params</a>) -> <a href="./src/braintrust/types/role.py">Role</a></code>
- <code title="get /v1/role">client.roles.<a href="./src/braintrust/resources/roles.py">list</a>(\*\*<a href="src/braintrust/types/role_list_params.py">params</a>) -> <a href="./src/braintrust/types/role.py">SyncListObjects[Role]</a></code>
- <code title="delete /v1/role/{role_id}">client.roles.<a href="./src/braintrust/resources/roles.py">delete</a>(role_id) -> <a href="./src/braintrust/types/role.py">Role</a></code>
- <code title="put /v1/role">client.roles.<a href="./src/braintrust/resources/roles.py">replace</a>(\*\*<a href="src/braintrust/types/role_replace_params.py">params</a>) -> <a href="./src/braintrust/types/role.py">Role</a></code>

# Groups

Types:

```python
from braintrust.types import Group
```

Methods:

- <code title="post /v1/group">client.groups.<a href="./src/braintrust/resources/groups.py">create</a>(\*\*<a href="src/braintrust/types/group_create_params.py">params</a>) -> <a href="./src/braintrust/types/group.py">Group</a></code>
- <code title="get /v1/group/{group_id}">client.groups.<a href="./src/braintrust/resources/groups.py">retrieve</a>(group_id) -> <a href="./src/braintrust/types/group.py">Group</a></code>
- <code title="patch /v1/group/{group_id}">client.groups.<a href="./src/braintrust/resources/groups.py">update</a>(group_id, \*\*<a href="src/braintrust/types/group_update_params.py">params</a>) -> <a href="./src/braintrust/types/group.py">Group</a></code>
- <code title="get /v1/group">client.groups.<a href="./src/braintrust/resources/groups.py">list</a>(\*\*<a href="src/braintrust/types/group_list_params.py">params</a>) -> <a href="./src/braintrust/types/group.py">SyncListObjects[Group]</a></code>
- <code title="delete /v1/group/{group_id}">client.groups.<a href="./src/braintrust/resources/groups.py">delete</a>(group_id) -> <a href="./src/braintrust/types/group.py">Group</a></code>
- <code title="put /v1/group">client.groups.<a href="./src/braintrust/resources/groups.py">replace</a>(\*\*<a href="src/braintrust/types/group_replace_params.py">params</a>) -> <a href="./src/braintrust/types/group.py">Group</a></code>

# ACLs

Types:

```python
from braintrust.types import ACL
```

Methods:

- <code title="post /v1/acl">client.acls.<a href="./src/braintrust/resources/acls.py">create</a>(\*\*<a href="src/braintrust/types/acl_create_params.py">params</a>) -> <a href="./src/braintrust/types/acl.py">ACL</a></code>
- <code title="get /v1/acl/{acl_id}">client.acls.<a href="./src/braintrust/resources/acls.py">retrieve</a>(acl_id) -> <a href="./src/braintrust/types/acl.py">ACL</a></code>
- <code title="get /v1/acl">client.acls.<a href="./src/braintrust/resources/acls.py">list</a>(\*\*<a href="src/braintrust/types/acl_list_params.py">params</a>) -> <a href="./src/braintrust/types/acl.py">SyncListObjects[ACL]</a></code>
- <code title="delete /v1/acl/{acl_id}">client.acls.<a href="./src/braintrust/resources/acls.py">delete</a>(acl_id) -> <a href="./src/braintrust/types/acl.py">ACL</a></code>

# Users

Types:

```python
from braintrust.types import User
```

Methods:

- <code title="get /v1/user/{user_id}">client.users.<a href="./src/braintrust/resources/users.py">retrieve</a>(user_id) -> <a href="./src/braintrust/types/user.py">User</a></code>
- <code title="get /v1/user">client.users.<a href="./src/braintrust/resources/users.py">list</a>(\*\*<a href="src/braintrust/types/user_list_params.py">params</a>) -> <a href="./src/braintrust/types/user.py">SyncListObjects[User]</a></code>

# ProjectScores

Types:

```python
from braintrust.types import ProjectScore
```

Methods:

- <code title="post /v1/project_score">client.project_scores.<a href="./src/braintrust/resources/project_scores.py">create</a>(\*\*<a href="src/braintrust/types/project_score_create_params.py">params</a>) -> <a href="./src/braintrust/types/project_score.py">ProjectScore</a></code>
- <code title="get /v1/project_score/{project_score_id}">client.project_scores.<a href="./src/braintrust/resources/project_scores.py">retrieve</a>(project_score_id) -> <a href="./src/braintrust/types/project_score.py">ProjectScore</a></code>
- <code title="patch /v1/project_score/{project_score_id}">client.project_scores.<a href="./src/braintrust/resources/project_scores.py">update</a>(project_score_id, \*\*<a href="src/braintrust/types/project_score_update_params.py">params</a>) -> <a href="./src/braintrust/types/project_score.py">ProjectScore</a></code>
- <code title="get /v1/project_score">client.project_scores.<a href="./src/braintrust/resources/project_scores.py">list</a>(\*\*<a href="src/braintrust/types/project_score_list_params.py">params</a>) -> <a href="./src/braintrust/types/project_score.py">SyncListObjects[ProjectScore]</a></code>
- <code title="delete /v1/project_score/{project_score_id}">client.project_scores.<a href="./src/braintrust/resources/project_scores.py">delete</a>(project_score_id) -> <a href="./src/braintrust/types/project_score.py">ProjectScore</a></code>
- <code title="put /v1/project_score">client.project_scores.<a href="./src/braintrust/resources/project_scores.py">replace</a>(\*\*<a href="src/braintrust/types/project_score_replace_params.py">params</a>) -> <a href="./src/braintrust/types/project_score.py">ProjectScore</a></code>

# ProjectTags

Types:

```python
from braintrust.types import ProjectTag
```

Methods:

- <code title="post /v1/project_tag">client.project_tags.<a href="./src/braintrust/resources/project_tags.py">create</a>(\*\*<a href="src/braintrust/types/project_tag_create_params.py">params</a>) -> <a href="./src/braintrust/types/project_tag.py">ProjectTag</a></code>
- <code title="get /v1/project_tag/{project_tag_id}">client.project_tags.<a href="./src/braintrust/resources/project_tags.py">retrieve</a>(project_tag_id) -> <a href="./src/braintrust/types/project_tag.py">ProjectTag</a></code>
- <code title="patch /v1/project_tag/{project_tag_id}">client.project_tags.<a href="./src/braintrust/resources/project_tags.py">update</a>(project_tag_id, \*\*<a href="src/braintrust/types/project_tag_update_params.py">params</a>) -> <a href="./src/braintrust/types/project_tag.py">ProjectTag</a></code>
- <code title="get /v1/project_tag">client.project_tags.<a href="./src/braintrust/resources/project_tags.py">list</a>(\*\*<a href="src/braintrust/types/project_tag_list_params.py">params</a>) -> <a href="./src/braintrust/types/project_tag.py">SyncListObjects[ProjectTag]</a></code>
- <code title="delete /v1/project_tag/{project_tag_id}">client.project_tags.<a href="./src/braintrust/resources/project_tags.py">delete</a>(project_tag_id) -> <a href="./src/braintrust/types/project_tag.py">ProjectTag</a></code>
- <code title="put /v1/project_tag">client.project_tags.<a href="./src/braintrust/resources/project_tags.py">replace</a>(\*\*<a href="src/braintrust/types/project_tag_replace_params.py">params</a>) -> <a href="./src/braintrust/types/project_tag.py">ProjectTag</a></code>

# Functions

Types:

```python
from braintrust.types import Function
```

Methods:

- <code title="post /v1/function">client.functions.<a href="./src/braintrust/resources/functions.py">create</a>(\*\*<a href="src/braintrust/types/function_create_params.py">params</a>) -> <a href="./src/braintrust/types/function.py">Function</a></code>
- <code title="get /v1/function/{function_id}">client.functions.<a href="./src/braintrust/resources/functions.py">retrieve</a>(function_id) -> <a href="./src/braintrust/types/function.py">Function</a></code>
- <code title="patch /v1/function/{function_id}">client.functions.<a href="./src/braintrust/resources/functions.py">update</a>(function_id, \*\*<a href="src/braintrust/types/function_update_params.py">params</a>) -> <a href="./src/braintrust/types/function.py">Function</a></code>
- <code title="get /v1/function">client.functions.<a href="./src/braintrust/resources/functions.py">list</a>(\*\*<a href="src/braintrust/types/function_list_params.py">params</a>) -> <a href="./src/braintrust/types/function.py">SyncListObjects[Function]</a></code>
- <code title="delete /v1/function/{function_id}">client.functions.<a href="./src/braintrust/resources/functions.py">delete</a>(function_id) -> <a href="./src/braintrust/types/function.py">Function</a></code>
- <code title="post /v1/function/{function_id}/feedback">client.functions.<a href="./src/braintrust/resources/functions.py">feedback</a>(function_id, \*\*<a href="src/braintrust/types/function_feedback_params.py">params</a>) -> None</code>
- <code title="put /v1/function">client.functions.<a href="./src/braintrust/resources/functions.py">replace</a>(\*\*<a href="src/braintrust/types/function_replace_params.py">params</a>) -> <a href="./src/braintrust/types/function.py">Function</a></code>

# Views

Types:

```python
from braintrust.types import View
```

Methods:

- <code title="post /v1/view">client.views.<a href="./src/braintrust/resources/views.py">create</a>(\*\*<a href="src/braintrust/types/view_create_params.py">params</a>) -> <a href="./src/braintrust/types/view.py">View</a></code>
- <code title="get /v1/view/{view_id}">client.views.<a href="./src/braintrust/resources/views.py">retrieve</a>(view_id, \*\*<a href="src/braintrust/types/view_retrieve_params.py">params</a>) -> <a href="./src/braintrust/types/view.py">View</a></code>
- <code title="patch /v1/view/{view_id}">client.views.<a href="./src/braintrust/resources/views.py">update</a>(view_id, \*\*<a href="src/braintrust/types/view_update_params.py">params</a>) -> <a href="./src/braintrust/types/view.py">View</a></code>
- <code title="get /v1/view">client.views.<a href="./src/braintrust/resources/views.py">list</a>(\*\*<a href="src/braintrust/types/view_list_params.py">params</a>) -> <a href="./src/braintrust/types/view.py">SyncListObjects[View]</a></code>
- <code title="delete /v1/view/{view_id}">client.views.<a href="./src/braintrust/resources/views.py">delete</a>(view_id, \*\*<a href="src/braintrust/types/view_delete_params.py">params</a>) -> <a href="./src/braintrust/types/view.py">View</a></code>
- <code title="put /v1/view">client.views.<a href="./src/braintrust/resources/views.py">replace</a>(\*\*<a href="src/braintrust/types/view_replace_params.py">params</a>) -> <a href="./src/braintrust/types/view.py">View</a></code>

# Organizations

Types:

```python
from braintrust.types import Organization
```

Methods:

- <code title="get /v1/organization/{organization_id}">client.organizations.<a href="./src/braintrust/resources/organizations.py">retrieve</a>(organization_id) -> <a href="./src/braintrust/types/organization.py">Organization</a></code>
- <code title="patch /v1/organization/{organization_id}">client.organizations.<a href="./src/braintrust/resources/organizations.py">update</a>(organization_id, \*\*<a href="src/braintrust/types/organization_update_params.py">params</a>) -> <a href="./src/braintrust/types/organization.py">Organization</a></code>
- <code title="get /v1/organization">client.organizations.<a href="./src/braintrust/resources/organizations.py">list</a>(\*\*<a href="src/braintrust/types/organization_list_params.py">params</a>) -> <a href="./src/braintrust/types/organization.py">SyncListObjects[Organization]</a></code>
- <code title="delete /v1/organization/{organization_id}">client.organizations.<a href="./src/braintrust/resources/organizations.py">delete</a>(organization_id) -> <a href="./src/braintrust/types/organization.py">Organization</a></code>

# APIKeys

Types:

```python
from braintrust.types import APIKey, APIKeyCreateResponse
```

Methods:

- <code title="post /v1/api_key">client.api_keys.<a href="./src/braintrust/resources/api_keys.py">create</a>(\*\*<a href="src/braintrust/types/api_key_create_params.py">params</a>) -> <a href="./src/braintrust/types/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="get /v1/api_key/{api_key_id}">client.api_keys.<a href="./src/braintrust/resources/api_keys.py">retrieve</a>(api_key_id) -> <a href="./src/braintrust/types/api_key.py">APIKey</a></code>
- <code title="get /v1/api_key">client.api_keys.<a href="./src/braintrust/resources/api_keys.py">list</a>(\*\*<a href="src/braintrust/types/api_key_list_params.py">params</a>) -> <a href="./src/braintrust/types/api_key.py">SyncListObjects[APIKey]</a></code>
- <code title="delete /v1/api_key/{api_key_id}">client.api_keys.<a href="./src/braintrust/resources/api_keys.py">delete</a>(api_key_id) -> <a href="./src/braintrust/types/api_key.py">APIKey</a></code>
