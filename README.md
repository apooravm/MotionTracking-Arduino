# MotionTracking-Arduino
Arduino Setup with object tracking using the mediapipe library

---

## Initialize and Install Dependencies
`pipenv shell`

`pipenv install`

---
### Board settings
locate `/src/arduino-sketch/sketch.json`

<b>Uno</b>
> "fqbn": "arduino:avr:uno"
    "name": "Arduino Uno"

<b>Nano (old Bootloader)</b>
> "fqbn": "arduino:avr:nano:cpu=atmega328old"
    "name": "Arduino Nano"

### Arduino-CLI 

**Upload**
`arduino-cli compile --upload`

**Generate sketch.json Config**
`arduino-cli board attach -b COM5 -v`

**Add Library**

* `arduino-cli lib install <lib Name>`
* `arduino-cli lib install <lib name>@1.0.0`
* `arduino-cli lib install --git-url https://github.com/arduino-libraries/WiFi101.git`
* `arduino-cli lib install --zip-path /path/to/<library>.zip`