import motors
import time

motors.Forwards()
time.sleep(1) # Pause for 1 second
motors.Left()
time.sleep(0.5) # Pause for half a second
motors.Forwards()
time.sleep(1)
motors.Right()
time.sleep(0.5)
motors.Backwards()
time.sleep(0.5)
motors.StopMotors()
