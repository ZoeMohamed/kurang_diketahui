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
def MinList(L):
    if IsoneElmnt(L):
        if IsAtom(FirstList(L)):
            return FirstList(L) 
        else:
            return MinList(FirstList(L))
      
    else:
        if IsAtom(FirstList(L)):
            print("xxxx")
            return Min2(FirstList(L),MinList(TailList(L)))
        else:

            print("xxx")
            return Min2(MinList(FirstList(L)),MinList(TailList(L)))
        

# print(MinList([3,[2,4,5],[6,3],[6,4,1,2],7,[21]]))
print(MinList([[22,21]]))