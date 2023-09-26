#include <Arduino.h>

#define PIN_COUNT 6

const int PIN[PIN_COUNT] = {2, 3, 4, 6, 7, 8}; // 푸시버튼
const int BUTTON_COUNT = 6; // 버튼 개수

int sold_position = 0;
int btnState[BUTTON_COUNT];
int prevBtnState[BUTTON_COUNT];

void setup() {
  Serial.begin(9600);

  for (int i = 0; i < BUTTON_COUNT; i++) {
    pinMode(PIN[i], INPUT_PULLUP);
    prevBtnState[i] = digitalRead(PIN[i]); // 초기 버튼 상태를 읽고 이전 버튼 상태로 설정
  }
}

void loop() {
  for (int i = 0; i < BUTTON_COUNT; i++) {
    btnState[i] = digitalRead(PIN[i]);

    if (btnState[i] != prevBtnState[i]) { // 버튼 상태가 변경되었는지 확인
      if (btnState[i] == LOW) { // 버튼이 눌린 경우
        sold_position = i + 1;
        Serial.print(sold_position);
        Serial.print("_E_");

        // 여기에 음성 파일 재생 코드를 추가해야 합니다.
        // playSound(sold_position);  // 음성 파일 재생 함수 호출 (해당 함수는 사용자가 정의해야 함)
      }
    }

    prevBtnState[i] = btnState[i]; // 현재 버튼 상태를 이전 버튼 상태로 업데이트
  }

  delay(50); // 버튼 입력 감지를 위한 짧은 딜레이
}

