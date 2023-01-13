import math
# int array instead of float array
# 4x200 points per 360 deg
# 2x storage save (int 2Byte float 4 Byte )
# sin*10000
sine_array =[0,79,158,237,316,395,473,552,631,710,789,867,946,1024,1103,1181,1260,1338,1416,1494,1572,1650,1728,1806,1883,1961,2038,2115,2192,2269,2346,2423,2499,2575,2652,2728,2804,2879,2955,3030,3105,3180,3255,3329,3404,3478,3552,3625,3699,3772,3845,3918,3990,4063,4135,4206,4278,4349,4420,4491,4561,4631,4701,4770,4840,4909,4977,5046,5113,5181,5249,5316,5382,5449,5515,5580,5646,5711,5775,5839,5903,5967,6030,6093,6155,6217,6279,6340,6401,6461,6521,6581,6640,6699,6758,6815,6873,6930,6987,7043,7099,7154,7209,7264,7318,7371,7424,7477,7529,7581,7632,7683,7733,7783,7832,7881,7930,7977,8025,8072,8118,8164,8209,8254,8298,8342,8385,8428,8470,8512,8553,8594,8634,8673,8712,8751,8789,8826,8863,8899,8935,8970,9005,9039,9072,9105,9138,9169,9201,9231,9261,9291,9320,9348,9376,9403,9429,9455,9481,9506,9530,9554,9577,9599,9621,9642,9663,9683,9702,9721,9739,9757,9774,9790,9806,9821,9836,9850,9863,9876,9888,9899,9910,9920,9930,9939,9947,9955,9962,9969,9975,9980,9985,9989,9992,9995,9997,9999,10000,10000]

# utility defines
_2_SQRT3=1.15470053838
_SQRT3=1.73205080757
_1_SQRT3=0.57735026919
_SQRT3_2=0.86602540378
_SQRT2=1.41421356237
_120_D2R= 2.09439510239
_PI= 3.14159265359
_PI_2= 1.57079632679
_PI_3= 1.0471975512
_2PI= 6.28318530718
_3PI_2= 4.71238898038
_PI_6= 0.52359877559
_RPM_TO_RADS= 0.10471975512

NOT_SET= -12345.0
_HIGH_IMPEDANCE= 0
_HIGH_Z= _HIGH_IMPEDANCE
_ACTIVE=1
_NC= (NOT_SET)


# sign function
def _sign(a):
    if a<0:
        return -1
    return (a)>0
def _round(x):
    if x>=0:
        return int(x+0.5)
    return int(x-0.5)
def _constrain(amt,low,high):
    if amt<low:
        return low
    if amt>high:
        return high
    return amt
def _sqrt(a):
    return (_sqrtApprox(a))
def _isset(a):
    return ( (a) != (NOT_SET) )
def _UNUSED(v):
    return (v)

# function approximating the sine calculation by using fixed size array
# ~40us (float array)
# ~50us (int array)
# precision +-0.005
# it has to receive an angle in between 0 and 2PI
def _sin(a):  
    if a < _PI_2:
        #return sine_array[(int)(199.0f*( a / (_PI/2.0)))];
        #return sine_array[(int)(126.6873f* a)];           # float array optimized
        return 0.0001*sine_array[_round(126.6873* a)]      # int array optimized
    elif a < _PI:
        # return sine_array[(int)(199.0f*(1.0f - (a-_PI/2.0) / (_PI/2.0)))];
        #return sine_array[398 - (int)(126.6873f*a)];          # float array optimized
        return 0.0001*sine_array[398 - _round(126.6873*a)]     # int array optimized
    elif a < _3PI_2 :
        # return -sine_array[(int)(199.0f*((a - _PI) / (_PI/2.0)))];
        #return -sine_array[-398 + (int)(126.6873f*a)];           # float array optimized
        return -0.0001*sine_array[-398 + _round(126.6873*a)]      # int array optimized
    else:
        # return -sine_array[(int)(199.0f*(1.0f - (a - 3*_PI/2) / (_PI/2.0)))];
        #return -sine_array[796 - (int)(126.6873f*a)];           # float array optimized
        return -0.0001*sine_array[796 - _round(126.6873*a)]      # int array optimized


# function approximating cosine calculation by using fixed size array
# ~55us (float array)
# ~56us (int array)
# precision +-0.005
# it has to receive an angle in between 0 and 2PI
def _cos( a):
    a_sin = a + _PI_2
    if a_sin > _2PI :
        a_sin =a_sin - _2PI        
    return _sin(a_sin)

# normalizing radian angle to [0,2PI]
def _normalizeAngle(angle):
    a = math.fmod(angle, _2PI)
    if a >= 0:
        return a
    return (a + _2PI)


# Electrical angle calculation
def _electricalAngle(shaft_angle, pole_pairs):
    return (shaft_angle * pole_pairs)

# square root approximation function using
# https:#reprap.org/forum/read.php?147,219210
# https:#en.wikipedia.org/wiki/Fast_inverse_square_root
def _sqrtApprox( number) :
    return math.sqrt(number)


# dq current structure
class DQCurrent_s:
    d=0
    q=0
# phase current structure
class PhaseCurrent_s:
    a=0
    b=0
    c=0
# dq voltage structs
class DQVoltage_s:
    d=0
    q=0


