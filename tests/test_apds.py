import time
import board
import busio
import adafruit_apds9960.apds9960

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_proximity = True
sensor.enable_color = True

while True:
    r, g, b, c = sensor.color_data
    print("Proximité:", sensor.proximity)
    print("RGB+C:", r, g, b, c)
    time.sleep(2)