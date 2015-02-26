#include <Arduino.h>
#include <Servo.h>

Servo servo;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 

struct Device{
  String name;
  char value;
  char port;
};

int NUM_SETTABLES = 4;
int NUM_GETTABLES = 2;

int indexOfSpace;
Device* targetDevice;
char buffer[20];

Device settables[]={
  (Device){"servo_1",0,9},
  (Device){"servo_2",0,10},
  (Device){"led_1",0,11},
  (Device){"led_2",0,13}
};

Device gettables[]={
  (Device){"sensor_1",0,0},
  (Device){"sensor_2",0,1}
};

String input;

void setup() 
{ 
  Serial.begin(9600);
  servo.attach(9);  // attaches the servo on pin 9 to the servo object 
} 

void printDevices(){
  for(int i=0; i<NUM_SETTABLES; i++){
    Serial.print(settables[i].name);
    Serial.print(", ");
  }
  for(int i=0; i<NUM_GETTABLES; i++){
    Serial.print(gettables[i].name);
    if(i < NUM_GETTABLES - 1){
      Serial.print(", ");
    }
  }
  Serial.println("");
}

Device* getDevice(String name){
  for(int i=0; i<NUM_SETTABLES; i++){
    if(settables[i].name.equals(name)){
      return &settables[i];
    }
  }
  for(int i=0; i<NUM_GETTABLES; i++){
    if(gettables[i].name.equals(name)){
      return &gettables[i];
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
    else{
      indexOfSpace = String(buffer).indexOf(' ');
      if(indexOfSpace>-1){
        targetDevice = getDevice(String(buffer).substring(0,indexOfSpace));
        if(targetDevice){
          Serial.print("PORT ");
          Serial.print(targetDevice->port, DEC);
          Serial.print(" - set to ");
          Serial.println(String(buffer).substring(indexOfSpace+1));
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


