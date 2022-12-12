# 시각장애인을 위한 자판기 / arduino
   1. 음료수를 구매할 수 있는 자판기 버튼 (Push Button으로 구현)
   2. 어떤 음료수인지 알수 있도록 손을 대면 센싱하는 터치 센서 (쿠킹 호일으로 구현)
   
   * 자판기 외형
   
   ![image](https://user-images.githubusercontent.com/119272401/207074270-7d6e85d2-d061-4794-a2fa-74f2e659be96.png)


## 시작하기에 앞서
   1. 이용하고있는 환경에서 최신버전의 [Arduiono IDE](https://www.arduino.cc/en/main/software)가 설치

   1-1. 이미 $ sudo apt-get install arduino로 깔려있다면 아래의 명령어를 통해 제거 
   ```
   $ sudo apt-get --purge remove arduino
   $ sudo apt-get autoremove
   $ sudo apt-get clean
   ```
   2. [www.arduino.cc](https://www.arduino.cc/en/Main/Software)를 방문해 Linux ARM 버전의 설치파일 다운
   (사진)
   3. 압축 해제 및 설치
   ```
   $ cd ~
   $ mkdir arduinoIDE
   $ cd ~/Downloads
   $ cp ./arduino-1.8.13-linuxarm.tar.xz ~/arduinoIDE
   $ cd ~/arduinoIDE
   $ tar xvf arduino-1.8.13-linuxarm.tar.xz
   $ cd arduino-1.8.13
   $ ./install.sh
   ```

   ```c++
   #define PIN_COUNT 6   //푸시 버튼의 수
   ```

   2. 터치 센서 연결
   * 쿠킹 호일을 이용한 터치센서 연결

   [연결방법](https://github.com/jsjjsj9710/Capstone_Design_TeamProject/tree/main/arduino/pushButton) 
   ```c++
   #include <CapacitiveSensor.h>   

   #define COMMON_PIN      2    // 모든 key에 대한 공통적인'send' pin
   #define NUM_OF_SAMPLES  10   // 읽어들이는 최소 횟수(숫자가 크면 정확도 up)
   #define NUM_OF_KEYS     6    // capacitive sensor의 수
   ```
   3. pushButton.ino와 capacitive.ino 실행
   > 주의 : 두 .ino 파일을 실행 시키기전에 RX,TX가 연결되어 있으면 오류 발생. 
   * .ino 파일을 각각 실행한 뒤 아두이노의 GND를 연결하고 푸시 버튼을 연결한 아두이노의 TX, 터치 센서를 연결한 아두이노의 RX를 연결한다.
    
# 참고한 웹 사이트
## 개발 환경

   * Arduino Uno
   * Arduino IDE @1.8.13

## 기여하기

[CONTRIBUTING.md](https://github.com/golagola2020/hango-arduino/blob/master/CONTRIBUTING.md) 를 읽으신 후 기여를 해주십시오.     
자세한 Pull Request 절차와 행동 규칙을 확인하실 수 있습니다.

## 개발자

 - **안혜수** [shehdn](https://github.com/suehdn)   

[기여자 목록](https://github.com/golagola2020/hango-arduino/graphs/contributors)을 확인하여 이 프로젝트에 참가하신 분들을 보실 수 있습니다.
