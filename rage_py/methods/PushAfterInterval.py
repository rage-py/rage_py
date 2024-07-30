import time

class PushAfterInterval():
    def __init__(self):
        self.loopActive = False

    def start(self):
        self.loopActive = True
    
        index = 0
        while self.loopActive:
            time.sleep(3)
            print(f"[{index}]")
            index += 1

    def stop(self):
        self.loopActive = False
        return