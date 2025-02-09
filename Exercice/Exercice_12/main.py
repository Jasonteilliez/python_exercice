def prime_factor(num):
    factors = set()
    factor = 3

    while num % 2 == 0 :
        factors.add(2)
        num = num // 2

    while abs(num) >= 3:
        if (num % factor == 0) :
            factors.add(factor)
            num = num / factor
        else :
            factor += 2  
    return factors

def sum_for_list(lst):
    list_dict = dict()
    for x in lst:
        prime = prime_factor(x)
        for y in prime:
            if y in list_dict.keys():
                list_dict[y] += x
            else:
                list_dict[y] = x
    return [[key, value] for key, value in sorted(list_dict.items())]


print(sum_for_list([15,21,24,30,-45]))
