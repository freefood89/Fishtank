#include <Arduino.h>
#include <Servo.h>
#include <stdio.h>

Servo servo1;  // create servo object to control a servo 
Servo servo2;  // a maximum of eight servo objects can be created 

struct Device{
  char name [10];
  char type [10];
  int value;
  int port;
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
int sensor1val = 0;
int sensor2val = 0;

char cmd [5];
char target [10];
int targetValue = 0;
int numArgs = 0;

void setup() 
{ 
  Serial.begin(9600);
  servo1.attach(9);  // attaches the servo on pin 9 to the servo object 
  servo2.attach(10);
  pinMode(5, OUTPUT);
  analogWrite(5,0);
  pinMode(6, OUTPUT);
  analogWrite(6,0);

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

Device* getDevice(char* name){
  for(int i=0; i<NUM_DEVICES; i++){
    if(0==strcmp(devices[i].name,name)){
      return &devices[i];
    }
  }
  return NULL;
}

void loop() 
{
  if(0 < Serial.readBytesUntil('\n',buffer,20)){
    // Serial.println(String(buffer)+"<");
    numArgs = sscanf(buffer,"%s %s %d",cmd,target,&targetValue);
    if(numArgs==3 && strcmp(cmd,"set")==0){
      targetDevice = getDevice(target);
      if(targetDevice){
        Serial.println("Found device in question");
      }
      else
        Serial.println("Error: Device Not Found");
    }
    else if(numArgs==2 && strcmp(cmd,"get")==0){
      targetDevice = getDevice(target);
      if(targetDevice){
        Serial.println("Found device in question");
      }
      else
        Serial.println("Error: Device Not Found");
    }
    else{
      Serial.println("Error: Invalid Command");
    }
      // indexOfSpace = String(buffer).indexOf(' ');
      // if(indexOfSpace>-1){
      //   targetDevice = getDevice(String(buffer).substring(0,indexOfSpace));
      //   if(targetDevice){
      //     if(String("servo_1").equals(targetDevice->name)){
      //       servo1.write(String(buffer).substring(indexOfSpace+1).toInt());
      //     }
      //     else if(String("servo_2").equals(targetDevice->name)){
      //       servo2.write(String(buffer).substring(indexOfSpace+1).toInt());
      //     }
      //     else if(String("pwm").equals(targetDevice->type)){
      //       analogWrite(targetDevice->port,String(buffer).substring(indexOfSpace+1).toInt());
      //     }
      //     else if(String("sensor").equals(targetDevice->type)){
      //       sensor1val = analogRead(targetDevice->port);
      //       Serial.print(sensor1val,DEC);
      //     }
      //     Serial.print("PORT ");
      //     Serial.print(targetDevice->port, DEC);
      //     Serial.print(" - set to ");
      //     Serial.println(String(buffer).substring(indexOfSpace+1).toInt(),DEC);
      //   }
      //   else{
      //     Serial.println("Device Not Found");
      //   }
      // }
      // else{
      //   Serial.print("Invalid: ");
      //   Serial.println(buffer);
      // }      
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


