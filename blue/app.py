from flask import Flask,request
import json
import requests
import time
from rpi_ws281x import *
import argparse

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

# Main program logic follows:
def turn_on_LED():
    
    # LED strip configuration:
    LED_COUNT      = 8      # Number of LED pixels.
    LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
    #LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

   
   
    #print ('Theater chase animations.')
    #theaterChase(strip, Color(127, 127, 127))  # White theater chase
    theaterChase(strip, Color(127,   0,   0))  # Red theater chase
    #theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
    #theaterChaseRainbow(strip, 50)
    colorWipe(strip, Color(0,0,0), 10)
    
app = Flask(__name__)

@app.route('/')
def root():
    return 'welcom'

@app.route('/sub')
def sub():
    return 'sub_page'

@app.route('/data',methods=['POST'])
def handle_post():
    data = json.loads(request.get_data())
    if len(data)==0:
        return 'No data'

    data_str=''
    print(data)
    turn_on_LED()
    return 'OK' 

if __name__=='__main__':
    app.debug=True
    app.run()
