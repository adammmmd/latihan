# print untuk menecetak tulisan
print("hello")

# DATA TYPE
# ----- STRING -----
makanan = "nasi goreng" # string kutip dua
makanan2 = 'sop buah' # string kutip satu
makanan3 = """
pisang
strawberry
melon
"""
print(makanan) 
print(makanan2)
print(makanan3)

# ----- NUMBER -----
int = 123
complex = 1j
float = 12.2

print(type(int))
print(type(complex))
print(type(float))

# --- NONE ----

tipe_none = None

print(type(tipe_none))

# ---- Sequence ---

list_makanan = ["pisang", "melon", "nanas"] #list
print(list_makanan)
print(type(list_makanan))

# ---- SET ------
menu = {
  "makanan": "nugget",
  "minuman": "air putih"
}

print(type(menu))

# ---- Boolean -----
sekarang_jumat = True
print(type(sekarang_jumat))



# OPERATOR ARITMATIKA
# ----- Penambahan ------
penambahan = 3 + 4
print("3 + 4 =", penambahan)

# ----- Pengurangan -----
pengurangan = 5 - 3
print("5 - 3 =", pengurangan)

# ----- Pengalian ----- 
pengalian = 5 * 3
print("5 * 3", pengalian)

# ----- Pembagian -----
pembagian = 9 / 9
print("9 / 9 =", pembagian)

# ----- Modulus -----
modulus = 5 % 4
print("5 % 4 =", modulus)

# ---- Pangkat ----
pangkat = 2 ** 2
print("2 ** 2 =", pangkat)

# ---- Floor Division ----
floor = 5 // 4
print("5 // 4", floor)

# ASSIGNMENT OPERATOR
x = 5
x += 3 # penambahan
x -= 2 # pengurangan
x *= 2 # pengalian
x /= 4 # pembagian
x %= 3 # modulus

y = 15
y //= 4 # floor division
y **= 3 # pangkat
print(y)


nomor = 3 == 3
nomor1 = 3 != 3
nomor2 = 3 < 2
nomor3 = 5 > 23
nomor4 = 4 <= 4
nomor5 = 16 <= 5
print(nomor) 
print(nomor1) 
print(nomor2) 
print(nomor3) 
print(nomor4) 
print(nomor5) 


# IF/ELIF/ELSE

nilai = 60

if nilai >= 80:
  print("selamat anda A")
elif nilai > 70:
  print("selamar anda B")
else:
  print("silahkan belajar lagi")


# FOR LOOPS

makanan = ['pisang goreng', 'sop', 'soto']
for makan in makanan:
  print(makan)


# FUNCTIONS

angka = 12
def kurangdua(data):
  hasil = data - 2
  return hasil

print(kurangdua(angka))

