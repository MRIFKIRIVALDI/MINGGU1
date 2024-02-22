#diskon di indomaret
belanja = float(input("Masukan total belanja anda : "))
keterangan = ""

if belanja > 60_000 :
    diskon = belanja * 10/100
    total = belanja - diskon
    keterangan = " Anda mendapatkan diskon sebesar 10% karena belanja lebih dari 60.000"
else:
    total = belanja
    keterangan = " Anda tidak mendapatkan diskon apapun, jika anda belanja lebih dari 60.000 maka anda mendapat diskon 10%"

print(" total belanjaan anda adalah %i rupiah "% total + keterangan)        