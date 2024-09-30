# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.prompt_data import PromptData

__all__ = [
    "EvalCreateParams",
    "Data",
    "DataDatasetID",
    "DataProjectDatasetName",
    "Score",
    "ScoreFunctionID",
    "ScoreProjectSlug",
    "ScoreGlobalFunction",
    "ScorePromptSessionID",
    "ScoreInlineCode",
    "ScoreInlineCodeInlineContext",
    "ScoreInlinePrompt",
    "Task",
    "TaskFunctionID",
    "TaskProjectSlug",
    "TaskGlobalFunction",
    "TaskPromptSessionID",
    "TaskInlineCode",
    "TaskInlineCodeInlineContext",
    "TaskInlinePrompt",
]


class EvalCreateParams(TypedDict, total=False):
    data: Required[Data]
    """The dataset to use"""

    project_id: Required[str]
    """Unique identifier for the project to run the eval in"""

    scores: Required[Iterable[Score]]
    """The functions to score the eval on"""

    task: Required[Task]
    """The function to evaluate"""

    experiment_name: str
    """An optional name for the experiment created by this eval.

    If it conflicts with an existing experiment, it will be suffixed with a unique
    identifier.
    """

    metadata: Dict[str, Optional[object]]
    """Optional experiment-level metadata to store about the evaluation.

    You can later use this to slice & dice across experiments.
    """

    stream: bool
    """Whether to stream the results of the eval.

    If true, the request will return two events: one to indicate the experiment has
    started, and another upon completion. If false, the request will return the
    evaluation's summary upon completion.
    """


class DataDatasetID(TypedDict, total=False):
    dataset_id: Required[str]


class DataProjectDatasetName(TypedDict, total=False):
    dataset_name: Required[str]

    project_name: Required[str]


Data: TypeAlias = Union[DataDatasetID, DataProjectDatasetName]


class ScoreFunctionID(TypedDict, total=False):
    function_id: Required[str]
    """The ID of the function"""

    version: str
    """The version of the function"""


class ScoreProjectSlug(TypedDict, total=False):
    project_name: Required[str]
    """The name of the project containing the function"""

    slug: Required[str]
    """The slug of the function"""

    version: str
    """The version of the function"""


class ScoreGlobalFunction(TypedDict, total=False):
    global_function: Required[str]
    """The name of the global function.

    Currently, the global namespace includes the functions in autoevals
    """


class ScorePromptSessionID(TypedDict, total=False):
    prompt_session_function_id: Required[str]
    """The ID of the function in the prompt session"""

    prompt_session_id: Required[str]
    """The ID of the prompt session"""

    version: str
    """The version of the function"""


class ScoreInlineCodeInlineContext(TypedDict, total=False):
    runtime: Required[Literal["node", "python"]]

    version: Required[str]


class ScoreInlineCode(TypedDict, total=False):
    code: Required[str]
    """The inline code to execute"""

    inline_context: Required[ScoreInlineCodeInlineContext]

    name: Optional[str]
    """The name of the inline code function"""


class ScoreInlinePrompt(TypedDict, total=False):
    inline_prompt: Required[Optional[PromptData]]
    """The prompt, model, and its parameters"""

    name: Optional[str]
    """The name of the inline prompt"""


Score: TypeAlias = Union[
    ScoreFunctionID, ScoreProjectSlug, ScoreGlobalFunction, ScorePromptSessionID, ScoreInlineCode, ScoreInlinePrompt
]


class TaskFunctionID(TypedDict, total=False):
    function_id: Required[str]
    """The ID of the function"""

    version: str
    """The version of the function"""


class TaskProjectSlug(TypedDict, total=False):
    project_name: Required[str]
    """The name of the project containing the function"""

    slug: Required[str]
    """The slug of the function"""

    version: str
    """The version of the function"""


class TaskGlobalFunction(TypedDict, total=False):
    global_function: Required[str]
    """The name of the global function.

    Currently, the global namespace includes the functions in autoevals
    """


class TaskPromptSessionID(TypedDict, total=False):
    prompt_session_function_id: Required[str]
    """The ID of the function in the prompt session"""

    prompt_session_id: Required[str]
    """The ID of the prompt session"""

    version: str
    """The version of the function"""


class TaskInlineCodeInlineContext(TypedDict, total=False):
    runtime: Required[Literal["node", "python"]]

    version: Required[str]


class TaskInlineCode(TypedDict, total=False):
    code: Required[str]
    """The inline code to execute"""

    inline_context: Required[TaskInlineCodeInlineContext]

    name: Optional[str]
    """The name of the inline code function"""


class TaskInlinePrompt(TypedDict, total=False):
    inline_prompt: Required[Optional[PromptData]]
    """The prompt, model, and its parameters"""

    name: Optional[str]
    """The name of the inline prompt"""


Task: TypeAlias = Union[
    TaskFunctionID, TaskProjectSlug, TaskGlobalFunction, TaskPromptSessionID, TaskInlineCode, TaskInlinePrompt
]
