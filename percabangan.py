#if dan else: mengambil keputusan
nilai = 80

if nilai >= 75:
    print("Selamat, kamu lulus!")
else:
      print("Ayo remedial dulu")

print("Program selesai")

#if – elif – else: Banyak Kondisi
nilai = 78

if nilai >= 85:
     grade = "A"
elif nilai >= 70:
     grade = "B"
elif nilai >= 55:
     grade = "C"
else:
    grade = "D"

print(f"Nilai {nilai} → grade {grade}")

#Nested if, Ternary & match-case

#NESTED IF — if di dalam if
umur, ktp = 20, True
if umur >= 17:
    if ktp:
        print("Boleh memilih")
    else:
        print("Buat KTP dulu")

#TERNARY — if dalam satu baris
umur = 16
s = "dewasa" if umur >= 17 else "anak"
print(s)   # anak

#MATCH-CASE — Python 3.10+
hari = "sabtu"

match hari:
    case "sabtu" | "minggu":
        print("Libur!")
    case "senin":
        print("Semangat!")
    case _:
        print("Hari kerja")



    




    