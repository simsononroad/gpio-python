import board
from adafruit_ht16k33.segments import BigSeg7x4
from datetime import datetime



i2c = board.I2C()
display = BigSeg7x4(i2c)

def time():
    current_dateTime = datetime.now()
    display.print(f"{current_dateTime.hour}:{current_dateTime.minute}")

def temp():
    display.print("Temp")