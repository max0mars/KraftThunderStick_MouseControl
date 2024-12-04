# KraftThunderStick_MouseControl

This allows a computer mouse to be controlled using a Kraft Thunder Stick which is 1990s game controller. The controller is wired up to an arduino and then the arduino is connected to the computer via usb. 

The controller uses variable resistors attached to the controller axles. The arduino measures the voltage coming from a voltage divider circuit attached to the variable resistors.

Because the Arduino Nano does not have the capabilities to move a computer mouse, a python script must be run to recieve the voltage readings from the arduino. It uses the library "serial" to read data from the usb port and "mouse" to control the mouse.

Right clicking the computer mouse will stop the python script in case you lose control.
![Controller](https://github.com/user-attachments/assets/f2e5a826-3aa0-41e5-95c9-5e996afda998)
