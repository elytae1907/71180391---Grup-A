#   Elyta Edenia 
#   71180391
#   Universitas Kristen Duta Wacana


# Problem
# Pius mendapatkan tugas untuk mencari 3 jenis ikan mana yang paling sering dibeli dan 3 paling jarang dibeli di toko ikan miliknya. Data yang dia miliki hanyalah berupa list nama jenis ikan yang sudah dibeli oleh pembeli. Bantu Pius dalam menyelesaikan persoalannya. 

# Input
    # ikan = ["Bawal","Patin","Nila","Lele","Lele","Gurameh","Bawal","Lele","Patin","Tengiri","Bandeng","Bandeng","Tengiri","Lele","Bandeng","Gurameh","Bandeng","Lele","Layur","Tengiri","Tengiri","Bandeng","Bandeng","Tengiri","Lele","Bandeng","Gurameh","Bandeng","Lele","Bawal", "Layur","Tengiri","Tengiri","Bandeng","Bandeng","Tengiri","Lele","Bandeng","Gurameh","Bandeng","Lele","Bawal","Kakap","Mujair","Kakap","Tongkol","Teri","Gurameh","Bandeng","Lele","Bawal","Kakap","Gurameh","Bandeng","Lele","Bawal","Kakap","Gurameh","Bandeng","Lele","Bawal","Kakap","Tengiri","Lele","Bandeng","Gurameh","Bandeng","Lele","Layur","Tengiri","Mujair","Kakap","Tongkol"]
# Proses
'''
tempList = []
temp = []
for i in ikan:
    freq = ikan.count(i)
    if i not in tempList:
        itemIkan = {
            'nama' : i,
            'jumlah' : freq
        }
        temp.append(itemIkan)
        tempList.append(i)

temp2 = sort(temp berdasarkan key jumlah)
''' 
# Output
    # print(Tiga jenis ikan yang paling sering dibeli adalah Bawal(7), Lele(12))
    # print(Tiga jenis ikan yang paling jarang dibeli adalah Nila(1), Gurameh(2))

# =========================================================================================
# Input
from operator import itemgetter

ikan = ["Bawal","Patin","Nila","Lele","Lele","Gurameh","Bawal","Lele","Patin","Tengiri","Bandeng","Bandeng","Tengiri","Lele","Bandeng","Gurameh","Bandeng","Lele","Layur","Tengiri","Tengiri","Bandeng","Bandeng","Tengiri","Lele","Bandeng","Gurameh","Bandeng","Lele","Bawal", "Layur","Tengiri","Tengiri","Bandeng","Bandeng","Tengiri","Lele","Bandeng","Gurameh","Bandeng","Lele","Bawal","Kakap","Mujair","Kakap","Tongkol","Teri","Gurameh","Bandeng","Lele","Bawal","Kakap","Gurameh","Bandeng","Lele","Bawal","Kakap","Gurameh","Bandeng","Lele","Bawal","Kakap","Tengiri","Lele","Bandeng","Gurameh","Bandeng","Lele","Layur","Tengiri","Mujair","Kakap","Tongkol"]

# Proses 
tempList = []
temp = []
for i in ikan:
    freq = ikan.count(i)
    if i not in tempList:
        itemIkan = {
            'nama' : i,
            'jumlah' : freq
        }
        temp.append(itemIkan)
        tempList.append(i)

temp2 = sorted(temp, key=itemgetter('jumlah'))

# Output
print("Tiga jenis ikan yang jarang dibeli adalah %s(%d), %s(%d), dan %s(%d)" %(temp2[0]['nama'],temp2[0]['jumlah'],temp2[1]['nama'],temp2[1]['jumlah'],temp2[2]['nama'],temp2[2]['jumlah']))
print("Tiga jenis ikan yang sering dibeli adalah %s(%d), %s(%d), dan %s(%d)" %(temp2[-1]['nama'],temp2[-1]['jumlah'],temp2[-2]['nama'],temp2[-2]['jumlah'],temp2[-3]['nama'],temp2[-3]['jumlah']))