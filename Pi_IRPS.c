

int ledPin = 13;
int sensorPin = 22;

double alpha = 0.75;
int period = 20;
double change = 0.0;

void setup() 
{
    pinMode(ledPin, OUTPUT);
    Serial.begin(115200);
}

void loop() 
{
    static double oldValue = 0;
    static double oldChange = 0;
    int rawValue = analogRead(sensorPin);
    double value = alpha * oldValue + (1 - alpha) * rawValue;  //这个平滑就是取本次和上一次测量数据的加权平均值
    Serial.println(value);

    oldValue = value;
    delay(period);
}