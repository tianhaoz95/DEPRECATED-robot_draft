from abc import ABC, abstractmethod
from .util import *

class Routine(ABC):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def run(self):
        pass

class SimpleRoutine(Routine):

    def __init__(self):
        self.tasks = []

    def load_task(self, robot, module_name, class_name):
        # task = load_local_task_module(robot, module_name, class_name)
        url = 'https://github.com/tianhaoz95/robot_draft/archive/master.zip'
        task = load_remote_task_module(robot, module_name, class_name, url)
        return task

    def add(self, robot, task_meta):
        module_name = task_meta['module_name']
        class_name = task_meta['class_name']
        task = self.load_task(robot, module_name, class_name)
        self.tasks.append(task)

    def run(self):
        for task in self.tasks:
            task.setup()
            task.run()
        print('All tasks done')
