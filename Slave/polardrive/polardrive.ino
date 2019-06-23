//Set pin numbers:
//const byte joyStickYPin = A2;
//const byte joyStickXPin = A1;

const byte motorL1DirPin = PB12;
const byte motorLDirPin = PB13;
const byte motorR1DirPin = PB14;
const byte motorRDirPin = PB15;
const byte motorLSpeedPin = PA7;
const byte motorRSpeedPin = PA6;

/*
const byte motorL1DirPin = PD2;
const byte motorLDirPin = PD4;
const byte motorR1DirPin = PD7;
const byte motorRDirPin = PB0;
const byte motorLSpeedPin = PD5;
const byte motorRSpeedPin = PD6;
*/
//my variables
char received_data = 0;  //Variable for storing received data
int datas[5];
int *p0=datas;
int i=0;
int meter=0;
int x_dat=0;
int y_dat=0;
bool status=true;//used for the switching between right and left;true is right;just to make sure :)
//variables
//Joystick input variables
int joyXValue = 0;
int joyYValue = 0;
int joyValueMax = 10;
int joyValueMin = -10;
int joyValueMid = 0;
int joyValueMidUpper = joyValueMid + 0;
int joyValueMidLower = joyValueMid - 0;
//DC motor variables
int speedFwd = 0;
int speedTurn = 0;
int speedLeft = 0;
int speedRight = 0;
byte motorSpeed = 0;
byte motorSpeedMax = 255;
byte motorSpeedMin = 110; //set to smallest value that make motor move (default 0)
// DC motor that I use start to move at 90 pwm value
void setup()
{
    initial(p0,5,2);//fill the data array with two's
    Serial1.begin(9600);                      //Sets the baud rate for bluetooth pins 
    //Serial.begin(9600);  
    //Serial1.print("BLUETOOTH WITH STM32\n");   
    pinMode(motorR1DirPin, OUTPUT);
    pinMode(motorL1DirPin, OUTPUT);
    pinMode(motorLSpeedPin, OUTPUT);
    pinMode(motorLDirPin, OUTPUT);
    pinMode(motorRSpeedPin, OUTPUT);
    pinMode(motorRDirPin, OUTPUT);
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
    if(Serial1.available() > 0)      // Send data only when you receive data:,outputs x_dat and y_dat
    //if(Serial.available() > 0)
    {
        //received_data = Serial.read();
        received_data = Serial1.read();        //Read the incoming data & store into a string     
        if(meter==0||meter==1)//fills the x coordinate array
        {
            if(received_data=='1')
                datas[i]=1;
            if(received_data=='0')
                datas[i]=0;
            if(received_data=='0'||received_data=='1'||received_data=='3')
                i++;
            if(received_data=='3')
            {
                i=0;
                meter++;
                if(meter==1)
                {
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
            //Serial1.print("data: ");
            //Serial1.print(x_dat);
            //Serial1.print(" ");
            //Serial1.print(y_dat);
            //Serial1.print("\n");
            initial(p000,5,2);
            joyXValue = x_dat;
            joyYValue = y_dat;
            
            if(joyYValue > 0)//forward
            {
                speedFwd = map(joyYValue, joyValueMidUpper, joyValueMax, motorSpeedMin, motorSpeedMax);
            }
            else if(joyYValue < 0) //backward
            {
                speedFwd = map(joyYValue, joyValueMidLower, joyValueMin, -motorSpeedMin, -motorSpeedMax);
            }
            else
            {   
                speedFwd =0;
            }
            if(joyXValue > 0) //right
            {
                speedTurn = map(joyXValue, joyValueMidUpper, joyValueMax, motorSpeedMin, motorSpeedMax);
            }
            else if(joyXValue < 0) //left
            {
                speedTurn = map(joyXValue, joyValueMidLower, joyValueMin, -motorSpeedMin, -motorSpeedMax);
            }
            else
            {
                speedTurn =0;
            }
            //speedLeft = speedFwd + speedTurn;
            //speedRight = speedFwd - speedTurn;
            speedRight = speedFwd - speedTurn;
            speedLeft = speedFwd +  speedTurn;
            speedLeft = constrain(speedLeft, -255, 255);
            speedRight = constrain(speedRight, -255, 255);
            //MoveRobot(speedLeft,speedRight);
            MoveRobot(speedRight,speedLeft);
            //Serial1.print(speedFwd);
            //Serial1.print(" ");
            //Serial1.print(speedTurn);
            //Serial1.print(" ");
            //Serial1.print(speedLeft);
            //Serial1.print(" ");
            //Serial1.print(speedRight);
            //Serial1.print("\n");
            //delay(100);
        }
    }
}
void MoveRobot(int spdL, int spdR)
{
    if(spdL>0)//controlls the speed of one wheel if the speed of the wheel if positive
    //this means that the wheel must rotate in that direction
    {
        digitalWrite(motorL1DirPin, HIGH);
        digitalWrite(motorLDirPin, LOW);
    }
    else
    {
        digitalWrite(motorL1DirPin, LOW);
        digitalWrite(motorLDirPin, HIGH);
    }
    if(spdR>0)
    {
        digitalWrite(motorR1DirPin, HIGH);
        digitalWrite(motorRDirPin, LOW);
    }
    else
    {
        digitalWrite(motorR1DirPin, LOW);
        digitalWrite(motorRDirPin, HIGH);
    }
    analogWrite(motorLSpeedPin, abs(spdR));
    analogWrite(motorRSpeedPin, abs(spdL));    
}
