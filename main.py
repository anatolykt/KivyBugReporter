import kivy
kivy.require("1.10.0")

from kivy.app import App
from bugreporter import BugReporter


class Test(App):
	def build(self):
		return BugReporter()


if __name__ == "__main__":

	# Sizes of the screens (DPI) of different devices
	# It is just an imitation. The actual form of application
	# can be achived by emulation of virtual devices or 
	# by checking on real-world devices

	ALLOWED_DEVICES = {
		"iPhone X": {
			"width": 375,
			"height": 812
		}
		"iPhone 6": {
			"width": 375,
			"height": 667
		},
		"iPhone SE": {
			"width": 320,
			"height": 568
		},
		"iPhone 7 Plus": {
			"width": 414,
			"height": 736
		},
		"iPad Pro 10.5-inch": {
			"width": 1112,
			"height": 834
		},
		"iPad Pro (9.7-inch)": {
			"width": 768,
			"height": 1024
		}
		"iPad Pro (12.9-inch)": {
			"width": 1024,
			"height": 1366
		},
	}

	# Append devices with the similar screen sizes.
	ALLOWED_DEVICES["iPhone 8"] = ALLOWED_DEVICES["iPhone 6"]
	ALLOWED_DEVICES["iPhone 7"] = ALLOWED_DEVICES["iPhone 6"]
	ALLOWED_DEVICES["iPhone 6 s"] = ALLOWED_DEVICES["iPhone 6"]
	ALLOWED_DEVICES["iPhone 6 Plus"] = ALLOWED_DEVICES["iPhone 6"]
	ALLOWED_DEVICES["iPhone 6s Plus"] = ALLOWED_DEVICES["iPhone 6"]
	ALLOWED_DEVICES["iPhone 8 Plus"] = ALLOWED_DEVICES["iPhone 7 Plus"]
	ALLOWED_DEVICES["iPad Air 2"] = ALLOWED_DEVICES["iPad Pro (9.7-inch)"]
	ALLOWED_DEVICES["iPad Mini 4"] = ALLOWED_DEVICES["iPad Pro (9.7-inch)"]
	ALLOWED_DEVICES["iPad Pro 12.9-inch (2nd generation)"] = \
		ALLOWED_DEVICES["iPad Pro (12.9-inch)"]

	WIDTH = None
	HEIGHT = None

	import os

	# There are several ways to set custom size of window.
	# To set window size appropriate to screen size of concrete device
	# set envirov variable DEVICE to one from ALLOWED_DEVICES
	# Other way is to set width and height of window separately by
	# setting environ variables WINDOW_WIDTH and WINDOW_HEIGHT

	DEVICE = os.getenv("DEVICE")
	WINDOW_WIDTH = os.getenv("WINDOW_WIDTH")
	WINDOW_HEIGHT = os.getenv("WINDOW_HEIGHT")

	if DEVICE and DEVICE in ALLOWED_DEVICES.keys():
		WIDTH = ALLOWED_DEVICES[DEVICE]["width"]
		HEIGHT = ALLOWED_DEVICES[DEVICE]["height"]

	if not (WIDTH and HEIGHT) and (WINDOW_WIDTH and WINDOW_HEIGHT):
		WIDTH = WINDOW_WIDTH
		HEIGHT = WINDOW_HEIGHT

	if not (WIDTH and HEIGHT):
		DEFAULT_DEVICE = "iPhone 6"
		WIDTH = ALLOWED_DEVICES[DEFAULT_DEVICE]["width"]
		HEIGHT = ALLOWED_DEVICES[DEFAULT_DEVICE]["height"]

	from kivy.core.window import Window
	Window.size = (WIDTH, HEIGHT)

	# There are several ways of errors handling
	# you can store error`s tracebacks in file
	# or just print it to the stdout.
	# To set custom absolute way to error log
	# set environ variable ERROR_LOG_ABS.
	# To set only custom path but not the file name
	# set environ variable ERROR_LOG_PATH.
	# To set only custom file name but not the path
	# set environ variable ERROR_LOG_FILE.
	# You can disable storing error log by
	# setting eviron variable DO_NOT_STORE_ERRORS to any value

	ERROR_LOG_ABS = os.getenv("ERROR_LOG_ABS")
	ERROR_LOG_PATH = os.getenv("ERROR_LOG_PATH")
	ERROR_LOG_FILE = os.getenv("ERROR_LOG_FILE")
	DO_NOT_STORE_ERRORS = os.getenv("DO_NOT_STORE_ERRORS")

	DEFAULT_ERROR_LOG_FILE = "error.log"
	DEFAULT_ERROR_LOG_PATH = "./"

 	ERROR_LOG = None

	if ERROR_LOG_ABS:
		ERROR_LOG = ERROR_LOG_ABS

	if not ERROR_LOG:
		if ERROR_LOG_PATH and ERROR_LOG_FILE:
			ERROR_LOG = ERROR_LOG_PATH + ERROR_LOG_FILE
		elif ERROR_LOG_PATH:
			ERROR_LOG = ERROR_LOG_PATH + DEFAULT_ERROR_LOG_FILE
		elif ERROR_LOG_FILE:
			ERROR_LOG = DEFAULT_ERROR_LOG_PATH + ERROR_LOG_FILE
		else:
			ERROR_LOG = DEFAULT_ERROR_LOG_PATH + DEFAULT_ERROR_LOG_FILE

	import traceback

	try:
		Test().run()
	except Exception as exc:
		print(exc)
		if not DO_NOT_STORE_ERRORS:
			traceback.print_exc(file=open(ERROR_LOG, "w"))