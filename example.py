from WallE.Robot.Robot import Robot
from WallE.Task.Routine import SimpleRoutine

robot = Robot('local', {'module_name': 'hal', 'class_name': 'HalAPI'})
routine = SimpleRoutine()
routine.add(robot, 'local', {'module_name':'example_task.task', 'class_name':'MoveTask'})
routine.add(robot, 'remote', {'module_name': 'example_remote_task-master.task', 'class_name': 'MoveTask', 'url': 'https://github.com/tianhaoz95/example_remote_task/archive/master.zip'})
robot.clean_cache()
robot.start()
routine.run()
robot.shutdown()
