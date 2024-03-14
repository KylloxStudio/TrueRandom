import random

first = []
for i in range(100):
    first[i] = random.randint(0, 1)

second = []
for i in range(100):
    second[i] = random.randint(0, 99)

ran = []
counts = []

repeat_count = int(input("시뮬레이션 횟수를 지정해주세요: "))
for i in range(repeat_count):
    ran[i] = first[random.choice(second)]
    counts[ran[i] - 1] += 1

    print(i + "차:", ran[i])

print("=====[ 시뮬레이션 결과 ]=====")
for i in range(len(counts)):
    print(i + ":", counts[i] + "회, 확률", (counts[i] / repeat_count) * 100 + "%")
