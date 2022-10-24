import pytest
from objects.task import Task
from objects.project import Project
from datetime import date
from module.task_manager import TaskManager


@pytest.fixture(scope='module', name='tm')
def fixture_tm():
    new_task = Task(
        name='t1',
        tags=['Android', 'Java'],
        project=Project('App Android'),
        deadline=date(2020, 12, 25)
    )

    task_manager = TaskManager()
    task_manager.add(new_task)
    yield task_manager
