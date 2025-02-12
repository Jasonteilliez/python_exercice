def solution(args):
    response = ""
    start=args[0]
    finish=args[0]
    for arg in args[1:]+[""]:
        if arg != finish + 1:
            if finish == start:
                response +=",{}".format(start)
            if finish == start+1:
                response += ",{},{}".format(start,finish)
            if finish > start+1:
                response += ",{}-{}".format(start,finish)
            start=arg
        finish=arg
    return response[1:]


def solution2(args):
    out = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(out)


print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
print(solution([-3,-2,-1,2,10,15,16,18,19,20]))
print(solution([-72, -70, -68, -65, -63, -62, -60, -59, -56, -54, -53, -50, -47, -45, -42, -40, -39, -36, -35, -34, -31, -28, -26, -24, -23, -21, -18]))

# -6,-3-1,3-5,7-11,14,15,17-20
# -3--1,2,10,15,16,18-20
# -72,-70,-68,-65,-63,-62,-60,-59,-56,-54,-53,-50,-47,-45,-42,-40,-39,-36--34,-31,-28,-26,-24,-23,-21,-18 