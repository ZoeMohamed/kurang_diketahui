def MakePoint(x, y):
    return [x, y]

def Absis(x):
    return x[0]

def Ordinat(y):
    return y[1]

def Tail(x):
    if x != []:
        return x[1:]

def FirstElmt(x):
    if x != []:    
        return x[0]

def IsEmpty(x):
    if x == []:
        return True
    else:
        return False

def Min(x, y):
    if x > y:
        return y
    else:
        return x

def jarak(x, y):
    return MakePoint(abs(Absis(x) - Absis(y)), abs(Ordinat(x) - Ordinat(y)))

def jarak2(x, y):
    return Min(x, jarak(x, y))

def NearestPoint2(x, y, w, z):
    if IsEmpty(y):
        return w
    else:
        if jarak2(x, FirstElmt(y)) < z:
            return NearestPoint2(x, Tail(y), FirstElmt(y), jarak2(x, FirstElmt(y)))
        else:
            return NearestPoint2(x, Tail(y), w, z)

def NearestPoint(x, y):
    if IsEmpty(y):
        return MakePoint(0, 0)
    else:
        return NearestPoint2(x, Tail(y), FirstElmt(y), jarak2(x,FirstElmt(y)))

print(NearestPoint(MakePoint(6, 2), [MakePoint(2, 0), MakePoint(-4, 4), MakePoint(6, 7), MakePoint(1, 2), MakePoint(2, 1) ]))