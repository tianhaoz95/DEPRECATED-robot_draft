from WallE.Robot.Robot import Robot

robot = Robot('local', {'module_name': 'hal', 'class_name': 'HalAPI'})

robot.clean_cache()

robot.start()

for i in range(10):
    robot.move()

robot.shutdown()
