hari_kerja = int(input("Berapa hari anda kerja :"))
gaji_bulanan = int(input("Masukan gaji pokok anda :"))
uang_transport = int(input("Berapa uang transportasi anda :"))
uang_makan = int(input("Masukan uang makan pokok anda : "))

total_transport = uang_transport * hari_kerja
total_makan = uang_makan * hari_kerja

lembur = int(input("Berapa jam anda lembur :"))

if lembur <= 2 : 
    total_lembur = lembur * 100_000
elif lembur <= 7 :
    lembur = lembur - 2
    total_lembur = (lembur * 150_000 ) + 200_000

else :
    lembur = lembur - 7
    total_lembur = (lembur * 200_000) + 950_000

hasil = gaji_bulanan + total_transport + total_makan + total_lembur
print("TOTAL HONOR ANDA ADALAH :" + str(hasil))