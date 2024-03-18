import random

def simulate():
    range_input = input("랜덤 범위를 콤마(,)로 구분지어 입력해주세요 ([n1, n2]): ")
    num_range = range_input.split(',')
    
    first = []
    for i in range(100000):
        first.append(random.randint(int(num_range[0]), int(num_range[1])))
    
    second = []
    for i in range(100000):
        second.append(random.randint(0, 99999))
    
    ran = []
    counts = [0] * (int(num_range[1]) + 1)
    
    repeat_count = int(input("시뮬레이션 횟수를 지정해주세요: "))
    
    for i in range(repeat_count):
        ran.append(first[random.choice(second)])
        counts[ran[i] - 1] += 1
    
        print(str(i + 1) + "차:", ran[i])
    
    print("\n=====[ 시뮬레이션 결과 ]=====\n")
    for i in range(int(num_range[0]), (int(num_range[1]) + 1)):
        print(str(i) + ":", str(counts[i - 1]) + "회, 확률:", str((counts[i - 1] / repeat_count) * 100) + "%")
        
while True:
    simulate()
    retry = input("\n다시 시뮬레이션 하려면 엔터를 누르십시오.")
    print("")
        