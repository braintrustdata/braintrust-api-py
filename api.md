# Shared Types

```python
from braintrust_api.types import (
    AISecret,
    ACL,
    ACLBatchUpdateResponse,
    APIKey,
    ChatCompletionContentPartImage,
    ChatCompletionContentPartText,
    ChatCompletionMessageToolCall,
    CodeBundle,
    CreateAPIKeyOutput,
    CrossObjectInsertResponse,
    DataSummary,
    Dataset,
    DatasetEvent,
    EnvVar,
    Experiment,
    ExperimentEvent,
    FeedbackDatasetItem,
    FeedbackExperimentItem,
    FeedbackProjectLogsItem,
    FeedbackResponseSchema,
    FetchDatasetEventsResponse,
    FetchExperimentEventsResponse,
    FetchProjectLogsEventsResponse,
    Function,
    Group,
    InsertDatasetEventMerge,
    InsertDatasetEventReplace,
    InsertEventsResponse,
    InsertExperimentEventMerge,
    InsertExperimentEventReplace,
    InsertProjectLogsEventMerge,
    InsertProjectLogsEventReplace,
    MetricSummary,
    OnlineScoreConfig,
    Organization,
    PatchOrganizationMembersOutput,
    PathLookupFilter,
    Project,
    ProjectLogsEvent,
    ProjectScore,
    ProjectScoreCategory,
    ProjectScoreConfig,
    ProjectSettings,
    ProjectTag,
    Prompt,
    PromptData,
    RepoInfo,
    Role,
    ScoreSummary,
    SpanIFrame,
    SummarizeDatasetResponse,
    SummarizeExperimentResponse,
    User,
    View,
    ViewData,
    ViewDataSearch,
    ViewOptions,
)
```

# TopLevel

Types:

```python
from braintrust_api.types import TopLevelHelloWorldResponse
```

Methods:

- <code title="get /v1">client.top_level.<a href="./src/braintrust_api/resources/top_level.py">hello_world</a>() -> str</code>

# Projects

Methods:

