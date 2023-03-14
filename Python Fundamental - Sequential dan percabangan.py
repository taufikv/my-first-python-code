"""
Semua sintaksis dasar bahasa pemograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu berkata, "pergi ke toko"')
print('Ahmad menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telur beli 6"')
print("Maka Ahmad pergi ke toko")
print("Dan mulai")

print("=" * 10)

# Percabangan

print('\nIbu berkata "Beli 1 botol susu dan 6 butir telur"')
print('Anak menjawab "Ok"')
print('Anak pergi ke toko')
print('Dan mulai berbelanja')

jumlah_botol_susu = 75
jumlah_telur      = 89
print(f'Jumlah botol susu {jumlah_botol_susu} botol')
print(f'Jumlah Telur {jumlah_telur} butir')

print('=' * 30)
if jumlah_botol_susu > 0:
    print('anak mengecek harganya,dan ternyata uangnya cukup')
    if jumlah_telur == 0:
        print('anak membeli 1 botol susu')
    else:
        print('anak membeli 1 botol susu dan 6 butir telur')
else:
    print('anak tidak jadi membeli susu')
print('=' * 30)

print('\nanak pulang kerumah')
print('Menyerahkan hasil belanjanya kepada ibu')
