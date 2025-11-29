# SOAL 1: Enkripsi Vigenère Cipher
# Plaintext: SECURITYISPRIORITY
# Key: LEMON

def vigenere_encrypt(plaintext, key):
    """Enkripsi menggunakan Vigenère Cipher"""
    ciphertext = ""
    calculations = []
    
    for i in range(len(plaintext)):
        p_char = plaintext[i]
        k_char = key[i % len(key)]
        
        # Konversi ke angka (A=0, B=1, ..., Z=25)
        p_num = ord(p_char) - ord('A')
        k_num = ord(k_char) - ord('A')
        
        # Enkripsi: C = (P + K) mod 26
        c_num = (p_num + k_num) % 26
        c_char = chr(c_num + ord('A'))
        
        ciphertext += c_char
        
        # Simpan perhitungan untuk tabel
        calculations.append({
            'index': i + 1,
            'p_char': p_char,
            'p_num': p_num,
            'k_char': k_char,
            'k_num': k_num,
            'calculation': f"({p_num} + {k_num}) mod 26 = {c_num}",
            'c_char': c_char
        })
    
    return ciphertext, calculations

def vigenere_decrypt(ciphertext, key):
    """Dekripsi untuk verifikasi"""
    plaintext = ""
    
    for i in range(len(ciphertext)):
        c_num = ord(ciphertext[i]) - ord('A')
        k_num = ord(key[i % len(key)]) - ord('A')
        
        # Dekripsi: P = (C - K) mod 26
        p_num = (c_num - k_num) % 26
        plaintext += chr(p_num + ord('A'))
    
    return plaintext

# Main Program
plaintext = "SECURITYISPRIORITY"
key = "LEMON"

print("="*60)
print("SOAL 1: ENKRIPSI VIGENÈRE CIPHER")
print("="*60)
print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print()

# Enkripsi
ciphertext, calcs = vigenere_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")
print()

# Tabel Perhitungan
print("Tabel Perhitungan:")
print("-"*80)
print(f"{'No':<4} {'P':<3} {'P(num)':<7} {'K':<3} {'K(num)':<7} {'Perhitungan':<25} {'C':<3}")
print("-"*80)

for calc in calcs:
    print(f"{calc['index']:<4} {calc['p_char']:<3} {calc['p_num']:<7} "
          f"{calc['k_char']:<3} {calc['k_num']:<7} {calc['calculation']:<25} "
          f"{calc['c_char']:<3}")

print("-"*80)
print()

# Verifikasi Dekripsi
decrypted = vigenere_decrypt(ciphertext, key)
print(f"Verifikasi Dekripsi: {decrypted}")
print(f"Match dengan plaintext: {decrypted == plaintext}")
print()