- <code title="post /v1/project">client.projects.<a href="./src/braintrust_api/resources/projects/projects.py">create</a>(\*\*<a href="src/braintrust_api/types/project_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/project.py">Project</a></code>
- <code title="get /v1/project/{project_id}">client.projects.<a href="./src/braintrust_api/resources/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/braintrust_api/types/shared/project.py">Project</a></code>
- <code title="patch /v1/project/{project_id}">client.projects.<a href="./src/braintrust_api/resources/projects/projects.py">update</a>(project_id, \*\*<a href="src/braintrust_api/types/project_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/project.py">Project</a></code>
- <code title="get /v1/project">client.projects.<a href="./src/braintrust_api/resources/projects/projects.py">list</a>(\*\*<a href="src/braintrust_api/types/project_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/project.py">SyncListObjects[Project]</a></code>
- <code title="delete /v1/project/{project_id}">client.projects.<a href="./src/braintrust_api/resources/projects/projects.py">delete</a>(project_id) -> <a href="./src/braintrust_api/types/shared/project.py">Project</a></code>

## Logs

Types:

```python
from braintrust_api.types.projects import LogInsertResponse
```

Methods:

- <code title="post /v1/project_logs/{project_id}/feedback">client.projects.logs.<a href="./src/braintrust_api/resources/projects/logs.py">feedback</a>(project_id, \*\*<a href="src/braintrust_api/types/projects/log_feedback_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/feedback_response_schema.py">FeedbackResponseSchema</a></code>
- <code title="get /v1/project_logs/{project_id}/fetch">client.projects.logs.<a href="./src/braintrust_api/resources/projects/logs.py">fetch</a>(project_id, \*\*<a href="src/braintrust_api/types/projects/log_fetch_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/fetch_project_logs_events_response.py">FetchProjectLogsEventsResponse</a></code>
- <code title="post /v1/project_logs/{project_id}/fetch">client.projects.logs.<a href="./src/braintrust_api/resources/projects/logs.py">fetch_post</a>(project_id, \*\*<a href="src/braintrust_api/types/projects/log_fetch_post_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/fetch_project_logs_events_response.py">FetchProjectLogsEventsResponse</a></code>
- <code title="post /v1/project_logs/{project_id}/insert">client.projects.logs.<a href="./src/braintrust_api/resources/projects/logs.py">insert</a>(project_id, \*\*<a href="src/braintrust_api/types/projects/log_insert_params.py">params</a>) -> <a href="./src/braintrust_api/types/projects/log_insert_response.py">LogInsertResponse</a></code>

# Experiments

Types:

```python
from braintrust_api.types import ExperimentInsertResponse
```

Methods:

- <code title="post /v1/experiment">client.experiments.<a href="./src/braintrust_api/resources/experiments.py">create</a>(\*\*<a href="src/braintrust_api/types/experiment_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/experiment.py">Experiment</a></code>
- <code title="get /v1/experiment/{experiment_id}">client.experiments.<a href="./src/braintrust_api/resources/experiments.py">retrieve</a>(experiment_id) -> <a href="./src/braintrust_api/types/shared/experiment.py">Experiment</a></code>
- <code title="patch /v1/experiment/{experiment_id}">client.experiments.<a href="./src/braintrust_api/resources/experiments.py">update</a>(experiment_id, \*\*<a href="src/braintrust_api/types/experiment_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/experiment.py">Experiment</a></code>
- <code title="get /v1/experiment">client.experiments.<a href="./src/braintrust_api/resources/experiments.py">list</a>(\*\*<a href="src/braintrust_api/types/experiment_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/experiment.py">SyncListObjects[Experiment]</a></code>
- <code title="delete /v1/experiment/{experiment_id}">client.experiments.<a href="./src/braintrust_api/resources/experiments.py">delete</a>(experiment_id) -> <a href="./src/braintrust_api/types/shared/experiment.py">Experiment</a></code>
- <code title="post /v1/experiment/{experiment_id}/feedback">client.experiments.<a href="./src/braintrust_api/resources/experiments.py">feedback</a>(experiment_id, \*\*<a href="src/braintrust_api/types/experiment_feedback_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/feedback_response_schema.py">FeedbackResponseSchema</a></code>
- <code title="get /v1/experiment/{experiment_id}/fetch">client.experiments.<a href="./src/braintrust_api/resources/experiments.py">fetch</a>(experiment_id, \*\*<a href="src/braintrust_api/types/experiment_fetch_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/fetch_experiment_events_response.py">FetchExperimentEventsResponse</a></code>
- <code title="post /v1/experiment/{experiment_id}/fetch">client.experiments.<a href="./src/braintrust_api/resources/experiments.py">fetch_post</a>(experiment_id, \*\*<a href="src/braintrust_api/types/experiment_fetch_post_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/fetch_experiment_events_response.py">FetchExperimentEventsResponse</a></code>
- <code title="post /v1/experiment/{experiment_id}/insert">client.experiments.<a href="./src/braintrust_api/resources/experiments.py">insert</a>(experiment_id, \*\*<a href="src/braintrust_api/types/experiment_insert_params.py">params</a>) -> <a href="./src/braintrust_api/types/experiment_insert_response.py">ExperimentInsertResponse</a></code>
- <code title="get /v1/experiment/{experiment_id}/summarize">client.experiments.<a href="./src/braintrust_api/resources/experiments.py">summarize</a>(experiment_id, \*\*<a href="src/braintrust_api/types/experiment_summarize_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/summarize_experiment_response.py">SummarizeExperimentResponse</a></code>

# Datasets

Methods:

- <code title="post /v1/dataset">client.datasets.<a href="./src/braintrust_api/resources/datasets.py">create</a>(\*\*<a href="src/braintrust_api/types/dataset_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/dataset.py">Dataset</a></code>
- <code title="get /v1/dataset/{dataset_id}">client.datasets.<a href="./src/braintrust_api/resources/datasets.py">retrieve</a>(dataset_id) -> <a href="./src/braintrust_api/types/shared/dataset.py">Dataset</a></code>
- <code title="patch /v1/dataset/{dataset_id}">client.datasets.<a href="./src/braintrust_api/resources/datasets.py">update</a>(dataset_id, \*\*<a href="src/braintrust_api/types/dataset_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/dataset.py">Dataset</a></code>
- <code title="get /v1/dataset">client.datasets.<a href="./src/braintrust_api/resources/datasets.py">list</a>(\*\*<a href="src/braintrust_api/types/dataset_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/dataset.py">SyncListObjects[Dataset]</a></code>
- <code title="delete /v1/dataset/{dataset_id}">client.datasets.<a href="./src/braintrust_api/resources/datasets.py">delete</a>(dataset_id) -> <a href="./src/braintrust_api/types/shared/dataset.py">Dataset</a></code>
- <code title="post /v1/dataset/{dataset_id}/feedback">client.datasets.<a href="./src/braintrust_api/resources/datasets.py">feedback</a>(dataset_id, \*\*<a href="src/braintrust_api/types/dataset_feedback_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/feedback_response_schema.py">FeedbackResponseSchema</a></code>
- <code title="get /v1/dataset/{dataset_id}/fetch">client.datasets.<a href="./src/braintrust_api/resources/datasets.py">fetch</a>(dataset_id, \*\*<a href="src/braintrust_api/types/dataset_fetch_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/fetch_dataset_events_response.py">FetchDatasetEventsResponse</a></code>
- <code title="post /v1/dataset/{dataset_id}/fetch">client.datasets.<a href="./src/braintrust_api/resources/datasets.py">fetch_post</a>(dataset_id, \*\*<a href="src/braintrust_api/types/dataset_fetch_post_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/fetch_dataset_events_response.py">FetchDatasetEventsResponse</a></code>
- <code title="post /v1/dataset/{dataset_id}/insert">client.datasets.<a href="./src/braintrust_api/resources/datasets.py">insert</a>(dataset_id, \*\*<a href="src/braintrust_api/types/dataset_insert_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/insert_events_response.py">InsertEventsResponse</a></code>
- <code title="get /v1/dataset/{dataset_id}/summarize">client.datasets.<a href="./src/braintrust_api/resources/datasets.py">summarize</a>(dataset_id, \*\*<a href="src/braintrust_api/types/dataset_summarize_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/summarize_dataset_response.py">SummarizeDatasetResponse</a></code>

# Prompts

Methods:

- <code title="post /v1/prompt">client.prompts.<a href="./src/braintrust_api/resources/prompts.py">create</a>(\*\*<a href="src/braintrust_api/types/prompt_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/prompt.py">Prompt</a></code>
- <code title="get /v1/prompt/{prompt_id}">client.prompts.<a href="./src/braintrust_api/resources/prompts.py">retrieve</a>(prompt_id) -> <a href="./src/braintrust_api/types/shared/prompt.py">Prompt</a></code>
- <code title="patch /v1/prompt/{prompt_id}">client.prompts.<a href="./src/braintrust_api/resources/prompts.py">update</a>(prompt_id, \*\*<a href="src/braintrust_api/types/prompt_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/prompt.py">Prompt</a></code>
- <code title="get /v1/prompt">client.prompts.<a href="./src/braintrust_api/resources/prompts.py">list</a>(\*\*<a href="src/braintrust_api/types/prompt_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/prompt.py">SyncListObjects[Prompt]</a></code>
- <code title="delete /v1/prompt/{prompt_id}">client.prompts.<a href="./src/braintrust_api/resources/prompts.py">delete</a>(prompt_id) -> <a href="./src/braintrust_api/types/shared/prompt.py">Prompt</a></code>
- <code title="put /v1/prompt">client.prompts.<a href="./src/braintrust_api/resources/prompts.py">replace</a>(\*\*<a href="src/braintrust_api/types/prompt_replace_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/prompt.py">Prompt</a></code>

# Roles

Methods:

- <code title="post /v1/role">client.roles.<a href="./src/braintrust_api/resources/roles.py">create</a>(\*\*<a href="src/braintrust_api/types/role_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/role.py">Role</a></code>
- <code title="get /v1/role/{role_id}">client.roles.<a href="./src/braintrust_api/resources/roles.py">retrieve</a>(role_id) -> <a href="./src/braintrust_api/types/shared/role.py">Role</a></code>
- <code title="patch /v1/role/{role_id}">client.roles.<a href="./src/braintrust_api/resources/roles.py">update</a>(role_id, \*\*<a href="src/braintrust_api/types/role_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/role.py">Role</a></code>
- <code title="get /v1/role">client.roles.<a href="./src/braintrust_api/resources/roles.py">list</a>(\*\*<a href="src/braintrust_api/types/role_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/role.py">SyncListObjects[Role]</a></code>
- <code title="delete /v1/role/{role_id}">client.roles.<a href="./src/braintrust_api/resources/roles.py">delete</a>(role_id) -> <a href="./src/braintrust_api/types/shared/role.py">Role</a></code>
- <code title="put /v1/role">client.roles.<a href="./src/braintrust_api/resources/roles.py">replace</a>(\*\*<a href="src/braintrust_api/types/role_replace_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/role.py">Role</a></code>

# Groups

Methods:

- <code title="post /v1/group">client.groups.<a href="./src/braintrust_api/resources/groups.py">create</a>(\*\*<a href="src/braintrust_api/types/group_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/group.py">Group</a></code>
- <code title="get /v1/group/{group_id}">client.groups.<a href="./src/braintrust_api/resources/groups.py">retrieve</a>(group_id) -> <a href="./src/braintrust_api/types/shared/group.py">Group</a></code>
- <code title="patch /v1/group/{group_id}">client.groups.<a href="./src/braintrust_api/resources/groups.py">update</a>(group_id, \*\*<a href="src/braintrust_api/types/group_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/group.py">Group</a></code>
- <code title="get /v1/group">client.groups.<a href="./src/braintrust_api/resources/groups.py">list</a>(\*\*<a href="src/braintrust_api/types/group_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/group.py">SyncListObjects[Group]</a></code>
- <code title="delete /v1/group/{group_id}">client.groups.<a href="./src/braintrust_api/resources/groups.py">delete</a>(group_id) -> <a href="./src/braintrust_api/types/shared/group.py">Group</a></code>
- <code title="put /v1/group">client.groups.<a href="./src/braintrust_api/resources/groups.py">replace</a>(\*\*<a href="src/braintrust_api/types/group_replace_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/group.py">Group</a></code>

# ACLs

Methods:

- <code title="post /v1/acl">client.acls.<a href="./src/braintrust_api/resources/acls.py">create</a>(\*\*<a href="src/braintrust_api/types/acl_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/acl.py">ACL</a></code>
- <code title="get /v1/acl/{acl_id}">client.acls.<a href="./src/braintrust_api/resources/acls.py">retrieve</a>(acl_id) -> <a href="./src/braintrust_api/types/shared/acl.py">ACL</a></code>
- <code title="get /v1/acl">client.acls.<a href="./src/braintrust_api/resources/acls.py">list</a>(\*\*<a href="src/braintrust_api/types/acl_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/acl.py">SyncListObjects[ACL]</a></code>
- <code title="delete /v1/acl/{acl_id}">client.acls.<a href="./src/braintrust_api/resources/acls.py">delete</a>(acl_id) -> <a href="./src/braintrust_api/types/shared/acl.py">ACL</a></code>
- <code title="post /v1/acl/batch-update">client.acls.<a href="./src/braintrust_api/resources/acls.py">batch_update</a>(\*\*<a href="src/braintrust_api/types/acl_batch_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/acl_batch_update_response.py">ACLBatchUpdateResponse</a></code>
- <code title="delete /v1/acl">client.acls.<a href="./src/braintrust_api/resources/acls.py">find_and_delete</a>(\*\*<a href="src/braintrust_api/types/acl_find_and_delete_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/acl.py">ACL</a></code>

# Users

Methods:

- <code title="get /v1/user/{user_id}">client.users.<a href="./src/braintrust_api/resources/users.py">retrieve</a>(user_id) -> <a href="./src/braintrust_api/types/shared/user.py">User</a></code>
- <code title="get /v1/user">client.users.<a href="./src/braintrust_api/resources/users.py">list</a>(\*\*<a href="src/braintrust_api/types/user_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/user.py">SyncListObjects[User]</a></code>

# ProjectScores

Methods:

- <code title="post /v1/project_score">client.project_scores.<a href="./src/braintrust_api/resources/project_scores.py">create</a>(\*\*<a href="src/braintrust_api/types/project_score_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/project_score.py">ProjectScore</a></code>
- <code title="get /v1/project_score/{project_score_id}">client.project_scores.<a href="./src/braintrust_api/resources/project_scores.py">retrieve</a>(project_score_id) -> <a href="./src/braintrust_api/types/shared/project_score.py">ProjectScore</a></code>
- <code title="patch /v1/project_score/{project_score_id}">client.project_scores.<a href="./src/braintrust_api/resources/project_scores.py">update</a>(project_score_id, \*\*<a href="src/braintrust_api/types/project_score_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/project_score.py">ProjectScore</a></code>
- <code title="get /v1/project_score">client.project_scores.<a href="./src/braintrust_api/resources/project_scores.py">list</a>(\*\*<a href="src/braintrust_api/types/project_score_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/project_score.py">SyncListObjects[ProjectScore]</a></code>
- <code title="delete /v1/project_score/{project_score_id}">client.project_scores.<a href="./src/braintrust_api/resources/project_scores.py">delete</a>(project_score_id) -> <a href="./src/braintrust_api/types/shared/project_score.py">ProjectScore</a></code>
- <code title="put /v1/project_score">client.project_scores.<a href="./src/braintrust_api/resources/project_scores.py">replace</a>(\*\*<a href="src/braintrust_api/types/project_score_replace_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/project_score.py">ProjectScore</a></code>

# ProjectTags

Methods:

- <code title="post /v1/project_tag">client.project_tags.<a href="./src/braintrust_api/resources/project_tags.py">create</a>(\*\*<a href="src/braintrust_api/types/project_tag_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/project_tag.py">ProjectTag</a></code>
- <code title="get /v1/project_tag/{project_tag_id}">client.project_tags.<a href="./src/braintrust_api/resources/project_tags.py">retrieve</a>(project_tag_id) -> <a href="./src/braintrust_api/types/shared/project_tag.py">ProjectTag</a></code>
- <code title="patch /v1/project_tag/{project_tag_id}">client.project_tags.<a href="./src/braintrust_api/resources/project_tags.py">update</a>(project_tag_id, \*\*<a href="src/braintrust_api/types/project_tag_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/project_tag.py">ProjectTag</a></code>
- <code title="get /v1/project_tag">client.project_tags.<a href="./src/braintrust_api/resources/project_tags.py">list</a>(\*\*<a href="src/braintrust_api/types/project_tag_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/project_tag.py">SyncListObjects[ProjectTag]</a></code>
- <code title="delete /v1/project_tag/{project_tag_id}">client.project_tags.<a href="./src/braintrust_api/resources/project_tags.py">delete</a>(project_tag_id) -> <a href="./src/braintrust_api/types/shared/project_tag.py">ProjectTag</a></code>
- <code title="put /v1/project_tag">client.project_tags.<a href="./src/braintrust_api/resources/project_tags.py">replace</a>(\*\*<a href="src/braintrust_api/types/project_tag_replace_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/project_tag.py">ProjectTag</a></code>

# SpanIframes

Methods:

- <code title="post /v1/span_iframe">client.span_iframes.<a href="./src/braintrust_api/resources/span_iframes.py">create</a>(\*\*<a href="src/braintrust_api/types/span_iframe_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/span_i_frame.py">SpanIFrame</a></code>
- <code title="get /v1/span_iframe/{span_iframe_id}">client.span_iframes.<a href="./src/braintrust_api/resources/span_iframes.py">retrieve</a>(span_iframe_id) -> <a href="./src/braintrust_api/types/shared/span_i_frame.py">SpanIFrame</a></code>
- <code title="patch /v1/span_iframe/{span_iframe_id}">client.span_iframes.<a href="./src/braintrust_api/resources/span_iframes.py">update</a>(span_iframe_id, \*\*<a href="src/braintrust_api/types/span_iframe_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/span_i_frame.py">SpanIFrame</a></code>
- <code title="get /v1/span_iframe">client.span_iframes.<a href="./src/braintrust_api/resources/span_iframes.py">list</a>(\*\*<a href="src/braintrust_api/types/span_iframe_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/span_i_frame.py">SyncListObjects[SpanIFrame]</a></code>
- <code title="delete /v1/span_iframe/{span_iframe_id}">client.span_iframes.<a href="./src/braintrust_api/resources/span_iframes.py">delete</a>(span_iframe_id) -> <a href="./src/braintrust_api/types/shared/span_i_frame.py">SpanIFrame</a></code>
- <code title="put /v1/span_iframe">client.span_iframes.<a href="./src/braintrust_api/resources/span_iframes.py">replace</a>(\*\*<a href="src/braintrust_api/types/span_iframe_replace_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/span_i_frame.py">SpanIFrame</a></code>

# Functions

Types:

```python
from braintrust_api.types import FunctionInvokeResponse
```

Methods:

- <code title="post /v1/function">client.functions.<a href="./src/braintrust_api/resources/functions.py">create</a>(\*\*<a href="src/braintrust_api/types/function_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/function.py">Function</a></code>
- <code title="get /v1/function/{function_id}">client.functions.<a href="./src/braintrust_api/resources/functions.py">retrieve</a>(function_id) -> <a href="./src/braintrust_api/types/shared/function.py">Function</a></code>
- <code title="patch /v1/function/{function_id}">client.functions.<a href="./src/braintrust_api/resources/functions.py">update</a>(function_id, \*\*<a href="src/braintrust_api/types/function_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/function.py">Function</a></code>
- <code title="get /v1/function">client.functions.<a href="./src/braintrust_api/resources/functions.py">list</a>(\*\*<a href="src/braintrust_api/types/function_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/function.py">SyncListObjects[Function]</a></code>
- <code title="delete /v1/function/{function_id}">client.functions.<a href="./src/braintrust_api/resources/functions.py">delete</a>(function_id) -> <a href="./src/braintrust_api/types/shared/function.py">Function</a></code>
- <code title="post /v1/function/{function_id}/invoke">client.functions.<a href="./src/braintrust_api/resources/functions.py">invoke</a>(function_id, \*\*<a href="src/braintrust_api/types/function_invoke_params.py">params</a>) -> <a href="./src/braintrust_api/types/function_invoke_response.py">object</a></code>
- <code title="put /v1/function">client.functions.<a href="./src/braintrust_api/resources/functions.py">replace</a>(\*\*<a href="src/braintrust_api/types/function_replace_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/function.py">Function</a></code>

# Views

Methods:

- <code title="post /v1/view">client.views.<a href="./src/braintrust_api/resources/views.py">create</a>(\*\*<a href="src/braintrust_api/types/view_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/view.py">View</a></code>
- <code title="get /v1/view/{view_id}">client.views.<a href="./src/braintrust_api/resources/views.py">retrieve</a>(view_id, \*\*<a href="src/braintrust_api/types/view_retrieve_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/view.py">View</a></code>
- <code title="patch /v1/view/{view_id}">client.views.<a href="./src/braintrust_api/resources/views.py">update</a>(view_id, \*\*<a href="src/braintrust_api/types/view_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/view.py">View</a></code>
- <code title="get /v1/view">client.views.<a href="./src/braintrust_api/resources/views.py">list</a>(\*\*<a href="src/braintrust_api/types/view_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/view.py">SyncListObjects[View]</a></code>
- <code title="delete /v1/view/{view_id}">client.views.<a href="./src/braintrust_api/resources/views.py">delete</a>(view_id, \*\*<a href="src/braintrust_api/types/view_delete_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/view.py">View</a></code>
- <code title="put /v1/view">client.views.<a href="./src/braintrust_api/resources/views.py">replace</a>(\*\*<a href="src/braintrust_api/types/view_replace_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/view.py">View</a></code>

# Organizations

Methods:

- <code title="get /v1/organization/{organization_id}">client.organizations.<a href="./src/braintrust_api/resources/organizations/organizations.py">retrieve</a>(organization_id) -> <a href="./src/braintrust_api/types/shared/organization.py">Organization</a></code>
- <code title="patch /v1/organization/{organization_id}">client.organizations.<a href="./src/braintrust_api/resources/organizations/organizations.py">update</a>(organization_id, \*\*<a href="src/braintrust_api/types/organization_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/organization.py">Organization</a></code>
- <code title="get /v1/organization">client.organizations.<a href="./src/braintrust_api/resources/organizations/organizations.py">list</a>(\*\*<a href="src/braintrust_api/types/organization_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/organization.py">SyncListObjects[Organization]</a></code>
- <code title="delete /v1/organization/{organization_id}">client.organizations.<a href="./src/braintrust_api/resources/organizations/organizations.py">delete</a>(organization_id) -> <a href="./src/braintrust_api/types/shared/organization.py">Organization</a></code>

## Members

Methods:

- <code title="patch /v1/organization/members">client.organizations.members.<a href="./src/braintrust_api/resources/organizations/members.py">update</a>(\*\*<a href="src/braintrust_api/types/organizations/member_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/patch_organization_members_output.py">PatchOrganizationMembersOutput</a></code>

# APIKeys

Methods:

- <code title="post /v1/api_key">client.api_keys.<a href="./src/braintrust_api/resources/api_keys.py">create</a>(\*\*<a href="src/braintrust_api/types/api_key_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/create_api_key_output.py">CreateAPIKeyOutput</a></code>
- <code title="get /v1/api_key/{api_key_id}">client.api_keys.<a href="./src/braintrust_api/resources/api_keys.py">retrieve</a>(api_key_id) -> <a href="./src/braintrust_api/types/shared/api_key.py">APIKey</a></code>
- <code title="get /v1/api_key">client.api_keys.<a href="./src/braintrust_api/resources/api_keys.py">list</a>(\*\*<a href="src/braintrust_api/types/api_key_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/api_key.py">SyncListObjects[APIKey]</a></code>
- <code title="delete /v1/api_key/{api_key_id}">client.api_keys.<a href="./src/braintrust_api/resources/api_keys.py">delete</a>(api_key_id) -> <a href="./src/braintrust_api/types/shared/api_key.py">APIKey</a></code>

# AISecrets

Methods:

- <code title="post /v1/ai_secret">client.ai_secrets.<a href="./src/braintrust_api/resources/ai_secrets.py">create</a>(\*\*<a href="src/braintrust_api/types/ai_secret_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/a_i_secret.py">AISecret</a></code>
- <code title="get /v1/ai_secret/{ai_secret_id}">client.ai_secrets.<a href="./src/braintrust_api/resources/ai_secrets.py">retrieve</a>(ai_secret_id) -> <a href="./src/braintrust_api/types/shared/a_i_secret.py">AISecret</a></code>
- <code title="patch /v1/ai_secret/{ai_secret_id}">client.ai_secrets.<a href="./src/braintrust_api/resources/ai_secrets.py">update</a>(ai_secret_id, \*\*<a href="src/braintrust_api/types/ai_secret_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/a_i_secret.py">AISecret</a></code>
- <code title="get /v1/ai_secret">client.ai_secrets.<a href="./src/braintrust_api/resources/ai_secrets.py">list</a>(\*\*<a href="src/braintrust_api/types/ai_secret_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/a_i_secret.py">SyncListObjects[AISecret]</a></code>
- <code title="delete /v1/ai_secret/{ai_secret_id}">client.ai_secrets.<a href="./src/braintrust_api/resources/ai_secrets.py">delete</a>(ai_secret_id) -> <a href="./src/braintrust_api/types/shared/a_i_secret.py">AISecret</a></code>
- <code title="delete /v1/ai_secret">client.ai_secrets.<a href="./src/braintrust_api/resources/ai_secrets.py">find_and_delete</a>(\*\*<a href="src/braintrust_api/types/ai_secret_find_and_delete_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/a_i_secret.py">AISecret</a></code>
- <code title="put /v1/ai_secret">client.ai_secrets.<a href="./src/braintrust_api/resources/ai_secrets.py">replace</a>(\*\*<a href="src/braintrust_api/types/ai_secret_replace_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/a_i_secret.py">AISecret</a></code>

# EnvVars

Types:

```python
from braintrust_api.types import EnvVarListResponse
```

Methods:

- <code title="post /v1/env_var">client.env_vars.<a href="./src/braintrust_api/resources/env_vars.py">create</a>(\*\*<a href="src/braintrust_api/types/env_var_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/env_var.py">EnvVar</a></code>
- <code title="get /v1/env_var/{env_var_id}">client.env_vars.<a href="./src/braintrust_api/resources/env_vars.py">retrieve</a>(env_var_id) -> <a href="./src/braintrust_api/types/shared/env_var.py">EnvVar</a></code>
- <code title="patch /v1/env_var/{env_var_id}">client.env_vars.<a href="./src/braintrust_api/resources/env_vars.py">update</a>(env_var_id, \*\*<a href="src/braintrust_api/types/env_var_update_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/env_var.py">EnvVar</a></code>
- <code title="get /v1/env_var">client.env_vars.<a href="./src/braintrust_api/resources/env_vars.py">list</a>(\*\*<a href="src/braintrust_api/types/env_var_list_params.py">params</a>) -> <a href="./src/braintrust_api/types/env_var_list_response.py">EnvVarListResponse</a></code>
- <code title="delete /v1/env_var/{env_var_id}">client.env_vars.<a href="./src/braintrust_api/resources/env_vars.py">delete</a>(env_var_id) -> <a href="./src/braintrust_api/types/shared/env_var.py">EnvVar</a></code>
- <code title="put /v1/env_var">client.env_vars.<a href="./src/braintrust_api/resources/env_vars.py">replace</a>(\*\*<a href="src/braintrust_api/types/env_var_replace_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/env_var.py">EnvVar</a></code>

# Evals

Methods:

- <code title="post /v1/eval">client.evals.<a href="./src/braintrust_api/resources/evals.py">create</a>(\*\*<a href="src/braintrust_api/types/eval_create_params.py">params</a>) -> <a href="./src/braintrust_api/types/shared/summarize_experiment_response.py">SummarizeExperimentResponse</a></code>
