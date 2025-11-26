import random
import time
from game.mole import Mole
from utils.timer import countdown

def start_game():
    print("🎮 두더지 잡기 게임 시작!")
    print("⏱ 제한 시간: 10초")
    print("두더지가 나오면 번호를 입력해서 잡으세요!")

    mole = Mole()
    score = 0

    start_time = time.time()

    while time.time() - start_time < 10:  # 10초 게임
        hole = random.randint(1, 5)
        mole.appear(hole)

        print(f"\n두더지가 {hole}번 구멍에서 나왔습니다!")

        hit = input("어디를 칠까요?(1~5): ")

        if hit.isdigit() and int(hit) == hole:
            print("🎯 명중!")
            score += 1
        else:
            print("❌ 빗나감!")

        time.sleep(0.5)

    print("\n⏳ 게임 종료!")
    print(f"⭐ 최종 점수: {score}점")
