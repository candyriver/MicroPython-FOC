class BLDCDriver：
        ### Initialise hardware ##
        def init():
            pass
        ### Enable hardware ##
        def enable():
            pass
        ### Disable hardware ##
        def disable():
            pass
        def __init__(self):
            self.pwm_frequency=15000 ##!< pwm frequency value in hertz
            self.voltage_power_supply=12  ##!< power supply voltage
            self.voltage_limit=3.5  ##!< limiting voltage set to the motor   
            self.dc_a=0  ##!< currently set duty cycle on phaseA
            self.dc_b=0  ##!< currently set duty cycle on phaseB
            self.dc_c=0  ##!< currently set duty cycle on phaseC
            self.initialized = False  ## true if driver was successfully initialized
            self.params = 0  ## pointer to hardware specific parameters of driver
        ###
         # Set phase voltages to the harware
         #
         # @param Ua - phase A voltage
         # @param Ub - phase B voltage
         # @param Uc - phase C voltage
        ##
        def setPwm(self,Ua,Ub,Uc):
            pass

        ###
         # Set phase state, enable#disable
         #
         # @param sc - phase A state : active # disabled ( high impedance )
         # @param sb - phase B state : active # disabled ( high impedance )
         # @param sa - phase C state : active # disabled ( high impedance )
        ##
        def setPhaseState(sa,sb,sc):
            pass