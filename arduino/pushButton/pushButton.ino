#define PIN_COUNT 6

const int PIN[PIN_COUNT] = {2, 3, 4, 5, 6, 7, }; //푸시버튼

int sold_position;     
int btn[6];            


void setup() {

  Serial.begin(9600);
  for (int i = 0; i < PIN_COUNT; i++) {
    pinMode(PIN[i] , INPUT_PULLUP);
  }
}

void loop() {
  
 
  for (int i = 0; i < PIN_COUNT; i++) {
    btn[i] = digitalRead(PIN[i]);
    if (btn[i] == 0) {        
      sold_position = i+1;
      Serial.print(sold_position);
      Serial.print("_E_");        
      break;
    }
    
  }
  delay(500);

}