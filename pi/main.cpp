#include <Arduino.h>

int ledPin = 13;

void setup(){
	pinMode(ledPin, OUTPUT);
}

void loop(){
	digitalWrite(ledPin, HIGH);
	delay(500);
	digitalWrite(ledPin, LOW);
	delay(500);
}

int main(void){
	init();
	setup();
	for(;;){
		loop();
	}
}
