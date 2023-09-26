#include <Char2Int.h>
#include <CapacitiveSensor.h>


#define COMMON_PIN      2    
#define NUM_OF_SAMPLES  10   
#define NUM_OF_KEYS     6   

#define CS(Y) CapacitiveSensor(2, Y) //각 터치 센서에의 키 지정 

CapacitiveSensor keys[] = { CS(3), CS(4), CS(5), CS(6), CS(8), CS(9)};

bool hand_exist = false;     

int sold_position;           
int sensed_position = -1;       
char serial_touch[3] = {0}; 
int overlap=0;               
int duplicate = 0;           

 
void setup()
{
  
  for (int i = 0; i < NUM_OF_KEYS; ++i) {
    keys[i].set_CS_AutocaL_Millis(0xFFFFFFFF);
  }
 
  Serial.begin(9600);
 
}

void loop()
{

  for (int i = 0; i < NUM_OF_KEYS; ++i) {

    
    if (keys[i].capacitiveSensor(NUM_OF_SAMPLES) > 5000 ) {
      sensed_position = i;    
      overlap += 1;
    } 
  }
  if (overlap == 1 || overlap == 0) 
    duplicate = false;
  if (overlap > 1) 
    duplicate = true;

 
  for (int i = 0; i < 3 ; i++) { 

    if (Serial.available()) {                
      serial_touch[i] = Serial.read();

      if (serial_touch[i] == 'E') {
        serial_touch[i] = 0;
        break;
      }
    }
  }

  sold_position = char2int(serial_touch[1]) * 10 + char2int(serial_touch[0]) - 1 ;
  
  if (sensed_position >= -1 && sensed_position < NUM_OF_KEYS && sold_position >= -1 && sold_position < NUM_OF_KEYS) { 
    Serial.print("success ");
    Serial.println(true);
    Serial.print("duplicate ");
    Serial.println(duplicate);
    Serial.print("sensed_position ");
    Serial.println(sensed_position);
    Serial.print("sold_position ");
    Serial.println(sold_position);
  }

  else {
    Serial.print("success ");
    Serial.println(false);
  }


  //변수 초기화 
  for (int i = 0; i < 3 ; i++) {  //serial_touch 초기화 
    serial_touch[i] = 0;
  }
  overlap = 0;
  sensed_position = -1;

  delay(5000);                            
}
