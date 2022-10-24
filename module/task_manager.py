from objects.task import Task


class TaskManager:

    def __init__(self):
        self.tasks_list = []

    def add(self, new_task: Task) -> bool:
        self.tasks_list.append(new_task)
        return True

    def delete(self, name_task: str) -> bool:
        i = self.check_name(name_task)
        if i == -1:
            return False
        else:
            self.tasks_list.remove(self.tasks_list[i])
            return True

    def check_name(self, name_task: str) -> int:  # Restituisce l'indice (se esiste) di un Task con un certo nome
        for i in range(0, len(self.tasks_list)):
            if self.tasks_list[i].get_name() == name_task:
                return i

        return -1

    def visualize(self) -> str:
        output = '[ '
        for t in self.tasks_list:
            output += t.to_string()

        output += ' ]'
        return output

    def change_status(self, name_task: str, new_status: str) -> bool:
        i = self.check_name(name_task)
        if i == -1:
            return False

        if new_status == 'DONE' or new_status == 'TODO' or new_status == 'DOING' or new_status == 'WONTDO':
            self.tasks_list[i].set_status(new_status=new_status)
            return True
