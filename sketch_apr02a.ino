const int pinLED = 11;
const int pinLED2 = 8;
 
void setup() 
{
   Serial.begin(9600);
   pinMode(pinLED, OUTPUT);
}
 
void loop()
{
   if (Serial.available()>0) 
   {
      char option = Serial.read();
      if (option == '1')
      {
        digitalWrite(pinLED2, LOW);
        digitalWrite(pinLED, HIGH);
      }
      else if (option == '2'){
        digitalWrite(pinLED, LOW);
        digitalWrite(pinLED2, HIGH);
      }
     
   }
}
