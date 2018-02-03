from WallE.Robot.Robot import Robot

robot = Robot('local', {'file_path': 'hal', 'class_name': 'HalAPI'})

robot.start()

robot.shutdown()
