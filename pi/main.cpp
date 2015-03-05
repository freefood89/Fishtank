#include <Arduino.h>
#include <Servo.h>

Servo servo1;  // create servo object to control a servo 
Servo servo2;  // a maximum of eight servo objects can be created 

struct Device{
  String name;
  String type;
  byte value;
  byte port;
};

int NUM_DEVICES = 6;

int indexOfSpace;
Device* targetDevice;
char buffer[20];

Device devices[]={
  (Device){"servo_1","servo",0,9},
  (Device){"servo_2","servo",0,10},
  (Device){"led_1","pwm",0,5},
  (Device){"led_2","pwm",0,6},
  (Device){"sensor_1","sensor",0,0},
  (Device){"sensor_2","sensor",0,1}
};

String input;

void setup() 
{ 
  Serial.begin(9600);
  servo1.attach(9);  // attaches the servo on pin 9 to the servo object 
  servo2.attach(10);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
} 

void printDevices(){
  for(int i=0; i<NUM_DEVICES; i++){
    Serial.print(devices[i].name);
    if(i < NUM_DEVICES - 1){
      Serial.print(", ");
    }
  }
  Serial.println("");
}

Device* getDevice(String name){
  for(int i=0; i<NUM_DEVICES; i++){
    if(devices[i].name.equals(name)){
      return &devices[i];
    }
  }
  return NULL;
}

void loop() 
{
  if(0 < Serial.readBytesUntil('\n',buffer,20)){
    // Serial.println(String(buffer)+"<");
    if(String(buffer).equals(String("list all"))){
      printDevices();
    }
    else if(String(buffer).equals(String("test"))){
      Serial.println("I'm here");
    }
    else{
      indexOfSpace = String(buffer).indexOf(' ');
      if(indexOfSpace>-1){
        targetDevice = getDevice(String(buffer).substring(0,indexOfSpace));
        if(targetDevice){
          Serial.print("PORT ");
          Serial.print(targetDevice->port, DEC);
          Serial.print(" - set to ");
          Serial.println(String(buffer).substring(indexOfSpace+1).toInt(),DEC);
          if(String("servo_1").equals(targetDevice->name)){
            servo1.write(String(buffer).substring(indexOfSpace+1).toInt());
          }
          else if(String("servo_2").equals(targetDevice->name)){
            servo2.write(String(buffer).substring(indexOfSpace+1).toInt());
          }
          else if(String("pwm").equals(targetDevice->type)){
            analogWrite((int)(targetDevice->port),String(buffer).substring(indexOfSpace+1).toInt());
          }
        }
        else{
          Serial.println("Device Not Found");
        }
      }
      else{
        Serial.print("Invalid: ");
        Serial.println(buffer);
      }      
    }
    for(int i=0; i<20; i++){
      buffer[i] = '\0';
    }
  }
} 

int main(void){
	init();
	setup();
	for(;;){
		loop();
	}
}


