#   Elyta Edenia 
#   71180391
#   Universitas Kristen Duta Wacana


# Problem
# Buatlah sebuah program yang dapat memberikan bilangan prima terdekat dari suatu bilangan yang diinputkan oleh user.

# Input
    # int 8
    # int 15
    # angka = input("Masukkan bilangan:")
# Proses
'''
    def cekPrima(n):
        prima = True
        if n<2:
            prima = False
        else:
            for i in range(2,n):
                if n%i==0:
                    prima = False
                    break
        return prima
    
    flag = True
    counter = 1
    if cekPrima(angka):
        output 1
    else:
        while flag:
            if cekPrima(angka+counter) and cekPrima(angka-counter):
                output2
                flag = False
            elif cekPrima(angka-counter):
                output3
            else cekPrima(angka+counter):    
                output4

'''
# Output
    # output1 -> Bilangan prima terdekat adalah bilangan itu sendiri (angka)
    # output2 -> Bilangan prima terdekat adalah bilangan angka+counter dan angka-counter
    # output3 -> Bilangan prima terdekat adalah bilangan angka-counter
    # output4 -> Bilangan prima terdekat adalah bilangan angka+counter
    # print -> 7
    # print -> 13 && 17

# =========================================================================================
# Input
angka = int(input("Masukkan angka yang akan digunakan: "))

# Proses & Output
def cekPrima(n):
    prima = True
    if n<2:
        prima = False
    else:
        for i in range(2,n):
            if n%i==0:
                prima = False
                break
    return prima

def cetakPrima(n):
    print("Bilangan prima terdekat adalah %d" %(n))

flag = True
counter = 1
if cekPrima(angka):
    print("Bilangan prima terdekat adalah bilangan itu sendiri (%d)"%(angka))
else:
    while flag:
        if cekPrima(angka+counter) and cekPrima(angka-counter):
            print("Bilangan prima terdekat adalah bilangan %d dan %d "%(angka+counter, angka-counter))
            flag = False
        elif cekPrima(angka-counter):
            cetakPrima(angka-counter)
            flag = False
        elif cekPrima(angka+counter):    
            cetakPrima(angka+counter)
            flag = False
        counter+=1


