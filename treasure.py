import random

"""
random.randint(a, b): a부터 b까지의 정수 중에서 랜덤한 값을 반환하는 함수
random.choice(리스트): 특정 리스트에서 랜덤하게 선택

그리드 = (행, 열),(x, y) 형태로 구성
그리드 예)
3X3 그리드일 때
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
초기 위치: x = 1, y = 1 → (1,1)
북쪽으로 이동: x -= 1 → (0,1)
남쪽으로 이동: x += 1 → (2,1)
동쪽으로 이동: y += 1 → (1,2)
서쪽으로 이동: y -= 1 → (1,0)


"""

#N x N (5-10)크기의 그리드 생성
N = random.randint(5, 10)

#보물, 플레이어 위치 랜덤 배정
treasure_x, treasure_y = random.randint(0, N - 1), random.randint(0, N - 1)
player_x, player_y = random.randint(0, N - 1), random.randint(0, N - 1)

#플레이어와 보물이 같은 위치에 걸릴 경우 플레이어 초기 위치 다시 배정
while (player_x, player_y) == (treasure_x, treasure_y):
    player_x, player_y = random.randint(0, N - 1), random.randint(0, N - 1)

move_count = 0 #플레이어가 움직인 횟수

"""
맨해튼거리: 두 점 사이의 이동 거리(경로)를 계산하는 방식 / 대각선 이동 없이 "가로 + 세로"만 이동할 수 있다고 가정
공식: D = |x1 - x2|+|y1 - y2|
abs(): 절댓값을 반환하는 함수
"""
#보물과 플레이어 사이의 맨해튼거리 계산
def calculate_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def initialize_game():
    for i in range(N):
        for j in range(N):
            if (i, j) == (player_x, player_y): #플레이어위치표시
                print("P", end=" ") 
            elif (i, j) == (treasure_x, treasure_y) and found_treasure:
                print(" X", end=" ") 
            else:
                print("__", end=" ")  
        print()
    print()

print(f"💎보물을 찾아보세요💎")
found_treasure = False  #보물을 찾았는지 여부를 저장
initialize_game()

while True:
    distance = calculate_distance(player_x, player_y, treasure_x, treasure_y)
    print(f"📍 현재 보물까지의 거리: {distance}")

 
    """
    .upper(): 문자열의 모든 문자를 대문자로 반환/사용자가 입력한 값을 대소문자 구분 없이 처리할 때 유용
    """
    #플레이어입력
    move = input("이동할 방향을 입력하세요 (W: 북, S: 남, D: 동, A: 서): ").upper() 
    if move == "W" and player_x > 0:
        player_x -= 1
    elif move == "S" and player_x < N - 1:
        player_x += 1
    elif move == "D" and player_y < N - 1:
        player_y += 1
    elif move == "A" and player_y > 0:
        player_y -= 1
    else:
        print("🚫해당 방향으로 이동할 수 없습니다🚫") #잘못 입력시 다시 방향 입력받음
        continue  

    move_count+=1

    # 보물 찾았을 때
    if (player_x, player_y) == (treasure_x, treasure_y):
        found_treasure = True
        print(f"💎보물을 찾았습니다💎 ({treasure_x}, {treasure_y})")
        print(f"총 이동 횟수: {move_count}")
        initialize_game()  
        break

 
    initialize_game()

