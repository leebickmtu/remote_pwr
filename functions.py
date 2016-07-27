import RPi.GPIO as GPIO
import time

pins = {'pwr':11, 'rst':12, 'led':7}

def hold(button):
	pin = (pins[button])

	try:
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin, GPIO.OUT)

		GPIO.output(pin, True)
		time.sleep(5)
		GPIO.output(pin, False)

	finally:
		GPIO.cleanup()

def pulse(button):
	pin = (pins[button])

	try:
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin, GPIO.OUT)

		GPIO.output(pin, True)
		time.sleep(.1)
		GPIO.output(pin, False)

	finally:
		GPIO.cleanup()

def pwr_state():
	pin = (pins['led'])

	try:
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
		class Counter(object):
			def __init__(self, start=0):
				self.x = start
			def __call__(self, channel):
				self.x += 1
				return self.x
		
		count = Counter()
		
		GPIO.add_event_detect(pin, GPIO.RISING)
		GPIO.add_event_callback(pin, count)
		
		time.sleep(1.2)
		GPIO.remove_event_detect(pin)
		
		if (count.x > 0):
			print "sleep"
		elif (GPIO.input(pin)):
			print "on"
		else:
			print "off"
	
	finally:
		GPIO.cleanup()

