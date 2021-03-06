
#module load
import RPi.GPIO as GPIO
import time

#sensor pin variable
PIR_PIN = 4 #BCM

##init fn
def sensorInit():
	#warning useless things remove(option)
	GPIO.setwarnings(False)

	#GPIO pin naming setting
	GPIO.setmode(GPIO.BCM)

	#sensor connect pin active mode setting
	GPIO.setup(PIR_PIN, GPIO.IN)
	
	print("init OK")

#init function will be cover them all

def controlPIR():
	return GPIO.input(PIR_PIN)


#buzzer ctrl
cnt = 0

sensorInit()
try:
    while True:
        time.sleep(0.5)
        human = controlPIR()
        if human == 1:
            print("detected!")
        #print(f"if PIR is {controlPIR()}")
        #time.sleep(0.1)
        #cnt = cnt + 1
        #if cnt > 100:
        #	break
        
except KeyboardInterrupt:
    print('stop')
finally:
    PWM_PBUZ.stop()
    GPIO.cleanup()
    print('end')

