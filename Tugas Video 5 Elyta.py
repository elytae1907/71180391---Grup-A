#   Elyta Edenia 
#   71180391
#   Universitas Kristen Duta Wacana


# Problem
# Ika adalah siswi salah satu SMA di Yogyakarta. Dia adalah siswi yang malas terutama ketika mata pelajaran matematika. Salah satu hal yang paling tidak disukai adalah tentang mencari faktor dari sebuah angka. Sebagai teman yang baik, bantulah Ika dalam menyelesaikan permasalahannya itu.

# Input
    # input int 12 -> 1, 2, 3, 4, 6, 12
    # input int 3 -> 1, 3
# Proses
'''
    counter = 0
    temp = ""
    for i=1;i<=angka;i++{
        if angka%i==0{
            faktor dari angka tersebut
            temp = temp + " " + str(i)
            counter+=1
        }
    }
'''
# Output
    # print(angka mempunyai x faktor yaitu temp)

# =========================================================================================
# Input
print("Selamat Datang Ika")
angka = int(input("Masukkan bilangan yang ingin dicari faktornya: "))

# Proses 
counter = 0
temp = ""
for i in range(1,angka+1):
    if angka%i==0:
        temp = temp + " " + str(i)
        counter+=1

# Output
print("Angka %d mempunyai %d buah faktor yaitu %s" %(angka, counter, temp))
