from abc import ABC, abstractmethod

class RobotAPI(ABC):
    
    @abstractmethod
    def start():
        pass

    @abstractmethod
    def shutdown():
        pass
