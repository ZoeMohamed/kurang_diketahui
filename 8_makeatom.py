def IsAtom(L):
    return type(L) != list

def Tail(L):
    return L[1:]
def TailList(L):
    return L[1:]

def NbElmnt(L):
    if L == []:
        return 0
    else:
        return 1 + NbElmnt(Tail(L))
def IsoneElmnt(L):
    if NbElmnt(L) == 1:
        return True
    else:
        return False
def FirstList(L):
    return L[0]
def Min2(a,b):
    if a<=b:
        return a
    else:
        return b

def Head(L):
    return L[:-1]
def LastElement(L):
    return L[-1]
def Konso(x,L):
    return [x] + L
def addinglist(L):
    if L == []:
        return 0
    else:
        return LastElement(L) + addinglist(Head(L))
    # 3 + [1,2]
    # 2 + [1]
    # 1 + 0

def MakeListAtomRec(S):
    if S == []:
        return []
    else:
        if IsAtom(FirstList(S)):
            return [FirstList(S)] + MakeListAtomRec(TailList(S))
        else:
            return [SumList(FirstList(S))] + MakeListAtomRec(TailList(S))

def SumList(L):
    if L == []:
        return 0
    else:
        return FirstList(L) + SumList(TailList(L))
    
print(MakeListAtomRec([3,[2,4,5],[1,3],[6,4,1,2],7,[2]]))

print([3,4] + [2,3])