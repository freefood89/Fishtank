#include <Arduino.h>
#include <Servo.h>

Servo servo;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 
char buffer[20];

int NUM_SETTABLES = 4;
int NUM_GETTABLES = 2;

struct Device{
  String name;
  char value;
  char port;
};

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

void loop() 
{
  if(0 < Serial.readBytesUntil('\n',buffer,20)){
    input = String(buffer);
    if(input.equals(String("list all"))){
      printDevices();
    }
    else if(input.equals(String("servo 180"))){                            
      servo.write(180);
      Serial.println("done\n");
      delay(1500);                  
    }
    else{
      Serial.print("Couldn't Understand: ");
      Serial.println(buffer);
    }
    for(int i=0;i<20;i++){
      buffer[i] = 0;
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


