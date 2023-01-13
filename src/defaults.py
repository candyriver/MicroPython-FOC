# default configuration values
# change this file to optimal values for your application

DEF_POWER_SUPPLY= 12.0 #!< default power supply voltage
# velocity PI controller params
DEF_PID_VEL_P= 0.5 #!< default PID controller P value
DEF_PID_VEL_I= 10.0 #!<  default PID controller I value
DEF_PID_VEL_D= 0.0 #!<  default PID controller D value
DEF_PID_VEL_RAMP= 1000.0 #!< default PID controller voltage ramp value
DEF_PID_VEL_LIMIT (DEF_POWER_SUPPLY) #!< default PID controller voltage limit


# for stm32, due, teensy, esp32 and similar
DEF_PID_CURR_P= 3 #!< default PID controller P value
DEF_PID_CURR_I= 300.0 #!<  default PID controller I value
DEF_PID_CURR_D= 0.0 #!<  default PID controller D value
DEF_PID_CURR_RAMP= 0  #!< default PID controller voltage ramp value
DEF_PID_CURR_LIMIT= (DEF_POWER_SUPPLY) #!< default PID controller voltage limit
DEF_CURR_FILTER_Tf= 0.005 #!< default currnet filter time constant
#endif
# default current limit values
DEF_CURRENT_LIM= 2.0 #!< 2Amps current limit by default

# default monitor downsample
DEF_MON_DOWNSMAPLE= 100 #!< default monitor downsample
DEF_MOTION_DOWNSMAPLE= 0 #!< default motion downsample - disable

# angle P params
DEF_P_ANGLE_P= 20.0 #!< default P controller P value
DEF_VEL_LIM= 20.0 #!< angle velocity limit default

# index search
DEF_INDEX_SEARCH_TARGET_VELOCITY=1.0 #!< default index search velocity
# align voltage
DEF_VOLTAGE_SENSOR_ALIGN= 3.0 #!< default voltage for sensor and motor zero alignemt
# low pass filter velocity
DEF_VEL_FILTER_Tf= 0.005 #!< default velocity filter time constant

# current sense default parameters
DEF_LPF_PER_PHASE_CURRENT_SENSE_Tf= 0.0  #!< default currnet sense per phase low pass filter time constant 