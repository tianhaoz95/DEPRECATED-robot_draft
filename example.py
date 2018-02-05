from WallE.Robot.Robot import Robot
from WallE.Task.Routine import SimpleRoutine

robot = Robot('local', {'module_name': 'hal', 'class_name': 'HalAPI'})
routine = SimpleRoutine()
routine.add(robot, {'module_name':'tasks.example_task', 'class_name':'MoveTask'})
robot.clean_cache()
robot.start()
routine.run()
robot.shutdown()
