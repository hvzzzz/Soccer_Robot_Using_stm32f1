//PROGRAM FOR BLUETOOTH INTERFACE WITH STM32F103C8
//CIRCUIT DIGEST
//Pramoth Thangavel
char received_data = 0;  //Variable for storing received data
int datas[5];
int *p0=datas;
int i=0;
int meter=0;
int x_dat=0;
int y_dat=0;
bool status=true;//used for the switching between right and left;true is right;just to make sure :)
//#include <AutoPID.h>
void setup()
{
   initial(p0,5,2);//fill the data array with two's
   Serial1.begin(9600);                      //Sets the baud rate for bluetooth pins 
   Serial1.print("BLUETOOTH WITH STM32\n");                     
   pinMode(PB12, OUTPUT);                  //Sets digital pin PA0 as output pin for led
   pinMode(PB13, OUTPUT);
   pinMode(PB14, OUTPUT);
   pinMode(PB15, OUTPUT);
   pinMode(PA5, OUTPUT);
   pinMode(PA4, OUTPUT);
   pinMode(PA6, OUTPUT);
   pinMode(PA7, OUTPUT);
}
void initial(int *p,int len,int val)
{
   for(int i=0;i<len;i++)
   {
      *p=val;
      p++;
   }
}
int constructor(int *number,int len)
{
   bool sign=true;
   int rebuilt=0;
   int count=0;
    //int *temp=number;
   if(*number==1)
      sign=false;
    //number++;
   for(int ii=0;ii<len;ii++)
   {
      if(*number!=2)
         count++;
      number++;
   }
   number=number-len+1;
   for(int i=1;i<count;i++)
   {
      if(*number!=2)    
         rebuilt=rebuilt+*number*pow(2,count-(i+1));
      number++;
   }
   if(!sign)
      rebuilt=rebuilt*-1;
   return(rebuilt);
}
void loop()
{
   if(Serial1.available() > 0)      // Send data only when you receive data:
   {
      received_data = Serial1.read();        //Read the incoming data & store into a string     
      //Serial1.print("pass");
      /*
      Serial1.print("meter is: ");
      Serial1.print(meter);
      Serial1.print("\n");
      Serial1.print("data is: ");
      Serial1.print(received_data);
      Serial1.print("\n");
      Serial1.print("i is: ");
      Serial1.print(i);
      Serial1.print("\n");
      */
      /*
      if(received_data=='1')
      {
         //i++;
         //String out=String(i);
         Serial1.print("one\n");
         //Serial1.print(meter);
      }
      if(received_data=='0')
         Serial1.print("ZERO\n");
      */

      if(meter==0||meter==1)//fills the x coordinate array
      {
         if(received_data=='1')
            datas[i]=1;
         if(received_data=='0')
            datas[i]=0;
         /*
         for(int ii=0;ii<5;ii++)
         {
            Serial1.print(datas[ii]);
            Serial1.print(" ");
         }
         Serial1.print("\n");
         */
         if(received_data=='0'||received_data=='1'||received_data=='3')
            i++;
         if(received_data=='3')
         {
            i=0;
            meter++;
            if(meter==1)
            {
               //Serial1.print("pass0");
               int*p=datas;
               int*p00=datas;
               x_dat=constructor(p,5);
               initial(p00,5,2);
            }
         }
      }
      if(meter==2)//fills the y coordinate array
      {
         meter=0;
         int *p1=datas;
         int *p000=datas;
         y_dat=constructor(p1,5);
         initial(p000,5,2);
         //Serial1.print("pass\n");
         Serial1.print("r dat: ");
         Serial1.print(x_dat);
         Serial1.print(" ");
         Serial1.print(y_dat);
         Serial1.print("\n");
         if(y_dat>0) 
         {
            //Serial1.print("posx\n");
            digitalWrite(PB12, LOW);
            digitalWrite(PB13, HIGH);
            digitalWrite(PB14, LOW);
            digitalWrite(PB15, LOW);
            digitalWrite(PA5, LOW);
            digitalWrite(PA4, LOW);
         }
         if(y_dat==0)
         {
            //Serial1.print("zero\n");
            digitalWrite(PB13, LOW);
            digitalWrite(PB12, LOW);
            digitalWrite(PB14, LOW);
            digitalWrite(PB15, LOW);
            digitalWrite(PA5, LOW);
            digitalWrite(PA4, HIGH);
         }
         if(y_dat<0)
         {
            //Serial1.print("zero\n");
            digitalWrite(PB13, LOW);
            digitalWrite(PB12, LOW);
            digitalWrite(PB14, LOW);
            digitalWrite(PB15, HIGH);
            digitalWrite(PA5, LOW);
            digitalWrite(PA4, LOW);
         }
         /*
         if(x_dat>0)
         {
            //Serial1.print("zero\n");
            digitalWrite(PB13, LOW);
            digitalWrite(PB12, HIGH);
            digitalWrite(PB14, LOW);
            digitalWrite(PB15, LOW);
            digitalWrite(PA5, LOW);
            digitalWrite(PA4, LOW);
         } 
         if(x_dat==0)
         {
            //Serial1.print("zero\n");
            digitalWrite(PB13, LOW);
            digitalWrite(PB12, LOW);
            digitalWrite(PB14, LOW);
            digitalWrite(PB15, LOW);
            digitalWrite(PA5, HIGH);
            digitalWrite(PA4, LOW);
         } 
         if(x_dat<0)
         {
            //Serial1.print("zero\n");
            digitalWrite(PB13, LOW);
            digitalWrite(PB12, LOW);
            digitalWrite(PB14, HIGH);
            digitalWrite(PB15, LOW);
            digitalWrite(PA5, LOW);
            digitalWrite(PA4, LOW);
         }
         */   
         //Serial1.print("x is: ");
         //Serial1.print(x_dat);
         //Serial1.print(" ");
         //Serial1.print("y is: ");
         //Serial1.print(y_dat);
         //Serial1.print("\n");
      }
      //printf("%d %d",x_value,y_value);
      //String out=String(x_value)+" "+String(y_value)+"\n";
      //Serial1.print(out);
      //Serial1.print(x_value);
      //Serial1.print(" ");
      //Serial1.print(String(y_value));
      //Serial1.print("\n");
      if(received_data == '1') 
      {
         digitalWrite(PB12, HIGH);
         digitalWrite(PB13, LOW);
         digitalWrite(PB14, HIGH);
         digitalWrite(PB15, LOW);
         //digitalWrite(PA5, HIGH);
         analogWrite(PA6, 65);
         analogWrite(PA7, 65); 
         Serial1.print("ADELANTE\n");
      }
      else if(received_data == '0')  
      {      
         digitalWrite(PB12, LOW);
         digitalWrite(PB13, HIGH);
         digitalWrite(PB14, LOW);
         digitalWrite(PB15, HIGH);
         //digitalWrite(PA4, HIGH);
         analogWrite(PA6, 70);
         analogWrite(PA7, 70);   
         Serial1.print("ATRAS\n");  
      }
      else if(received_data == '2')
      {
         digitalWrite(PB12, LOW);
         digitalWrite(PB13, LOW);
         digitalWrite(PB14, LOW);
         digitalWrite(PB15, LOW);
         analogWrite(PA6, 0);
         analogWrite(PA7, 0);   
         Serial1.print("PARAR\n");
      }
   }
}
