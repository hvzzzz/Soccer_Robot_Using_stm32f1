//PROGRAM FOR BLUETOOTH INTERFACE WITH STM32F103C8
//CIRCUIT DIGEST
//Pramoth Thangavel
char inputdata = 0;  //Variable for storing received data
#include <AutoPID.h>
void setup()
{
    Serial1.begin(9600);                      //Sets the baud rate for bluetooth pins 
    Serial1.print("BLUETOOTH WITH STM32\n");                     
    pinMode(PA4, OUTPUT);                  //Sets digital pin PA0 as output pin for led
    pinMode(PA6, OUTPUT);
    pinMode(PA7, OUTPUT);
}

void loop()
{
   if(Serial1.available() > 0)      // Send data only when you receive data:
   {
      inputdata = Serial1.read();        //Read the incoming data & store into data
           
      if(inputdata == '1') 
      {
         digitalWrite(PA4, HIGH);
         analogWrite(PA6, 250);
         analogWrite(PA7, 0); 
         Serial1.print("LED ON\n");
      }
         
      else if(inputdata == '0')  
      {      
         digitalWrite(PA4, LOW);
         analogWrite(PA6, 0);
         analogWrite(PA7, 50);   
         Serial1.print("LED OFF\n");  
      }
   }
}
