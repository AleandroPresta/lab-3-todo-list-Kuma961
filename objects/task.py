from datetime import date

from .project import Project


class Task:

    def __init__(self, name: str, tags: list, project: Project, deadline: date):
        self.name = name
        self.tags = tags
        self.project = project
        self.deadline = deadline
        self.status = 'TODO'

    def get_name(self):
        return self.name

    def to_string(self):
        output = 'Task ' + self.name + '\nTags ' + str(self.tags) + '\nProject ' + self.project.name + '\nDeadline ' + \
                 str(self.deadline.day) + '/' + str(self.deadline.month) + '/' + str(self.deadline.year) + '\nStatus ' + self.status

        return output

    def set_status(self, new_status: str):
        self.status = new_status
