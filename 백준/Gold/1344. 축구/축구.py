from math import comb
A = int(input())
B = int(input())

primes = [2, 3, 5, 7, 11, 13, 17]

percent_A = A/100
percent_B = B/100

answer1 = answer2 = 0
for i in primes:
    combs = comb(18,i)
    answer1 += combs * (percent_A**i) *((1-percent_A)**(18-i))
    answer2 += combs * (percent_B**i) *((1-percent_B)**(18-i))


print(answer1+answer2-answer1*answer2)