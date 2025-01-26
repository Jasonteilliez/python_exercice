def solution1(number):
    sum = 0
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0 :
            sum += x
    return sum

def solution2(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

def solution3(number):
    if number < 0:
        return 0
    a3 = (number-1)//3
    a5 = (number-1)//5
    a15 = (number-1)//15
    return int((a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15)

def solution4(number):
    return sum({*range(3, number, 3), *range(5, number, 5)})


number = 10
print("Pour number =",number)
print("Solution 1 :",solution1(number))
print("Solution 2 :",solution2(number))
print("Solution 3 :",solution3(number))
print("Solution 4 :",solution4(number))



