import numpy as np
#import pylab as pl
import wave
import RPi.GPIO as GPIO
from time import sleep
import wave
#import os
#from playsound import playsound
#from scipy.io import wavfile
file = "/home/pi/Desktop/superbia.wav"
f = wave.open("/home/pi/Desktop/superbia.wav", "rb")
# 读取格式信息
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
# 读取波形数据
str_data = f.readframes(nframes)
f.close()
wave_data = np.fromstring(str_data, dtype=np.short)
# 在时间轴上画波形图
# 以上nchannels=1, sampwidth=2, framerate=16000
lenth = len(wave_data)
ti = lenth / 16000.0
t = np.arange(0, ti, ti / lenth)
print(t)


i = 0

LedPin = 25
freq = 100
dc = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LedPin, GPIO.OUT)

pwm = GPIO.PWM(LedPin, freq)
pwm.start(dc)
#os.system(file)
#freq = int(input("Please input the frequency of PWM(1-2000Hz): "))
pwm.ChangeFrequency(10)
#playsound("/home/pi/Desktop/superbia.wav")
while True:
    dc = t[i]
    sleep(0.01)
    pwm.ChangeDutyCycle(dc)
    i = i + 220
"""""
    if dc == 0:
        while 1:
            dc = dc + 1
            sleep(0.01)
            pwm.ChangeDutyCycle(dc)
            if dc == 100:
                break
    if dc == 100:
        while 1:
            dc = dc - 1
            sleep(0.01)
            pwm.ChangeDutyCycle(dc)
            if dc == 0:
                break
"""

input()
GPIO.cleanup()
