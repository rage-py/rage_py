# from .util.hello import returnHello
import time
import threading
import sys

def greet():
  # greetMsg = returnHello()
  time.sleep(5)
  print("Hello world by Python 🐍")

loopActive = False

def runLoop():
  global loopActive
  loopActive = True
  index = 0
  while loopActive:
    time.sleep(3)
    print(f"[{index}]")
    index += 1

loopThread = threading.Thread(target=runLoop, args=())

def main():
  global loopActive 
  loopThread.start()
  greet()

  try:
    while True:
      pass
  except KeyboardInterrupt:
    loopActive = False
    loopThread.join()
    sys.exit(0)
    
  

if __name__ == '__main__':
  main()