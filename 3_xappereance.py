def Head(T):
    
    if T !='':
        
      return T[:-1]
def Tail(T):
    
    if T != '':
            
      return T[1:]
def LastChar(T):
    if T != '':
        return T[-1]

def nbx(C,T):
    if T == '':
        return 0
    else:
        if LastChar(T) ==C : 
            return 1 + nbx(C,Head(T))
        else:
            return nbx(C,Head(T))



    
print(Head(['g','2']))
    
print(nbx('a','babai'))