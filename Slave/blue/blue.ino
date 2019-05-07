//PROGRAM FOR BLUETOOTH INTERFACE WITH STM32F103C8
//CIRCUIT DIGEST
//Pramoth Thangavel
char received_data = 0;  //Variable for storing received data
int xdat[5];
int ydat[5];
bool status=true;//used for the switching between right and left;true is right;just to make sure :)
//#include <AutoPID.h>
void setup()
{
   memset(xdat,0,sizeof(xdat));//fills the x array of zeros
   memset(ydat,0,sizeof(ydat));//fills the y array of zeros
   Serial1.begin(9600);                      //Sets the baud rate for bluetooth pins 
   Serial1.print("BLUETOOTH WITH STM32\n");                     
   pinMode(PB12, OUTPUT);                  //Sets digital pin PA0 as output pin for led
   pinMode(PB13, OUTPUT);
   pinMode(PB14, OUTPUT);
   pinMode(PB15, OUTPUT);
   //pinMode(PA5, OUTPUT);
   //pinMode(PA4, OUTPUT);
   pinMode(PA6, OUTPUT);
   pinMode(PA7, OUTPUT);
}
int constructor(int *number,int len)
{
   bool sign=true;//positive number
   int rebuilt=0;
   if(*number==1)
      sign=false;//negative number
   number++;
   for(int i=1;i<len;i++)
   {
      rebuilt=rebuilt+*number*pow(2,len-(i+1));
      number++;
   }
   if(!sign)
      rebuilt=rebuilt*-1;
   return (rebuilt);
}
void loop()
{
   if(Serial1.available() > 0)      // Send data only when you receive data:
   {
      received_data = Serial1.read();        //Read the incoming data & store into a string     
      if(status)//fills the x coordinate array
      {
         int i=0;
         while(received_data!=' ')
         {
            if(received_data=='1')
            {
               xdat[i]==1;
            }
            i++;
         }
         status=false;
      }
      int *x_point=xdat;
      int x_value=constructor(x_point,5);
      if(!status)//fills the y coordinate array
      {
         int i=0;
         while(received_data!=' ')
         {
            if(received_data=='1')
            {
               ydat[i]==1;
            }
            i++;
         }
         status=true;
      }
      int *y_point=ydat;
      int y_value=constructor(y_point,5);
      //printf("%d %d",x_value,y_value);
      //String out=String(x_value)+" "+String(y_value)+"\n";
      //Serial1.print(out);
      Serial1.print(x_value);
      //Serial1.print(" ");
      //Serial1.print(String(y_value));
      //Serial1.print("\n");
      /*
      if(inputdata == "1 9") 
      {
         digitalWrite(PB12, HIGH);
         digitalWrite(PB13, LOW);
         digitalWrite(PB14, HIGH);
         digitalWrite(PB15, LOW);
         //digitalWrite(PA5, HIGH);
         analogWrite(PA6, 250);
         analogWrite(PA7, 250); 
         Serial1.print("ADELANTE\n");
      }
      else if(inputdata == "0 7")  
      {      
         digitalWrite(PB12, LOW);
         digitalWrite(PB13, HIGH);
         digitalWrite(PB14, LOW);
         digitalWrite(PB15, HIGH);
         //digitalWrite(PA4, HIGH);
         analogWrite(PA6, 250);
         analogWrite(PA7, 250);   
         Serial1.print("ATRAS\n");  
      }
      else if(inputdata == "2")
      {
         digitalWrite(PB12, LOW);
         digitalWrite(PB13, LOW);
         digitalWrite(PB14, LOW);
         digitalWrite(PB15, LOW);
         analogWrite(PA6, 0);
         analogWrite(PA7, 0);   
         Serial1.print("PARAR\n");
      }
      */
   }
}
