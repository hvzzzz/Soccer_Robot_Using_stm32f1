int val=0;
void setup() 
{
    Serial.begin(9600);
}
void loop() 
{
    if(Serial1.available() > 0)
    { 
        val = map(val, 0, 10, 25, 50);
        Serial.write(val);
    }
}