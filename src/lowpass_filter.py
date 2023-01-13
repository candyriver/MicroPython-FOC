
from foc_utils import *
import time
###
 #  Low pass filter class
 ##
class LowPassFilter:
    ###
     # @param Tf - Low pass filter time constant
     ##
    def __init__(self,time_constant):
        self.Tf= time_constant##!< Low pass filter time constant
        self.timestamp_prev=time.time_ns()  ##!< Last execution timestamp
        self.y_prev=0.0 ##!< filtered value in previous execution step
    def func(self,x):
        timestamp = time.time_ns()
        dt = (timestamp - self.timestamp_prev)*1e-9
        if dt < 0.0 :
            dt = 1e-3
        else if dt > 0.3:
            self.y_prev = x
            self.timestamp_prev = timestamp
            return x
        alpha = self.Tf/(self.Tf + dt)
        y = alpha*self.y_prev + (1.0 - alpha)*x
        self.y_prev = y
        self.timestamp_prev = timestamp
        return y
