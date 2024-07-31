from .methods.PushAfterInterval import PushAfterInterval
from .util.formatLog import formatLog
import threading

class App():
    def __init__(self, configFilePath: str, logger: bool = False):
        # Public variables 
        self.logger = logger
        self.configFilePath = configFilePath
        # Private variables
        self.__newMethodInstance = PushAfterInterval() 
        self.__loopThread = threading.Thread(target=self.__newMethodInstance.start, args=())
        self.__setup = False

    def start(self):     
        try:
            if self.__setup is False:
                ...
            
            self.__loopThread.start()
        except:
            formatLog("Unexpected error occurred!", "error", self.logger)

    def returnLoopactive(self):
        return self.loopActive
    
    def stop(self):
        self.__newMethodInstance.stop()
        self.__loopThread.join()
        formatLog("Application terminated successfully", "final", self.logger)
        return

if __name__ == '__main__':
    app = App()
    app.main()