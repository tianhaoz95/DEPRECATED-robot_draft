from WallE.API.RobotAPI import RobotAPI

class HalAPI(RobotAPI):
    def start(self):
        print('hal is starting')

    def shutdown(self):
        print('hal is shutdown')
