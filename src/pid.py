from foc_utils import *
import time
###
 #  PID controller class
 ##
class PIDController:
    ###
     #  
     # @param P - Proportional gain 
     # @param I - Integral gain
     # @param D - Derivative gain 
     # @param ramp - Maximum speed of change of the output value
     # @param limit - Maximum output value
     ##
    def __init__( P,  I,  D,  ramp,  limit):
        self.P=P ##!< Proportional gain 
        self.I=I ##!< Integral gain 
        self.D=D ##!< Derivative gain 
        self.output_ramp=ramp ##!< Maximum speed of change of the output value
        self.limit=limit ##!< Maximum output value
        self.error_prev=0.0 ##!< last tracking error value
        self.output_prev=0.0  ##!< last pid output value
        self.integral_prev=0.0 ##!< last integral component value
        self.timestamp_prev=time.time_ns() ##!< Last execution timestamp
       

    def func(self, error):
        # calculate the time from the last call
        timestamp_now =time.time_ns() 
        Ts = (timestamp_now -self.timestamp_prev) * 1e-9
        # quick fix for strange cases (micros overflow)
        if Ts <= 0 or Ts > 0.5:
           Ts = 1e-3

        # u(s) = (P + I/s + Ds)e(s)
        # Discrete implementations
        # proportional part
        # u_p  = P *e(k)
        proportional = self.P * error
        # Tustin transform of the integral part
        # u_ik = u_ik_1  + I*Ts/2*(ek + ek_1)
        integral = self.integral_prev + self.I*Ts*0.5*(error + self.error_prev)
        # antiwindup - limit the output
        integral = _constrain(integral, -self.limit, self.limit)
        # Discrete derivation
        # u_dk = D(ek - ek_1)/Ts
        derivative = self.D*(error - self.error_prev)/Ts

        # sum all the components
        output = proportional + integral + derivative
        # antiwindup - limit the output variable
        output = _constrain(output, -self.limit, self.limit)

        # if output ramp defined
        if self.output_ramp > 0:
            
            # limit the acceleration by ramping the output
            output_rate = (output - self.output_prev)/Ts
            if  output_rate > self.output_ramp:
                output = self.output_prev + self.output_ramp*Ts
            elif output_rate < -self.output_ramp:
                output = self.output_prev - self.output_ramp*Ts
        
        # saving for the next pass
        self.integral_prev = integral
        self.output_prev = output
        self.error_prev = error
        self.timestamp_prev = timestamp_now
        return output
