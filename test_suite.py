# Team Members: Michael Wang
# Github Repo Link: 
"""EE 250L Lab 07

Run test_suite.py on Raspberry Pi."""

# Imports
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO

# Blink LED on pin for given number of times for given interval duration
def led_blink(times, interval, pin):
  for i in range(times):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(interval)

led_pin = 11
sound_sensor_pin = 0
light_sensor_pin = 1
# Set pin numbering system to BOARD numbering
GPIO.setmode(GPIO.BOARD)
# Set led_pin to be an output pin
GPIO.setup(led_pin, GPIO.OUT)
# Software SPI configuration:
SCLK = 23
MISO = 21
MOSI = 19
CE0 = 24
mcp = Adafruit_MCP3008.MCP3008(clk=SCLK, cs=CE0, miso=MISO, mosi=MOSI)

if __name__ == '__main__':
  while True:
    # Blink the LED 5 times with on/off intervals of 500ms
    led_blink(5, 0.5, led_pin)

    # Read output of Grove light sensor for 5s with intervals of 100ms
    # Print raw values of light sensor with text "bright" or "dark"
    for i in range(50):
      light_sensor = mcp.read_adc(sound_sensor_pin)
      print(light_sensor)
      if light_sensor > 100:
        print("bright")
      else:
        print("dark")
      time.sleep(0.1)

    # Blink the LED 4 times with on/off intervals of 200ms
    led_blink(4, 0.2, led_pin)

    # Read output of Grove sound sensor for 5s with intervals of 100ms
    # Print sound sensor raw value
    # If sound sensor is tapped, turn on LED for 100ms
    for i in range(50):
      GPIO.output(led_pin, GPIO.LOW)
      sound_sensor = mcp.read_adc(sound_sensor_pin)
      print(sound_sensor)
      if sound_sensor > 500:
        GPIO.output(led_pin, GPIO.HIGH)
      time.sleep(0.1)
