# Fibonacci Sequence #

list_fibonacci = [0, 1]
n = int(input("how many numbers of fibonacci sequence do you want: "))

for i in range(2, n):
    next_num = list_fibonacci[-1] + list_fibonacci[-2]
    list_fibonacci.append(next_num)

print(list_fibonacci)
