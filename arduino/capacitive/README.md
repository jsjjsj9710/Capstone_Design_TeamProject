# 시각장애인을 위한 자판기/arduino/capacitive
   * 이 파일은 터치 센서를 설치하고 실행하기위한 순서를 알려줍니다.
   
 1.준비물  
   쿠킹 호일 6개, 1MΩ 저항 6개, 전선 12개  
     -저항은 1 MΩ 에서 4.7 MΩ 사이 저항 사용. 
   
   arduino IDE에서 '라이브러리포함하기'를 통해 CapacitiveSensor.h를 다운로드 받아 놓습니다.
   
   1.1 Char2Int 라이브러리를 아두이노의 라이브러리에 넣은 뒤
   ```
   #include <Char2Int.h>
   ```
   불러옵니다.
  
   2.터치 센서 설치
   ```c++
   #include <CapacitiveSensor.h>

   #define COMMON_PIN      2    // 모든 key에 대한 공통적인'send' pin
   #define NUM_OF_SAMPLES  10   // 읽어들이는 최소 횟수 (숫자가 클수록 정확도가 올라갑니다)
   #define NUM_OF_KEYS     6    // capacitive sensor의 수

   // 각 터치센서에 키 지정
   #define CS(Y) CapacitiveSensor(2, Y)

   CapacitiveSensor keys[] = {CS(9), CS(7), CS(6), CS(5), CS(4), CS(3)};;
   ```
   현재 코드에서 사용하는 터치 센서는 총 8개로 각각 3,4,5,6,7,9핀에 연결되어 있습니다.  
   모든 터치 센서에 대한 공통적인 전송핀은 2번핀에 연결됩니다.

- 전체적인 구조(X 모양의 부위는 서로 연결되었다는 뜻(납땜))

![터치센서](https://user-images.githubusercontent.com/67812466/96829064-c727c900-1473-11eb-977f-d28c495047ba.PNG)


- 납땜 방식
<img src="https://user-images.githubusercontent.com/67812466/96612452-ba528a80-1338-11eb-9885-7bc12c7d2b5c.png" width="500">

- 터치센서 쿠킹 호일과 연결하는 법
![터치센서만들기](https://user-images.githubusercontent.com/67812466/96615124-dd326e00-133b-11eb-84cb-f929c6f1a710.PNG)
   
   > 쿠킹호일을 3,4,5,6,8,9번 핀과 연결하는 전선중 하나와 연결된 저항의 다리로 통과시킨다.  
   > 쿠킹호일과 통과시킨 저항을 밀착시킨다.(밀착되지 않으면 제대로 동작 x)  
   > 쿠킹호일을 절연테이프로 고정한다.    

   완성된 모습은 위의 '전체적인 구조' 사진과 같습니다.  
   
   3.captest.ino 파일 실행을 통한 정상 동작 확인  

   captest.ino를 통해 터치센서가 제대로 동작하는지 확인할 수 있습니다.  
   
   Tool의 Serial Moniter를 켜면  
   - 터치센서를 누르지 않았을 때
![캡처1](https://user-images.githubusercontent.com/67812466/96619551-449eec80-1341-11eb-98f3-4e6ba00486ea.PNG)  
   - 터치센서를 눌렀을 때   
![캡처2](https://user-images.githubusercontent.com/67812466/96619556-47014680-1341-11eb-9586-329a28cd106f.PNG)  

두가지 상황을 쉽게 볼 수 있습니다.
