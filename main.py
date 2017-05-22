import pygame
import math
from src import motors
#from src import servos
from time import sleep

print('Starting initializing joystick...')
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
print('Joystick initialized : ', j.get_name())

# Returns a vector of the following form:
# [LThumbstickX, LThumbstickY, RThumbstickY
# Left Trigger, Right Trigger, RThumbstickX,
# Button A, Button B, Button X, Button Y, 
# Left Bumper, Right Bumper,
# LThumbstickZ, RThumbstickZ
# Select, Start, Menu]

# Note:
# No D-Pad.
# Triggers are switches, not variable. 
# Your controller may be different

def get():
    out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    it = 0 #iterator
    pygame.event.pump()
    
    #Read input from the two joysticks       
    for i in range(0, j.get_numaxes()):
        out[it] = j.get_axis(i)
        it+=1
    #Read input from buttons
    for i in range(0, j.get_numbuttons()):
        out[it] = j.get_button(i)
        it+=1
    return out

def __main__():
    while True:
        values = get()
        #print(values)
        #continue

        if (values[2] > 0) :
            print("Camera Right")
            servos.increase()
        elif (values[2] < 0) :
            print("Camera Left")
            servos.decrease()


        if (math.fabs(values[1]) > math.fabs(values[0])) :
            if (values[1] > 0) :
                motors.Backwards()
            else :
                motors.Forwards()
        elif (values[0] != 0) :
            if (values[0] > 0) :
                motors.Right()
            elif (values[0] < 0) :
                motors.Left()
        else:
            motors.StopMotors()

        # if (values[0] < 0 or values[5] < 0) :

        # for i in range(len(values)):
        #     if (values[i]) :

        #         case 1:
        #         break

        #     print(i)

        sleep(0.2)


def __main2__():
    while True:
        values = get()
        # print(values)

        if (values[2] > 0) :
            print("Full Backward")
            motors.Backwards(abs(values[2]))
        elif (values[2] < 0) :
            print("Full Forward")
            motors.Forwards(abs(values[2]))

        if (values[5] < 0) :
            print("Full Left")
            motors.Left(abs(values[5]))
        elif (values[5] > 0) :
            print("Full Right")
            motors.Right(abs(values[5]))


        #forward
        # motors.pwmMotorAForwards.ChangeDutyCycle(motors.DutyCycleA * (values[2] if values[2] > 0 else 0))
        # motors.pwmMotorABackwards.ChangeDutyCycle(motors.DutyCycleA * (-values[2] if values[2] < 0 else 0))
        # motors.pwmMotorBForwards.ChangeDutyCycle(motors.DutyCycleB * (values[2] if values[2] > 0 else 0))
        # motors.pwmMotorBBackwards.ChangeDutyCycle(motors.DutyCycleB * (-values[2] if values[2] < 0 else 0))

        #backward
        # pwmMotorAForwards.ChangeDutyCycle(DutyCycleA * coef)
        # pwmMotorABackwards.ChangeDutyCycle(Stop)
        # pwmMotorBForwards.ChangeDutyCycle(DutyCycleB * coef)
        # pwmMotorBBackwards.ChangeDutyCycle(Stop)
        # if (values[5] < 0 and values[2] < 0) :
        #     print("Forward Left")
        #     motors.pwmMotorAForwards.ChangeDutyCycle(motors.Stop)
        #     motors.pwmMotorABackwards.ChangeDutyCycle(motors.DutyCycleA * abs(values[2]) * abs(values[5]))
        #     motors.pwmMotorBForwards.ChangeDutyCycle(motors.Stop)
        #     motors.pwmMotorBBackwards.ChangeDutyCycle(motors.DutyCycleB * abs(values[2]))

        if (values[5] == 0 and values[2] == 0):
            motors.StopMotors()

        # if (values[0] < 0 or values[5] < 0) :

        # for i in range(len(values)):
        #     if (values[i]) :

        #         case 1:
        #         break

        #     print(i)

        sleep(0.2)


if __name__ == "__main__":
     __main__()
