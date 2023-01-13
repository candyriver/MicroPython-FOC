from BLDCDriver import *
from foc_utils import *

###
 #  Current sensing abstract class defintion
 # Each current sensoring implementation needs to extend this interface
 ##
class CurrentSense:
    ###
     #  Function intialising the CurrentSense class
     #   - All the necessary intialisations of adc and sync should be implemented here
     #   
     # @returns -  0 - for failure &  1 - for success 
     ##
    def init():
        pass
    
    ###
     # Linking the current sense with the motor driver
     # Only necessary if synchronisation in between the two is required
     ##
    def linkDriver(_driver):
        driver = _driver


    ## variables
    skip_align = False ##!< variable signaling that the phase current direction should be verified during initFOC()
    driver = BLDCDriver() ##!< driver link
    initialized = False ## true if current sense was successfully initialized   
    params = 0 ##!< pointer to hardware specific parameters of current sensing
    
    ###
     # Function intended to verify if:
     #   - phase current are oriented properly 
     #   - if their order is the same as driver phases
     # 
     # This function corrects the alignment errors if possible ans if no such thing is needed it can be left empty (return 1)
     # @returns -  0 - for failure &  positive number (with status) - for success 
     ##
    def driverAlign( align_voltage):
        pass

    ###
     #  Function rading the phase currents a, b and c
     #   This function will be used with the foc control throught the function 
     #   CurrentSense::getFOCCurrents(electrical_angle)
     #   - it returns current c equal to 0 if only two phase measurements available
     # 
     #  @return PhaseCurrent_s current values
     ##
    def getPhaseCurrents():
        pass
    ###
     # Function reading the magnitude of the current set to the motor
     #  It returns the abosolute or signed magnitude if possible
     #  It can receive the motor electrical angle to help with calculation
     #  This function is used with the current control  (not foc)
     #  
     # @param angle_el - electrical angle of the motor (optional) 
     ##
     # get current magnitude 
    #   - absolute  - if no electrical_angle provided 
    #   - signed    - if angle provided

    def getDCCurrent(motor_electrical_angle = 0):
        # read current phase currents
        current = getPhaseCurrents()
        # currnet sign - if motor angle not provided the magnitude is always positive
        sign = 1
        # calculate clarke transform
        i_alpha=0
        i_beta=0
        if current.c==0:
            # if only two measured currents
            i_alpha = current.a  
            i_beta = _1_SQRT3 * current.a + _2_SQRT3 * current.b
        if current.a==0:
            # if only two measured currents
            a = -current.c - current.b
            i_alpha = a  
            i_beta = _1_SQRT3 * a + _2_SQRT3 * current.b
        if current.b==0:
            # if only two measured currents
            b = -current.a - current.c
            i_alpha = current.a  
            i_beta = _1_SQRT3 * current.a + _2_SQRT3 * b
        else:
            # signal filtering using identity a + b + c = 0. Assumes measurement error is normally distributed.
            mid = (1.0/3) * (current.a + current.b + current.c)
            a = current.a - mid
            b = current.b - mid
            i_alpha = a
            i_beta = _1_SQRT3 * a + _2_SQRT3 * b
        

        # if motor angle provided function returns signed value of the current
        # determine the sign of the current
        # sign(atan2(current.q, current.d)) is the same as c.q > 0 ? 1 : -1  
        if motor_electrical_angle==1:
            if (i_beta * _cos(motor_electrical_angle) - i_alpha*_sin(motor_electrical_angle)) > 0:
                sign=1
            else:
                sign=-1
        # return current magnitude
        return sign*_sqrt(i_alpha*i_alpha + i_beta*i_beta)
            

    ###
     # Function used for FOC contorl, it reads the DQ currents of the motor 
     #   It uses the function getPhaseCurrents internally
     # 
     # @param angle_el - motor electrical angle
     ##
     
    # function used with the foc algorihtm
    #   calculating DQ currents from phase currents
    #   - function calculating park and clarke transform of the phase currents 
    #   - using getPhaseCurrents internally

    def getFOCCurrents( angle_el):
          # read current phase currents
        current = getPhaseCurrents()
        # calculate clarke transform
        i_alpha=0.0
        i_beta=0.0
        if current.c==0:
            # if only two measured currents
            i_alpha = current.a  
            i_beta = _1_SQRT3 * current.a + _2_SQRT3 * current.b
        if current.a==0
            # if only two measured currents
            a = -current.c - current.b
            i_alpha = a  
            i_beta = _1_SQRT3 * a + _2_SQRT3 * current.b
        if current.b==0
            # if only two measured currents
            b = -current.a - current.c
            i_alpha = current.a  
            i_beta = _1_SQRT3 * current.a + _2_SQRT3 * b
        else:
            # signal filtering using identity a + b + c = 0. Assumes measurement error is normally distributed.
            mid = (1.f/3) * (current.a + current.b + current.c)
            a = current.a - mid
            b = current.b - mid
            i_alpha = a
            i_beta = _1_SQRT3 * a + _2_SQRT3 * b
        
        # calculate park transform
        ct = _cos(angle_el)
        st = _sin(angle_el)
        return_current=DQCurrent_s()
        return_current.d = i_alpha * ct + i_beta * st
        return_current.q = i_beta * ct - i_alpha * st
        return return_current
            
        
        

