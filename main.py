from time import sleep
import board
from adafruit_ht16k33.segments import BigSeg7x4
from datetime import datetime
import requests
import json

i2c = board.I2C()
display = BigSeg7x4(i2c)

def time():
    current_dateTime = datetime.now()
    display.print(f"{current_dateTime.hour}:{current_dateTime.minute}")
    sleep(30)
    
def temp():
    lekerdez = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=pécel&appid=a3c3ac028697416ece9bd3c3a7c0f500&units=metric')
    jsonformatum = json.loads(lekerdez.text)
    display.print(f"{jsonformatum['main']['temp']}C")
    print(round(jsonformatum['main']['temp']))
    sleep(30)
    
