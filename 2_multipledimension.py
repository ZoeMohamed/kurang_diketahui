def FirstElement(L):
    return L[0]
def Konso(x,L):
    return [x] + L    
def Tail(L):
    return L[1:]
def Dimension(L):
    if L == []:
        return 0
    else:
        return 1 + Dimension(Tail(L))

def KaliList(L1,L2):
      if Dimension(L1) == 0:
          return []
      else:
          return Konso(FirstElement(L1) * FirstElement(L2),KaliList(Tail(L1),Tail(L2)))
print(KaliList([1,2,3],[2,3,4]))