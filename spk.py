
bobot = []
Rating = []
matriks = []
matriksNormalisasi = []

#fungsi
def tambahKriteria(listToAdd):
    namaKriteriaBaru = input("Nama kriteria : ")
    print ("Jenis Kriteria:\nA.Benefit\nB.Cost")
    jenisKriteriaBaru = input("Pilih jenis kriteria = ").upper()
    kriteria = (namaKriteriaBaru, jenisKriteriaBaru)
    return listToAdd.append(kriteria)

def tambahBobot(listToAdd):
    j = 0
    for j in range (len(listToAdd)):
        bobotKriteria = float(input("Bobot Kriteria "+listToAdd[j][0]+" = "))
        bobot.append(bobotKriteria)
    return bobot

def jumlahBobot(bobot):
    jum = 0
    for j in range (len(bobot)):
        jum += bobot[j]
    return jum

def ulangIsiBobot(listToRe,bobot):
    print (len(bobot))
    j = 0
    a = len (bobot)
    while (a > j):
        del bobot[a-1]
        a -= 1
    tambahBobot(listToRe)
    return bobot

def cekJumlah(jum):
    if (jum != 100):
        ulangIsiBobot(kriteria,bobot)
        jum = jumlahBobot(bobot)
        cekJumlah(jum)
    else:
        print ("Bobot sudah benar")
    return 

def tambahAlternatif(listToAdd,i):
    namaAlternatifBaru = input("Nama : ")
    alter.append(namaAlternatifBaru)
    Rating = []
    j = 0
    for j in range (len(listToAdd)):
        nilaiRating = float(input("Masukkan nilai rating pada kriteria "+listToAdd[j][0]+" = "))
        Rating.append(nilaiRating)
    matriks.append(Rating)
    return (alter, matriks)

def normalisasi (kriteria,matriks,j):
    i = 0
    matriksPerAtribut = []
    if (kriteria[j][1] == 'A'):
        maxi = matriks[i][j]
        for i in range (len(matriks)):
            if (matriks[i][j] > maxi):
                maxi = matriks[i][j]
        i=0
        for i in range (len(matriks)):
            matriksN = matriks[i][j]/maxi
            matriksPerAtribut.append(matriksN)
    else:
        mini = matriks[i][j]
        for i in range (len(matriks)):
            if (matriks[i][j] < mini):
                mini = matriks[i][j]
        i=0
        for i in range (len(matriks)):
            matriksN = mini/matriks[i][j]
            matriksPerAtribut.append(matriksN)
    return matriksPerAtribut

def nilaiPreference(matrik,bobot):
    i = 0
    nf = []
    for i in range (len(matrik)):
        j = 0
        ref = 0
        for j in range (len(bobot)):
            ref += bobot[j]/100*matrik[j][i]
        nf.append(ref)
    return nf

def pengurutan (nama,nf):
    #print("cek")
    ind = 0
    #print(nf)
    i = 0
    for i in range (len(nf)):
        #print("cek2")
        j = len(nf)-1
        while (j>=i):
            if(nf[j]>nf[j-1]):
                temp = nf[j-1]
                nf[j-1] = nf[j]
                nf[j]=temp

                #print("cek3")
                
                temp = alter[j-1]
                alter[j-1] = alter[j]
                alter[j] = temp
            j -= 1
        hasilPeringkat = (alter, nf)
        #print("cek4")
    return hasilPeringkat

#main
kriteria = []
alter = []
hasil = []

print ("SPK Penerima Beasiswa")
m = int(input("Masukkan banyak kriteria = "))
j = 0
while (j<m):
    print ("\nKriteria ke-{}".format(j+1))
    tambahKriteria(kriteria) 
    j = j+1

print ("\nMasukkan bobot setiap kriteria")

tambahBobot(kriteria)

jumlah = jumlahBobot(bobot)

cekJumlah(jumlah)

#tampilkan kriteria, jenis, dan bobot disini nanti

#inputkan alternatif
print("\n")
n = int(input("Masukkan jumlah alternatif = "))
i = 0
while (i<n):
    print ("Input Data calon penerima beasiswa ke {}".format(i+1))
    tambahAlternatif(kriteria,i)
    i += 1
    print()
    
#print(matriks)
print("============================")
print ("\nHasil Data Calon Penerima Beasiswa")
for i in range (len(alter)):
    print ("{}".format(alter[i]))
    for j in range(len(matriks[i])):
        print ("{}:{}".format(kriteria[j][0],matriks[i][j]))
    print()
    
#Hasil Normalisasi
j = 0
while (j<m):
    matriksNormalisasi.append(normalisasi(kriteria,matriks,j))
    j += 1
#print (matriksNormalisasi)
print("============================")
print ("\nHasil Normalisasi")
for i in range (len(alter)):
    print ("{}".format(alter[i]))
    for j in range(len(matriksNormalisasi[i])):
        print ("{}:{}".format(kriteria[j][0],matriksNormalisasi[j][i]))
    print()

hasilPreference = nilaiPreference(matriksNormalisasi,bobot)
#print (hasilPreference)
print("============================")
print ("\nHasil Preference")
print ("Nama   |  Nilai")
for i in range (len(hasilPreference)):
                print("{}    |   {}  ".format(alter[i],hasilPreference[i]))
print()

#sisa sorting yang belum
print("============================")
hasil = pengurutan (kriteria,hasilPreference)
print ("\nHasil Pengurutan")
print ("Nama   |  Nilai")
for i in range (len(hasil[0])):
                print("{}    |   {}  ".format(hasil[0][i],hasil[1][i]))
print()

banyak = int (input("Jumlah penerima beasiswa = "))
print ("Maka penerima beasiswa adalah : ")
for i in range (banyak):
    print("{}.{}".format(i+1, hasil[0][i]))
