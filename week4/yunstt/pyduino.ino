byte data = 0;
int led = 13;
void setup() {
  Serial1.begin(9600);
  pinMode(led, OUTPUT);
}
void loop() {
  data = Serial1.read();
  if(data == 1){
    digitalWrite(led, HIGH);
    delay(1000);
  }else{
    digitalWrite(led, LOW);      
  }
}