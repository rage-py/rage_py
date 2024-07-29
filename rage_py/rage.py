from .methods.PushAfterInterval import PushAfterInterval
import time
import threading

class App():
    def __init__(self):
        self.loopActive = False
        # Private variable
        self.__loopThread = threading.Thread(target=self.runLoop, args=())

    def runLoop(self):
        self.loopActive = True
    
        index = 0
        while self.loopActive:
            time.sleep(3)
            print(f"[{index}]")
            index += 1


    def main(self):     
        self.__loopThread.start()
        newInstance = PushAfterInterval()
        newInstance.sayHello()

    def returnLoopactive(self):
        return self.loopActive
    
    def stop(self):
        self.loopActive = False
        self.__loopThread.join()
        return

if __name__ == '__main__':
    app = App()
    app.main()