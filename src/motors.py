# CamJam EduKit 3 - Robotics
# Worksheet 4 – Driving and Turning
import RPi.GPIO as GPIO 
from time import sleep
# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# How many times to turn the pin on and off each second
Frequency = 20
# How long the pin stays on each cycle, as a percent (here, it's 30%)
DutyCycleA = 35
DutyCycleB = 35
# Setting the duty cycle to 0 means the motors will not turn
Stop = 0

# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)

# Turn all motors off
def StopMotors():
    print("StopMotors()")
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn both motors backwards
def Backwards(coef = 1):
    print("Backwards()")
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA * coef)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB * coef)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn both motors forwards
def Forwards(coef = 1):
    print("Forwards()")
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA * coef)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB * coef)
# Turn left
def Left(coef = 1):
    print("Left()")
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA * coef)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleA * coef)
# Turn Right
def Right(coef = 1):
    print("Right")
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA * coef)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB * coef)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)


def __main__():
    Forwards()
    sleep(0.5)
    Backwards()
    sleep(0.5)
    Left()
    sleep(0.5)
    Right()
    sleep(0.5)
    StopMotors()

if __name__ == "__main__":
     __main__()

