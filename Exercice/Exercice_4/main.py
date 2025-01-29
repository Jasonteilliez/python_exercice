def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

def create_phone_number2(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number3(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

def create_phone_number4(n):
    return "(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n)

print(create_phone_number2([1,2,3,4,5,6,7,8,9,0]))




