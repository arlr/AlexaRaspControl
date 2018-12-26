#include <Arduino.h>
#include <SoftwareSerial.h>

// Constantes
#define RELAY 12
#define TX 8
#define RX 7

SoftwareSerial hc05(RX , TX);

void InitBL(){
  pinMode(TX, OUTPUT);
  pinMode(RX, INPUT);
  hc05.begin(9600); //Speed
  //Serial.begin(9600); 
  SetupBL();
}

void SetupBL(){
  hc05.write("AT+UART=9600,0,0"); //Speed
  hc05.write("AT+NAME=LumBur"); //Name
  hc05.write("AT+PSWD=1234"); //PassWord
}

readBL(){
  char val;
  if(hc05.available){
    val = hc05.read()
    if(val == '0'){ //If transmission is 0 turn off the light.
      digitalWrite(RELAY,LOW);
    }
    if(val == '1'){
      digitalWrite(RELAY,HIGH);
    }
  }
}
void setup() {
  
  InitBL();
  pinMode(RELAY,OUTPUT);
  digitalWrite(RELAY,HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  readBL();
}