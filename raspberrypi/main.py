import pygame
import serial

# Arduino와 연결된 시리얼 포트 경로를 확인하세요.
# 예: "/dev/ttyACM0", "/dev/ttyUSB0"
push_button_port = "/dev/ttyACM0"
ultrasonic_port = "/dev/ttyACM1"

# 시리얼 통신 속도와 타임아웃 설정
push_button_ser = serial.Serial(push_button_port, 9600, timeout=1)
ultrasonic_ser = serial.Serial(ultrasonic_port, 9600, timeout=1)

# pygame 초기화 및 오디오 초기화
pygame.init()
pygame.mixer.init(buffer=1024)  # 버퍼 크기 조정

# 각각의 오디오 파일 경로와 오디오 객체 생성
sound_files = ["/home/rlaqudgus/Desktop/sound/success_1.wav",
               "/home/rlaqudgus/Desktop/sound/success_2.wav",
               "/home/rlaqudgus/Desktop/sound/success_3.wav",
               "/home/rlaqudgus/Desktop/sound/success_4.wav",
               "/home/rlaqudgus/Desktop/sound/success_5.wav",
               "/home/rlaqudgus/Desktop/sound/success_6.wav",
               "/home/rlaqudgus/Desktop/sound/99.wav"]
sounds = [pygame.mixer.Sound(file) for file in sound_files]

# 오디오 재생 함수
def play_sound(index):
    channel = pygame.mixer.Channel(0)
    if not channel.get_busy():
        channel.play(sounds[index])

# 거리가 20cm 이내인지 확인하는 함수
def is_within_range(distance):
    return distance <= 20

# 초음파 센서 인식 여부 플래그
ultrasonic_detected = False

# 무한 루프를 돌며 시리얼 포트에서 데이터를 받아 처리
while True:
    if push_button_ser.in_waiting > 0:
        line = push_button_ser.readline().decode("utf-8").strip()
        if line.endswith("_E_"):
            button_num = line.split("_")[0]
            button_index = int(button_num) - 1

            # 버튼에 맞는 음성 파일 재생
            play_sound(button_index)

    # 초음파 센서 아두이노에서 데이터를 받았을 때
    if ultrasonic_ser.in_waiting > 0:
        distance_str = ultrasonic_ser.readline().decode("utf-8").strip()
        distance = ''.join(filter(str.isdigit, distance_str))
        if distance:
            distance = int(distance)
            if is_within_range(distance) and not ultrasonic_detected:
                # 새로운 오디오 파일 재생 (인덱스 6번에 해당하는 소리)
                play_sound(6)
                ultrasonic_detected = True
            elif not is_within_range(distance) and ultrasonic_detected:
                ultrasonic_detected = False

# 시리얼 포트를 닫기
push_button_ser.close()
ultrasonic_ser.close()
