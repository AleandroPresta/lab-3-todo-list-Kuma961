from module.task_manager import TaskManager
from objects.task import Task
from datetime import date
from objects.project import Project


class TestCreation:

    def test_dummy(self):
        assert True

    def test_creation(self):  # Acceptance test
        # Given il sistema è in idle e aspetta un comando utente
        tm = TaskManager()
        p = Project(name='AnlisiImmagini')

        # When l'utente crea un task e lo aggiunge alla to-do list

        new_task = Task(
            name='task-1',
            tags=['Python', 'MachineLearning'],
            project=p,
            deadline=date(2022, 10, 25))
        # Then il task è aggiunto correttamente
        assert tm.add(new_task)  # Restituisce True se l'aggiunta è andata a buon fine
