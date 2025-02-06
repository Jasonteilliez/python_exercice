def digital_root(n):
    while n > 9 :
        n = sum (int(x) for x in str(n))
    return n

def digital_root2(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

def digital_root3(n):
	return n%9 or n and 9 

print(digital_root3(493193))
