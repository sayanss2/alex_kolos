import sys
import time
import threading
from ns4help import *

class Model:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        
    def run(self, t_run: int):
        try:
            t_model = ModelFunc(self.func, *self.args, **self.kwargs)
            t_htime = ModelTimeHandler(t_run)
            if checksyn(*sys.argv):
                t_htime.start()
                t_model.start()
            else:
                gethelp(*sys.argv, **self.kwargs)
        except IndexError as err:
            errreport(err)
    
class ModelFunc(threading.Thread):
    tRun = None
    event = False
    errorEvent = True
    def __init__(self, func, *args, **kwargs):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        if not ModelFunc.errorEvent:
#            l_time = ModelFunc.tRun
            s_time = time.asctime()
            while not ModelFunc.event:
                l_time = time.asctime()
                self.func(s_time, l_time, *self.args, **self.kwargs)
#                l_time -= 1
        pass

class ModelTimeHandler(threading.Thread):
    def __init__(self, t_run):
        threading.Thread.__init__(self)
        ModelFunc.tRun = t_run

    def run(self):
        ModelFunc.errorEvent = False
        time.sleep(ModelFunc.tRun)
        ModelFunc.event = True
        print('Done!\n')