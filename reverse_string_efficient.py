def rreverse(s):
    if s == []:
        return s
    else:
        a = s.pop()
        return  [a] + rreverse(s)



z = rreverse(['d','p','i'])

