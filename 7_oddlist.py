def FirstList(L):
    return L[0]
def IsAtom(L):
    return type(L) != list
def IsEmpty(L):
    return L == []
def TailList(L):
    return L[1:]

def NBOdds(S):
    # mengembalikan banyaknya elemen atom bernilai ganjil yang ada pada sebuah list of list
    # jika list kosong, maka akan mengembalikan nilai 0
    if IsEmpty(S): # jika list kosong
        return 0 # kembalikan 0
    elif IsAtom(FirstList(S)): # jika elemen pertama list adalah atom
        if FirstList(S) % 2 == 1: # jika atom tersebut ganjil
            return 1 + NBOdds(TailList(S)) # tambahkan 1 dan lanjutkan ke elemen berikutnya
        else: # jika atom tersebut genap
            return NBOdds(TailList(S)) # lanjutkan ke elemen berikutnya tanpa menambahkan
    else: # jika elemen pertama list adalah list
        return NBOdds(FirstList(S)) + NBOdds(TailList(S)) # jumlahkan hasil dari list tersebut dan elemen berikutnya
    

print(NBOdds([3,[2,4,5],[6,3],[6,4,1,2],7,[21]]))
