import time
import threading

class Timer(threading.Thread):
    def __init__(self, segundos):
        self.runTime = segundos
        threading.Thread.__init__(self)
    def run(self):
        time.sleep(self.runTime)
        print ("Executado!")

t = Timer(10)
t.start()