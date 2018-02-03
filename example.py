from WallE.Robot.Robot import Robot

robot = Robot('local', {'module_name': 'hal', 'class_name': 'HalAPI'})

robot.start()

robot.shutdown()
