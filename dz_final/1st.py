class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(", ".join(self.items))

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()


class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        tasks = ""
        for key in sorted(self.task.keys()):
            tasks += f"{key} {self.task[key]} \n"
        return tasks

    def new_task(self, task, priority):
        if priority not in self.task.keys():
            self.task[priority] = Stack()
            self.task[priority].push(task)
        else:
            new_stack = Stack()
            while len(str(self.task[priority])) != 0:
                value = self.task[priority].pop()
                if value != task:
                    new_stack.push(value)
            new_stack.push(task)
            self.task[priority] = new_stack


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)

print(manager)
