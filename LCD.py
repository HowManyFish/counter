from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO

lcd = CharLCD(numbering_mode=GPIO.BCM,
              cols=16, rows=2,
              pin_rs=5, pin_e=6,
              pins_data=[12, 13, 19, 26])

# Example: display numbers
lcd.clear()
lcd.write_string('Number: 1234')
