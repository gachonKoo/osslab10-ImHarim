import sys

# 명령줄 인자로 받은 수를 정수로 변환
number = int(sys.argv[1])

# 1부터 number까지 순회하며 나누어 떨어지는 수를 찾기
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")

print()
