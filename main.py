import random
import math

# 고속 거듭제곱 함수
def power(a, b, m):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m

    return result

# 진성 난수 생성 함수
def true_randint(n1, n2, count):
    first = [] # 첫 번째 의사난수 집합 배열
    for i in range(100000): # 첫 배열에 의사난수 10만 개 추가
        first.append(random.randint(n1, n2))
    
    second_array = [] # 두 번째 의사난수 집합 배열
    for i in range(len(first)): # 두 번째 의사난수 집합에 의사난수를 첫 의사난수 집합 배열의 개수만큼 추가
        second_array.append(random.randint(0, len(first) - 1)) # 의사난수의 범위: 0 ~ 첫 의사난수 집합 원소의 개수 - 1
       
    ran = []
    for i in range(count):
        index = 0
        while True: # 무한 반복
            second = random.choice(second_array) #
            index = math.ceil(power(second, 1/2, 100000) * (random.random() + 1))
            if index < len(first):
                break
        ran.append(first[index])
    return ran

def simulate():
    range_input = input("랜덤 범위를 콤마(,)로 구분지어 입력해주세요 ([n₁, n₂]): ")
    num_range = range_input.split(',')
    counts = [0] * (int(num_range[1]) + 1)
    
    repeat_count = int(input("시뮬레이션 횟수를 지정해주세요: "))
    
    ran = true_randint(int(num_range[0]), int(num_range[1]), repeat_count)
    for i in range(len(ran)):
        counts[ran[i] - 1] += 1
        print(str(i + 1) + "차:", ran[i])
        
    print("\n=====[ 시뮬레이션 결과 ]=====\n")
    
    for i in range(int(num_range[0]), (int(num_range[1]) + 1)):
        print(str(i) + ":", str(counts[i - 1]) + "회, 확률:", str((counts[i - 1] / repeat_count) * 100) + "%")
        
    print("\n시뮬레이션이 종료되었습니다.\n")
    
# 몬티홀 딜레마 함수: 
def montyhall(CHANGE, DOOR_COUNT, REPEAT_COUNT):
    success_count = 0 # 성공 횟수
    for k in range(REPEAT_COUNT): # 시뮬레이션 횟수만큼 반복
        door = [0] * DOOR_COUNT # 0: 염소, 1: 스포츠카
        spocar_idx = random.randint(0, DOOR_COUNT - 1) # 스포츠카가 있는 문의 번호를 랜덤 지정
        door[spocar_idx] = 1 # 스포츠카 위치를 문에 기록
        choice = random.randint(0, DOOR_COUNT - 1) # 첫번째 선택
        
        #print(spocar_idx)
        #print(choice)
        
        open_idxs = []
        while len(open_idxs) < DOOR_COUNT - 1: # 공개할 문의 개수 = 전체 문의 개수 - 1
            # 공개할 문의 번호가 배열에 없고, 스포츠카의 위치번호가 아니고, 처음 선택한 번호가 아니면 배열에 추가
            open_idx = random.randint(0, DOOR_COUNT) # 공개할 문의 번호 랜덤 지정
            if open_idx not in open_idxs and open_idx != spocar_idx and open_idx != choice:
                open_idxs.append(open_idx)
                
        #print(open_idx)
                
        change_choice = 0 # 바꾼 선택 번호
        if CHANGE: # 선택을 바꾼다면
            while True:
                # 바꾼 선택 번호가 처음 선택한 번호가 아니고, 공개된 문의 번호들에 포함되지 않을 때까지 무한 반복
                change_choice = random.randint(0, DOOR_COUNT)
                if change_choice != choice and change_choice not in open_idxs:
                    break
                    
            #print(change_choice)
                    
            if change_choice == spocar_idx: # 스포츠카의 위치를 맞추면
                print(str(k + 1) + "회차: 성공")
                success_count += 1 # 성공횟수 + 1
            else: #못 맞추면
                print(str(k + 1) + "회차: 실패")
        else: # 선택을 바꾸지 않으면
            if choice == spocar_idx: # 스포츠카의 위치를 맞추면
                print(str(k + 1) + "회차: 성공")
                success_count += 1
            else: # 못 맞추면
                print(str(k + 1) + "회차: 실패")
                
    print("\n시뮬레이션이 종료되었습니다.")
    print("성공 횟수:", success_count, ",", "확률:", str((success_count / REPEAT_COUNT) * 100) + "%") # 성공횟수, 확률 출력
   
   
# 사용자 입력     
while True:
    print("")
    choice = input("[입력] 큰 수의 법칙: 0, 몬티홀: 1: ")
    print("\n")
    if choice == "0":
        simulate()
    elif choice == "1":
        _choice = input("선택 바꾸기 / 바꾸지 않기 [Y / N]: ")
        door_count = 0
        while door_count < 3:
            door_count = int(input("문의 개수: "))
        repeat_count = int(input("시뮬레이션 횟수: "))
        if _choice.lower() == "y":
            montyhall(True, door_count, repeat_count)
        elif _choice.lower() == "n":
            montyhall(False, door_count, repeat_count)