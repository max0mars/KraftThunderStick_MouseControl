uint8_t br = A3;
uint8_t bl = A2;
uint8_t ora = A1;

uint8_t gr = 4;
uint8_t blue = 7;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(br, INPUT);
  pinMode(bl, INPUT);
  pinMode(ora, INPUT);
  

  pinMode(gr, OUTPUT);
  digitalWrite(gr, LOW);
  pinMode(blue, INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(50);
  int brRead = analogRead(br);
  int blRead = analogRead(bl);
  int orRead = analogRead(ora);
  int buttonRead = digitalRead(blue);

  Serial.println(String(brRead) + " " + String(orRead) + " " + String(blRead) + " " + String(buttonRead));
}
