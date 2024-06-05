#include <Servo.h>
int const PINO_SGAS = A1;
int BUZZER2_PIN =13;
int pos = 0;
Servo myservo;


int led = 5;                // the pin that the LED is atteched to
int sensor = 2;              // the pin that the sensor is atteched to
int state = LOW;             // by default, no motion detected
int val = 0; 


void setup() {
  
  pinMode(A1, INPUT);
  pinMode(13, OUTPUT);
  myservo.attach(9);
  
  
  pinMode(led, OUTPUT);      // initalize LED as an output
  pinMode(sensor, INPUT);    // initialize sensor as an input
  
  
  
  Serial.begin(9600);
}

void loop() {
 
  int valor = analogRead(PINO_SGAS);
    valor = map(valor, 300, 750, 0, 100);

	if (valor >= 30) {
    // Turn on the buzzer with the specified frequency and delay
    tone(BUZZER2_PIN, 2600);
      
                  // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
   
      
    
  } else {
    // Turn off the buzzer
    noTone(BUZZER2_PIN);
      
   
    
  }
  
  
  val = digitalRead(sensor);   // read sensor value
  if (val == HIGH) {           // check if the sensor is HIGH
    digitalWrite(led, HIGH);   // turn LED ON
    delay(100);                // delay 100 milliseconds 
    
    if (state == LOW) {
      Serial.println("Motion detected!"); 
      state = HIGH;       // update variable state to HIGH
    }
  } 
  else {
      digitalWrite(led, LOW); // turn LED OFF
      delay(200);             // delay 200 milliseconds 
      
      if (state == HIGH){
        Serial.println("Motion stopped!");
        state = LOW;       // update variable state to LOW
    }

  

  delay(10);
} 
}
 
