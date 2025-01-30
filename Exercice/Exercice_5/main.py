def add_binary(a,b):
    return bin(a+b)[2:]

def add_binary2(a,b):
    num = a + b
    bi = ''
    if num == 0 :
        return '0'
    while num > 0 : 
        bi = str(num % 2) + bi
        num = num // 2
    return bi



print(add_binary(1,3))



