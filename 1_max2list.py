def FirstElement(L):
    return L[0]
def Konso(x,L):
    return [x] + L
def Tail(L):
    return L[1:]

def Rember(x,L):
    if L == []:
        return L
    else:
        if FirstElement(L) == x :
            return Tail(L)
        else:
            return Konso(FirstElement(L),Rember(x,Tail(L)))

def max2(a,b):
    if a > b:
        return a
    else:
        return b
def IsoneElmnt(L):
    if L == []:
        return False
    elif Tail(L) != []:
        return False
    else:
        return True
       
def maxList(L):
    if IsoneElmnt(L):
        return FirstElement(L)
    else:
        return max2(FirstElement(L),maxList(Tail(L)))

        
def MaxList2(L):
    return maxList(Rember(maxList(L),L))
    
print(MaxList2([1,2,3,4]))


# def FirstElement(L):
#     return L[0]
# def Konso(x,L):
#     return [x] + L
# def Tail(L):
#     return L[1:]

# def Insert(x,L):
#     if L == []:
#         return [x]
#     else:
#         if (x <= FirstElement(L) ):
#             return Konso(x,L)
#         else:
#             return Konso(FirstElement(L),Insert(x,Tail(L)))
# def Insort(L):
#     if L == []:
#         return []
#     else:
#         return Insert(FirstElement(L),Insort(Tail(L)))
    
# def MaxList2(L):
#     return Insort(L)[-2]
    
# print(MaxList2([1,2,3,4]))


#  def LastElement(L):
#     return L[-1]


# def Head(L):
#     return L[:-1]


# def Konsi(x, L):
#     return L + [x]


# def Konso(x, L):
#     return [x] + L


# def max2(a, b):
#     if a > b:
#         return a
#     else:
#         return b


# def max2List(a, b):
#     if b == []:
#         return a
#     else:
#         return max2(a, max2List(a, Head(b)))


# def NbElmnt(L):
#     if L == []:
#         return 0
#     else:
#         return 1 + NbElmnt(Head(L))


# def MaxList2(L):
#     # Sorting dar kecil sampai besar ambil ke [-2]
#     if NbElmnt(L) == 1:
#         return LastElement(L)

#     else:
#         return max2(LastElement(L), MaxList2(Head(L)))  # return max2(8,[3,1])
#         #  return max2(1,[3])
#         #  return 3

#         #  return max2(LastElement(3),MaxList2([1,2]))
#         #  return max2(LastElement(2),MaxList2([1]))


# def MaxList3(L):
#     # Sorting dar kecil sampai besar ambil ke [-2]
#     if NbElmnt(L) == 0:
#         return []

#     else:
#         return Konso(max2List(LastElement(L), MaxList3(Head(L))), MaxList3(Head(L)))


# print(MaxList2([3, 1, 8]))


# [1, 2, 3].sort()[-2]


# def findLargest(arr):
#     secondLargest = 0
#     largest = min(arr)

#     for i in range(len(arr)):
#         if arr[i] > largest:
#             secondLargest = largest
#             largest = arr[i]
#         else:
#             secondLargest = max(secondLargest, arr[i])

#     # Returning second largest element
#     return secondLargest


# print(findLargest([1, 2, 3]))
