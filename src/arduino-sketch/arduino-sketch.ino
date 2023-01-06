#include <Servo.h>

Servo myservo1;   
Servo myservo2;
   
String inByte;
int pos;
int whichservo = 1;
int onboard = 13;  

void setup() {
 
  myservo1.attach(9);
  Serial.begin(9600);
}

void loop()
{    
  if(Serial.available())  // if data available in serial port
    { 
    inByte = Serial.readStringUntil('\n'); // read data until newline
    pos = inByte.toInt();   // change datatype from string to integer 
      if(whichservo == 1)   
        {       
        myservo1.write(map(pos, 0, 1280, 20, 160));     // move servo
        Serial.print("Servo1 in position: ");  
        Serial.println(inByte);
        whichservo = 1;
        }
      else if(whichservo == 2)
        {       
        myservo2.write(pos);     // move servo
        Serial.print("Servo2 in position: ");  
        Serial.println(inByte);
        whichservo = 3;
        }  
      else if (whichservo == 3)
      {
        digitalWrite(onboard, pos);
        whichservo = 1;
      }
        
    }
}