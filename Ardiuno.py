#include <Servo.h>

const int irSensorPin = 2;
const int irSensorPin2 = 3;
const int touchSensorPin = 5;
const int greenLightPin = 6;
const int yellowLightPin = 7;
const int redLightPin = 8;
const int buzzerPin = 9;
const int barrierPin = 10;

Servo barrierServo;

int carsInside = 0;
const int maxCapacity = 7;
void setup() {
  Serial.begin(9600);
  pinMode(irSensorPin, INPUT);
  pinMode(touchSensorPin, INPUT_PULLUP);
  pinMode(greenLightPin, OUTPUT);
  pinMode(yellowLightPin, OUTPUT);
  pinMode(redLightPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(barrierPin, OUTPUT);

  barrierServo.attach(barrierPin);

  digitalWrite(greenLightPin,LOW);
  digitalWrite(yellowLightPin,HIGH);
  digitalWrite(redLightPin, LOW);
  digitalWrite(buzzerPin, LOW);
  barrierServo.write(0);
}
void loop() {
  digitalWrite(redLightPin, LOW);
  if(carsInside==maxCapacity){
    Serial.println("Sorry Max Capacity Reached");
    digitalWrite(redLightPin, HIGH);
    delay(10000);
  }
  else{
  if((digitalRead(irSensorPin)==HIGH) && (digitalRead(irSensorPin2)==LOW)){
   if(barrierServo.read()==0){
    digitalWrite(greenLightPin,HIGH);
    digitalWrite(yellowLightPin,LOW);
    barrierServo.write(90);
    delay(1000);
    }
  }
  if((digitalRead(irSensorPin)==LOW) && (digitalRead(irSensorPin2)==HIGH)){
    if(barrierServo.read()==90){
    barrierServo.write(0);
    digitalWrite(greenLightPin,LOW);
    digitalWrite(yellowLightPin,HIGH);
    carsInside++;
    Serial.print("Car Passed:");
    Serial.println(carsInside);
    }
  }
  if((digitalRead(irSensorPin)==LOW) && (digitalRead(irSensorPin2)==LOW)){
    barrierServo.write(0);
  }}
  
  if(digitalRead(touchSensorPin)==HIGH){
    digitalWrite(redLightPin, HIGH);
    digitalWrite(buzzerPin, HIGH);
    delay(500);
    digitalWrite(buzzerPin, LOW);
  }

}