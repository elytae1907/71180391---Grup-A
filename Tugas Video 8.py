#   Elyta Edenia 
#   71180391
#   Universitas Kristen Duta Wacana


# Problem
# Pius mempunyai sekumpulan file berisi kata atau kalimat yang diduga beberapa diantaranya adalah palindrom. Tugasmu kali ini adalah untuk mengecek setiap kata/kalimat yang ada dan memberikan keterangan apakah kata/kalimat tersebut adalah palindrom atau bukan.

# Input
    # String -> file 
    # file wordList.txt
# Proses
'''
    handle = open file inputan user
    handle2 = open result.txt
    temp -> 123kasurusak
    temp2 -> kasurusak321
    counter=0
    for line in handle:
        line2 = line.lower()
        for c in line2:
            if c.isalnum():
                temp+=c
        temp2 = temp[-1:0:-1] + temp[0]
        if temp==temp2:
            handle2.write(line + "\t adalah Palindrom!")
            counter+=1
''' 
# Output
    # print(Ada %d palinrom dalam file tersebut!) 
# =========================================================================================
# Input
namaFile = input("Masukkan nama file: ")

# Proses 
handle = open(namaFile)
handle2 = open("result.txt","w")
temp = ""
temp2 = ""
counter = 0
for line in handle:
    line2 = line.lower()
    for c in line2:
        if c.isalnum():
            temp+=c
    temp2 = temp[-1:0:-1]+temp[0]
    if temp==temp2:
        handle2.write(line)
        counter+=1
    temp=""
    temp2=""

handle.close()
handle2.close()
# Output
print("Ada %d palindrom di file tersebut"%(counter))
