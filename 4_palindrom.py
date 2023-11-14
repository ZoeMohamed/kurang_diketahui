def Head(T):
    
    if T != []:
        
      return T[:-1]

def Konso(x, L):
    return [x] + L


def Tail(T):
    
    if T != []:
            
      return T[1:]
def LastChar(T):
    if T != []:
        return T[-1]
    
def Inverse(T):
   if T == []:
      return []
   else:
      return Konso(LastChar(T),Inverse(Head(T)))
      

def isPalindrom(T):
   
   if T == Inverse(T):
      return True
   else:
      return False
   
print(isPalindrom([]))
   
    