# Servo Control
import os

__min_value__ = 50
__max_value__ = 250
current_value = 0

def __setValue__(val):
	if int(val) >= __min_value__ and int(val) <= __max_value__:
		cmd = "echo 0=" + str(int(val)) + " > /dev/servoblaster"
		cmd_result = os.system(cmd)
		print("result : " + str(cmd_result))
		if cmd_result == 0:
			global current_value
			current_value = int(val)
			print("current value : " + str(current_value))

def increase():
	__setValue__(current_value + 1)
	print("increased to " + str(current_value))

def decrease():
	__setValue__(current_value - 1)
	print("decreased to " + str(current_value))

def __main__():
	__setValue__(__min_value__)
	while(1):
		line = input("Enter a value: ")
		if line:
			__setValue__(str(int(line)))
		else:
			break

if __name__ == "__main__":
	__main__()
