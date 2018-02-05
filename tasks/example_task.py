from WallE.Task.Task import SimpleTask

class MoveTask(SimpleTask):

    def __init__(self, robot):
        super().__init__(robot)

    def setup(self):
        print('Setting up the robot ...')

    def run(self):
        print('Running the task ...')
        for i in range(10):
            self.robot.move()
        print('Task finished')
