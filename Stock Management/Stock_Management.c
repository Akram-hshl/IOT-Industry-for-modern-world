int Distance = 0;
int buzzer = 9;

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);  // Clear the trigger
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  // Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  // Reads the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(echoPin, HIGH);
}

void setup()
{
  Serial.begin(9600);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(8, OUTPUT);
}

void loop()
{
  Distance = 0.01723 * readUltrasonicDistance(6, 5);

  Serial.println(Distance);
  if (Distance < 30) {
    digitalWrite(11, HIGH);
   
    digitalWrite(9, LOW);
    
  } else {
    digitalWrite(11, LOW);
    digitalWrite(9, HIGH);
  }
    
    if (Distance >30 && Distance<= 80) {
      digitalWrite(10, HIGH);
      
    } else {
      digitalWrite(10, LOW);
    }
  
  
  
  if (Distance >80 && Distance <= 125) {
    digitalWrite(8, HIGH);
    
  } else {
    digitalWrite(8, LOW);
  }
  delay(10); // Delay a little bit to improve simulation performance
}
