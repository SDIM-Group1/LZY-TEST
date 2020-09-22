import numpy as np
#import pylab as pl
import RPi.GPIO as GPIO
from time import sleep
import wave
import pydub


f = wave.open("/home/pi/Desktop/dead.wav", "rb")

params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
# 读取波形数据
str_data = f.readframes(nframes)
f.close()
wave_data = np.fromstring(str_data, dtype=np.short)

lenth = len(wave_data)
ti = lenth / 16000.0
t = np.arange(0, ti, ti / lenth)

i = 0
LedPin = 25
freq = 100
dc = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LedPin, GPIO.OUT)

pwm = GPIO.PWM(LedPin, freq)
pwm.start(dc)



#set the wave shape to the range 0-100, serving DC
result0 = []
a = 30000
b = 60000
result1 = []

for element0 in np.nditer(wave_data, order='F'):
    result0.append(element0 + a)
for element1 in result0:
    c = element1 / b * 100
    if c > 100:
        c = 100
    elif c < 0:
        c = 0
    result1.append(c)
    #print(c)

#freq = int(input("Please input the frequency of PWM(1-2000Hz): "))
pwm.ChangeFrequency(300)
while True:
    dc = result1[i]
    sleep(0.01)
    pwm.ChangeDutyCycle(dc)
    i = i + 220
input()
GPIO.cleanup()
