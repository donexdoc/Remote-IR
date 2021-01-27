#include "IRremote.h"

#define IR_PIN 7 

IRrecv irrecv(IR_PIN);

decode_results results;

void setup() {
  Serial.begin (9600);
  irrecv.enableIRIn();
}

void loop() {
  if ( irrecv.decode( &results )) { 
    Serial.println( results.value, HEX ); 
    irrecv.resume(); 
  }
}