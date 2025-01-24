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
    sleep(1)
    display.print("")
    
def temp():
    lekerdez = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=pécel&appid=a3c3ac028697416ece9bd3c3a7c0f500&units=metric')
    jsonformatum = json.loads(lekerdez.text)
    test = 12.3
    test = round(test)
    test = str(test)
    #print(type(jsonformatum['main']['temp']))
    print(f"{test} | {len(test)}")
    if len(test) == 1:
        display.print(f"--{round(jsonformatum['main']['temp'])}C")
    elif len(test) == 2:
        display.print(f"-{round(jsonformatum['main']['temp'])}C")
    #print(round(jsonformatum['main']['temp']))
    sleep(10)
    #jsonformatum['main']['temp']
def main():
    while True:
        time()
        temp()

if __name__ == "__main__":
    main()