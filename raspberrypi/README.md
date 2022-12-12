# 시각장애인을 위한 자판기 raspberrypi

  * 이 리드미 파일은 라즈베리파이를 통해 아두이노의 감지 데이터를 수신하고, 데이터를 가공하여 스피커로 출력하는 방법을 설명하기 위해 작성되었습니다.

# 시작하기에 앞서

프로젝트를 실행시키기 위한 도구 및 프로그램 설치

1.pip 설치
```
$ sudo apt-get install python-pip
```

2.virtualenv 설치
```
$ sudo pip install virtualenv
```

# 설치

### 가상환경 만들기
(패키지 충돌을 방지하기 위해 가상환경에 설치하는 것을 권장합니다.)
```
$ virtualenv hango-raspberry
$ cd hango-raspberry
$ source bin/activate
```

* https://github.com/golagola2020/hango-raspberry-pi 에 push 권한이 있다면 :  
   * git fetch or pull or clone
      ```
      $ git clone https://github.com/golagola2020/hango-raspberry-pi.git
      $ cd hango-server
      ```
  * https://github.com/golagola2020/hango-raspberry-pi 에 push 권한이 없다면 :  
   1. https://github.com/golagola2020/hango-raspberry-pi 에서 ```Fork```버튼 클릭하고,
   2. 포크 저장소 계정(maybe 개인 계정) 선택
   3. git fetch or pull or clone
      ```
      # 포크한 저장소 clone
      $ git clone https://github.com:YOUR_GITHUB_ACCOUNT/hango-raspberry-pi.git
      $ cd hango-server

      # hango-server 레포지터리를 upstream으로 리모트 설정
      $ git remote add upstream https://github.com/golagola2020/hango-raspberry-pi.git

      # 로컬 코드와 hango-server 동기화
      $ git fetch upstream
      $ git checkout master
      $ git merge upstream/master
      ```
