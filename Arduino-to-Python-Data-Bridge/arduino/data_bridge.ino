void setup() {
  Serial.begin(9600);
  pinMode(9, OUTPUT);
}

void loop() {

  int brightness = analogRead(A0);
  int ledBrightness = map(brightness, 50, 1000, 255, 0);
  analogWrite(9, ledBrightness);
  Serial.println(brightness);
  delay(50);

}
