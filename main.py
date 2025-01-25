try:
    from time import sleep
    import board
    from adafruit_ht16k33.segments import BigSeg7x4
    from datetime import datetime
    import requests
    import json
    import RPi.GPIO as GPIO
    
    GPIO.setwarnings(False) # Ignore warning for now
    #GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    

    i2c = board.I2C()
    display = BigSeg7x4(i2c)

    while True: # Run forever
        if GPIO.input(10) == GPIO.HIGH:
            print("Button was pushed!")
            break
    
    def time():
        current_dateTime = datetime.now()

        min = str(current_dateTime.minute)
        if len(min) == 1:
            display.print(f"{current_dateTime.hour}:0{min}")
        else:
            display.print(f"{current_dateTime.hour}:{current_dateTime.minute}")
        sleep(10)
        
        
        
    def temp():
        lekerdez = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=pécel&appid=a3c3ac028697416ece9bd3c3a7c0f500&units=metric')
        jsonformatum = json.loads(lekerdez.text)
        temp = jsonformatum['main']['temp']
        temp = round(temp)
        temp = str(temp)
        #print(type(jsonformatum['main']['temp']))
        if len(temp) == 1:
            display.print(f"||{round(jsonformatum['main']['temp'])}C")
        elif len(temp) == 2:
            display.print(f"|{round(jsonformatum['main']['temp'])}C")
        #print(round(jsonformatum['main']['temp']))
        sleep(10)
        #jsonformatum['main']['temp']
    def main():
        while True:
            time()
            temp()

    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    display.print('quit')
    sleep(3)
    display.fill(0)
    import os
    os.system('clear')
    print("Program leállítva")
    exit()