#   Elyta Edenia 
#   71180391
#   Universitas Kristen Duta Wacana


# Problem
# Pius mendapatkan tugas untuk mencari jenis ikan mana yang paling sering dibeli dan paling jarang dibeli di toko ikan miliknya. Data yang dia miliki hanyalah berupa list nama jenis ikan yang sudah dibeli oleh pembeli. Bantu Pius dalam menyelesaikan persoalannya. 

# Input
    # ikan = ["Bawal","Patin","Nila","Lele","Lele","Gurameh","Bawal","Lele","Patin","Tengiri","Bandeng","Bandeng","Tengiri","Lele","Bandeng","Gurameh","Bandeng","Lele","Layur","Tengiri"]
# Proses
'''
namaIkanSering = ""
namaIkanJarang = ""
sering = 0
jarang = 100
for i in ikan:
    freq = ikan.count(i)
    if sering < freq:
        sering = freq
        namaIkanSering = i
    if jarang > freq:
        jarang = freq
        namaIkanJarang = i
''' 
# Output
    # print("Jenis ikan yang paling sering dibeli oleh pembeli di Toko Ikan milik Pius adalah %s" %(namaIkanSering))
    # print("Jenis ikan yang paling jarang dibeli oleh pembeli di Toko Ikan milik Pius adalah %s" %(namaIkanJarang))

# =========================================================================================
# Input
ikan = ["Bawal","Patin","Nila","Lele","Lele","Gurameh","Bawal","Lele","Patin","Tengiri","Bandeng","Bandeng","Tengiri","Lele","Bandeng","Gurameh","Bandeng","Lele","Layur","Tengiri","Tengiri","Bandeng","Bandeng","Tengiri","Lele","Bandeng","Gurameh","Bandeng","Lele","Bawal", "Layur","Tengiri","Tengiri","Bandeng","Bandeng","Tengiri","Lele","Bandeng","Gurameh","Bandeng","Lele","Bawal"]

# Proses 
namaIkanSering = ""
namaIkanJarang = ""
sering = 0
jarang = 100
for i in ikan:
    freq = ikan.count(i)
    if sering < freq:
        sering = freq
        namaIkanSering = i
    if jarang > freq:
        jarang = freq
        namaIkanJarang = i

# Output
print("Jenis ikan yang paling sering dibeli oleh pembeli di Toko Ikan milik Pius adalah %s dengan %d penjualan" %(namaIkanSering, sering))
print("Jenis ikan yang paling jarang dibeli oleh pembeli di Toko Ikan milik Pius adalah %s dengan %d penjualan" %(namaIkanJarang, jarang))