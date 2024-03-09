from zrb import StrInput, Task, python_task, runner
from zrb.helper.python_task import show_lines

from _automate.noto.log._group import LOG_GROUP
from _automate.noto.log._helper import append_log, get_log, get_log_file_name


@python_task(
    name="add",
    group=LOG_GROUP,
    inputs=[
        StrInput(
            name="text",
            prompt="Text",
            default="",
        ),
    ],
)
def add(*args, **kwargs):
    task: Task = kwargs.get("_task")
    text = kwargs.get("text")
    append_log(text)
    file_name = get_log_file_name()
    log_str = get_log(file_name)
    logs = log_str.split("\n")
    show_lines(task, *logs)


runner.register(add)
