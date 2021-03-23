#   Elyta Edenia 
#   71180391
#   Universitas Kristen Duta Wacana


# Problem
# Maria adalah seorang penggemar berat film bergenre misteri. Suatu saat dia berkeinginan untuk membuat sebuah program yang dapat mengenkripsi kalimatnya ke dalam bentuk lain sehingga hanya dia dan orang tertentu yang dapat memahami isi kalimat tersebut. Bantulah Maria dalam mewujudkan keinginannya.

# Input
    # String : ABC
    # String : ADA HANTU
# Proses
'''
    listAlpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    temp = ""
    inputan = inputan.upper()
    for karakter in inputan:
        if karakter in listAlpha:
            index = listAlpha -> cari index huruf di listAlpha
            indexTemp = (index + 2) % 26
            temp += listAlpha[indexTemp]
        else:
            temp+= karakter
'''
# Output
    # String : BCD
    # String : CFC JCPVW
# =========================================================================================
# Input
inputan = input("Masukkan kalimat yang ingin dienkripsi: ")
# Proses 
inputan = inputan.upper()
listAlpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
temp = ""
inputan = inputan.upper()
for karakter in inputan:
    if karakter in listAlpha:
        index = listAlpha.index(karakter)
        indexTemp = (index + 2) % 26
        temp += listAlpha[indexTemp]
    else:
        temp+= karakter
# Output
print("Kalimat setelah dienkripsi: "+temp)
