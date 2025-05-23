void setup() {
  Serial.begin(9600);
  delay(2000);

  String mensaje = "HOLA MUNDO";
  int desplazamiento = 3;
  String mensajeCifrado = "";

  for (int i = 0; i < mensaje.length(); i++) {
    char c = mensaje[i];
    if (c >= 'A' && c <= 'Z') {
      c = ((c - 'A' + desplazamiento) % 26) + 'A';
    }
    mensajeCifrado += c;
  }

  Serial.println("MSG:" + mensaje);
  Serial.println("CIF:" + mensajeCifrado);
}

void loop() {
}


