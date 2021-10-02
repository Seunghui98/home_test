import serial  # 시리얼통신을 위한 pyserial import
import time


def color_change(emotion):
    ser = serial.Serial('COM3', 9600)  # 아두이노와 시리얼통신을 위한 포트 연결 및 보드레이트 일치시킴
    count = 0
    while True:
        if count > 2:
            break
        if ser.readable():
            print('color')
            if emotion == "ANGRY":
                val = '1'
            elif emotion == "DISGUST":
                val = '2'
            elif emotion == "HAPPY":
                val = '3'
            elif emotion == "FEAR":
                val = '4'
            elif emotion == "NEUTRAL":
                val = '5'
            elif emotion == "SAD":
                val = '6'
            elif emotion == "SURPRISE":
                val = '7'
            val = val.encode('utf-8')

            print(val)
            ser.write(val)  # 아두이노에 시리얼통신으로 val 값 전송
            time.sleep(0.5)
            count += 1


def off():
    ser = serial.Serial('COM3', 9600)  # 아두이노와 시리얼통신을 위한 포트 연결 및 보드레이트 일치시킴
    count = 0
    while (True):
        if count > 2:
            break
        if ser.readable():
            print('off')
            val = '0'
            val = val.encode('utf-8')
            ser.write(val)  # 아두이노에 시리얼통신으로 val 값 전송
            time.sleep(0.5)
            count += 1
def on():
    ser = serial.Serial('COM3', 9600)  # 아두이노와 시리얼통신을 위한 포트 연결 및 보드레이트 일치시킴
    count = 0
    while (True):
        if count > 2:
            break
        if ser.readable():
            print('on')
            val = '8'
            val = val.encode('utf-8')
            ser.write(val)  # 아두이노에 시리얼통신으로 val 값 전송
            time.sleep(0.5)
            count += 1

def emergency():
    ser = serial.Serial('COM3', 9600)  # 아두이노와 시리얼통신을 위한 포트 연결 및 보드레이트 일치시킴
    count = 0
    while (True):
        if count > 2:
            break
        if ser.readable():
            print('on')
            val = '9'
            val = val.encode('utf-8')
            ser.write(val)  # 아두이노에 시리얼통신으로 val 값 전송
            time.sleep(0.5)
            count += 1
            
off()
time.sleep(1)
on()
time.sleep(1)
color_change('ANGRY')
time.sleep(1)
color_change('DISGUST')
time.sleep(1)
color_change('HAPPY')
time.sleep(1)
color_change('FEAR')
time.sleep(1)
color_change('NEUTRAL')
time.sleep(1)
color_change('SAD')
time.sleep(1)
color_change('SURPRISE')
time.sleep(1)
off()
