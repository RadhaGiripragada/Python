""" this python program will accept n number of integers from user, where n is user's choice. Finds the max of product of any two given numbers :EX2
"""

n=int(raw_input("Enter n :"))

numbers = [int(x) for x in raw_input().split()]
assert[len(numbers)==n]

result=0

for i in range(0,n):
    for j in range(i+1, n):
        if numbers[i]*numbers[j] > result:
            result = numbers[i]*numbers[j]
print(result)


