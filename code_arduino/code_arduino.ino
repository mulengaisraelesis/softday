int ledPin = 13;  // Modifier pour le pin que tu veux utiliser
bool ledState = LOW;

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW); // S'assurer que la LED est éteinte au démarrage
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char data = Serial.read();
    if (data == '1') {
      // Clignoter la LED 3 fois
      for (int i = 0; i < 5; i++) {
        digitalWrite(ledPin, HIGH);
        delay(500);  // Allumé pendant 500ms
        digitalWrite(ledPin, LOW);
        delay(500);  // Éteint pendant 500ms
      }
    } else {
      digitalWrite(ledPin, LOW);  // Éteindre la LED sinon
    }
  }
}
