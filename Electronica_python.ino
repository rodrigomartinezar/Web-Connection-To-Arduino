const int pinLED = 13;
 
void setup() 
{
   Serial.begin(9600);
   pinMode(pinLED, OUTPUT);
   pinMode(2, OUTPUT);
}
 
void loop()
{
   if (Serial.available()>0) 
   {
      char msg = Serial.read();
      if (msg == 'h'){
        Serial.println("Holi");
        digitalWrite(pinLED, HIGH);
      }
      if (msg == 'z'){
        Serial.println("Chai");
        digitalWrite(2, HIGH);
      }
   }
}
