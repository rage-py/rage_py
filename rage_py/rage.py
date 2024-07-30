from .methods.PushAfterInterval import PushAfterInterval
import threading

class App():
    def __init__(self):
        # Private variables
        self.__newMethodInstance = PushAfterInterval() 
        self.__loopThread = threading.Thread(target=self.__newMethodInstance.start, args=())

    def main(self):     
        self.__loopThread.start()

    def returnLoopactive(self):
        return self.loopActive
    
    def stop(self):
        print("Application will terminate in few seconds")
        self.__newMethodInstance.stop()
        self.__loopThread.join()
        print("Application terminated successfully")
        return

if __name__ == '__main__':
    app = App()
    app.main()