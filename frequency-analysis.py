# SOAL 3: Analisis Frekuensi
# Ciphertext: Monoalphabetic Substitution

def frequency_analysis(ciphertext):
    """Menghitung frekuensi huruf"""
    freq = {}
    total = len(ciphertext)
    
    for char in ciphertext:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    
    # Urutkan berdasarkan frekuensi
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_freq, total

def decrypt_substitution(ciphertext, mapping):
    """Dekripsi menggunakan mapping yang diberikan"""
    plaintext = ""
    for char in ciphertext:
        if char in mapping:
            plaintext += mapping[char]
        else:
            plaintext += char
    return plaintext

# Main Program
ciphertext = "ZITJXUFNZITVXFGQGMTRJXUBMEKZITOQFNJXUZDGMEKZITUFNBMEKJXUVXFGQGMTR"

print("="*70)
print("SOAL 3: ANALISIS FREKUENSI - MONOALPHABETIC SUBSTITUTION")
print("="*70)
print(f"Ciphertext: {ciphertext}")
print()

# Hitung frekuensi
freq_data, total = frequency_analysis(ciphertext)

print("Tabel Frekuensi:")
print("-"*50)
print(f"{'Huruf':<10} {'Frekuensi':<12} {'Persentase':<15}")
print("-"*50)

for char, count in freq_data:
    percentage = (count / total) * 100
    print(f"{char:<10} {count:<12} {percentage:.2f}%")

print("-"*50)
print()

# Frekuensi huruf bahasa Inggris (sebagai referensi)
print("Referensi Frekuensi Bahasa Inggris:")
print("E(12.7%), T(9.1%), A(8.2%), O(7.5%), I(7.0%), N(6.7%)")
print("S(6.3%), H(6.1%), R(6.0%), D(4.3%), L(4.0%), U(2.8%)")
print()

# Mapping berdasarkan analisis
mapping = {
    'Z': 'T', 'J': 'A', 'T': 'N', 'X': 'O', 'U': 'D',
    'F': 'I', 'G': 'S', 'M': 'H', 'E': 'R', 'K': 'E',
    'I': 'W', 'V': 'L', 'Q': 'U', 'D': 'G', 'O': 'C',
    'N': 'F', 'R': 'Y', 'B': 'B'
}

print("Mapping yang Digunakan:")
print("-"*30)
for cipher, plain in sorted(mapping.items()):
    print(f"{cipher} → {plain}")
print("-"*30)
print()

# Dekripsi
plaintext = decrypt_substitution(ciphertext, mapping)
print(f"Plaintext: {plaintext}")
print()

print("Langkah Analisis:")
print("1. Hitung frekuensi setiap huruf dalam ciphertext")
print("2. Huruf Z muncul paling sering → kemungkinan E atau T")
print("3. Huruf J muncul sering → kemungkinan A")
print("4. Cari pola kata umum (THE, AND, OF)")
print("5. Sesuaikan mapping berdasarkan konteks")
print()