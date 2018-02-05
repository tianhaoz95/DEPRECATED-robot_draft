from WallE.API.RobotAPI import RobotAPI
import numpy as np
from multiprocessing import Process, Queue
from time import sleep

class HalAPI(RobotAPI):
    def __init__(self):
        self.status = 'idle'
        self.safe_q = Queue(maxsize=3)
        self.safety_check_process = Process(target=self.run_safety_check, args=(self.safe_q,))

    def start(self):
        if self.status == 'idle':
            print('Starting Hal ...')
            self.status = 'running'
            self.safety_check_process.start()
        else:
            print('Hal has already started')

    def shutdown(self):
        if self.status == 'running':
            print('Shutting down Hal ...')
            self.status = 'idle'
            self.safety_check_process.terminate()
        else:
            print('Hal is not running')

    def is_safe(self):
        safe = False
        while not self.safe_q.empty():
            safe = self.safe_q.get()
        return safe

    def move(self):
        safe_snap = self.is_safe()
        if safe_snap:
            print('Safe, moving')
        else:
            print('Not safe, stop')
        sleep(1)

    def run_safety_check(self, safe_q):
        while True:
            num = np.random.randint(0, 100)
            safe = True
            if num <= 20:
                safe = False
            safe_q.put(safe)
            sleep(0.1)
