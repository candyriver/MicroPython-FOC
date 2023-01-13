import time
from MagneticSensorI2C import *
#AS5600 EXAMPLE   
AS5600_I2C=MagneticSensorI2CConfig_s()
sensor = MagneticSensorI2C()
sensor.init_config(AS5600_I2C)
i2c = I2C(0,scl=Pin(18),sda=Pin(19),freq=400000)        
sensor.init(i2c)
print("Sensor ready")
time.sleep(1)
while 1:
    sensor.update()
    #print("angle: ",sensor.getAngle()*360/(2*math.pi),"full_rotations: ",sensor.full_rotations," velocity:",sensor.getVelocity())
    print(sensor.getAngle());
    print(sensor.getVelocity());
