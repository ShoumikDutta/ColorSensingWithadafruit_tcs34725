import time
import board
import busio
import adafruit_tcs34725

def is_red_or_blue():
    # Create I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)
    
    # Create sensor object, communicating over the I2C bus
    sensor = adafruit_tcs34725.TCS34725(i2c)
    
    # Enable sensor
    sensor.integration_time = 0xEB  # Set integration time
    sensor.gain = 0x01  # Set gain
    
    # Read the RGB values from the sensor
    r, g, b = sensor.color_rgb_bytes
    
    # Print the RGB values for debugging
   # print(f"R: {r}, G: {g}, B: {b}")
    
    # Determine if the color is red or blue
    if r > b:
        return True  # Red
    else:
        return False  # Blue

