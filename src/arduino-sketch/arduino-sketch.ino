#include <Servo.h>
#include <TM1637Display.h>

int DIO = 6;
int CLK = 7;
Servo servo;

int angle;
int state;
String serial_inp;
int prevAngle = 0;

int onboard = 13;

TM1637Display display = TM1637Display(CLK, DIO);

const uint8_t allON[] = {0xff, 0xff, 0xff, 0xff};
const uint8_t allOFF[] = {0x00, 0x00, 0x00, 0x00};

int brightness = 1;

int angle1;
int angle2;
String _;

void pushCoords(String inputString)
{
    _ = inputString.substring(0, 3);
    angle1 = _.toInt();
    _ = inputString.substring(4, 7);
    angle2 = _.toInt();
}

void setup()
{
    pinMode(onboard, OUTPUT);
    servo.attach(9);
    Serial.begin(9600);
}

void loop()
{
    display.setBrightness(5);
    // display.setSegments(allON);
    if(Serial.available())
    {
        serial_inp = Serial.readStringUntil('\n');
        state = serial_inp.toInt();
        angle = map(state, 0, 1280, 10, 170);
        
        if (angle != prevAngle)
        {
            // display.clear();
            display.showNumberDec(angle);
            servo.write(angle);
            prevAngle = angle;
            delay(20);
        } 
    }
}