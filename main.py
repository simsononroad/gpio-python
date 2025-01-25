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
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setwarnings(False)    # Ignore warning for now   # Use physical pin numbering
    GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)

    
    mode = "time"
    button_pressed = 0

    i2c = board.I2C()
    display = BigSeg7x4(i2c)
    
    
    def time():
        current_dateTime = datetime.now()
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(20, GPIO.LOW)
        min = str(current_dateTime.minute)
        if len(min) == 1:
            display.print(f"{current_dateTime.hour}:0{min}")
        else:
            display.print(f"{current_dateTime.hour}:{current_dateTime.minute}")
        
        
        
    def temp():
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(21, GPIO.LOW)
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
        #jsonformatum['main']['temp']
        
    def auto():
        while True:
            time()
            sleep(10)
            temp()
            sleep(10)
    
    
    def main():
        global mode
        global button_pressed
        while True:
            if GPIO.input(18) == GPIO.HIGH:
                change_mode()
            display_mode()
            sleep(0.09)
                      

    def change_mode():
        global mode
        if mode == "time":
            mode = "temp"
        
        elif mode == "temp":
            mode = "time"
        
        elif mode == "temp":
            mode = "auto"
        
    def display_mode():
        global mode
        if mode == "time":
            time()
        elif mode == "temp":
            temp()
        elif mode == "auto":
            auto()
        
        

    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    display.print('quit')
    sleep(1)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    display.fill(0)
    import os
    os.system('clear')
    print("Program leállítva")
    exit()