# 시각장애인을 위한 자판기/arduino/pushButton
   * 이 리드미 파일은 푸시 버튼을 설치하고 실행하는데 도움을 주기 위해 작성되었습니다.
  
   1. 준비물   
   푸시 버튼 8개, 1k옴 저항 8개, 전선 24개

   2. 푸시 버튼 설치
   ```c++
   #define PIN_COUNT 6         // 푸시 버튼의 수

   const int PIN[PIN_COUNT] = {2, 3, 4, 5, 6, 7}; 
   ```
   현재 코드에서 사용하는 푸시 버튼은 총 6개로 각각 2,3,4,5,6,7핀에 연결되어있습니다. 
   
   사진을 참고해 연결하세요. (사진 그대로 제작할시 오류 발생 말그대로 참고)

![푸시버튼](https://user-images.githubusercontent.com/67812466/96615971-f1c33600-133c-11eb-92f4-07f6f6062b95.PNG)
    
   3. pushButton.ino 실행


  ![image](https://user-images.githubusercontent.com/117191814/207063715-66d1e96d-70b0-4657-a1be-b328b38e0f98.png)


   4. 푸쉬버튼 제작 사진 (참고)




   푸시버튼을 눌렀을 때 1E, 2E, 3E, 4E, 5E, 6E 의 숫자가 나오면 정상 작동 입니다. 
