# SOAL 4: OTP Key Recovery
# Ciphertext: TLCYKUMGDF
# Plaintext: MRJOHNSONL

def otp_key_recovery(ciphertext, plaintext):
    """Menemukan kunci OTP dari plaintext dan ciphertext"""
    key = ""
    calculations = []
    
    for i in range(len(ciphertext)):
        c = ciphertext[i]
        p = plaintext[i]
        
        # Konversi ke angka
        c_num = ord(c) - ord('A')
        p_num = ord(p) - ord('A')
        
        # Hitung kunci: K = (C - P) mod 26
        k_num = (c_num - p_num + 26) % 26
        k_char = chr(k_num + ord('A'))
        
        key += k_char
        
        calculations.append({
            'index': i + 1,
            'c': c,
            'c_num': c_num,
            'p': p,
            'p_num': p_num,
            'calculation': f"({c_num} - {p_num} + 26) mod 26 = {k_num}",
            'k': k_char,
            'k_num': k_num
        })
    
    return key, calculations

def otp_encrypt(plaintext, key):
    """Enkripsi OTP untuk verifikasi"""
    ciphertext = ""
    
    for i in range(len(plaintext)):
        p_num = ord(plaintext[i]) - ord('A')
        k_num = ord(key[i]) - ord('A')
        c_num = (p_num + k_num) % 26
        ciphertext += chr(c_num + ord('A'))
    
    return ciphertext

def otp_decrypt(ciphertext, key):
    """Dekripsi OTP"""
    plaintext = ""
    
    for i in range(len(ciphertext)):
        c_num = ord(ciphertext[i]) - ord('A')
        k_num = ord(key[i]) - ord('A')
        p_num = (c_num - k_num + 26) % 26
        plaintext += chr(p_num + ord('A'))
    
    return plaintext

# Main Program
ciphertext = "TLCYKUMGDF"
plaintext = "MRJOHNSONL"

print("="*80)
print("SOAL 4: OTP KEY RECOVERY")
print("="*80)
print(f"Ciphertext (C): {ciphertext}")
print(f"Plaintext (P):  {plaintext}")
print()

# Recovery kunci
key, calcs = otp_key_recovery(ciphertext, plaintext)
print(f"Key Recovered (K): {key}")
print()

# Tabel Perhitungan
print("Tabel Perhitungan Kunci:")
print("-"*90)
print(f"{'No':<4} {'C':<3} {'C(num)':<8} {'P':<3} {'P(num)':<8} "
      f"{'Perhitungan':<30} {'K':<3}")
print("-"*90)

for calc in calcs:
    print(f"{calc['index']:<4} {calc['c']:<3} {calc['c_num']:<8} "
          f"{calc['p']:<3} {calc['p_num']:<8} {calc['calculation']:<30} "
          f"{calc['k']:<3}")

print("-"*90)
print()

# Verifikasi dengan enkripsi
print("Verifikasi:")
print("-"*40)
verified_ciphertext = otp_encrypt(plaintext, key)
print(f"Enkripsi P dengan K: {verified_ciphertext}")
print(f"Ciphertext asli:     {ciphertext}")
print(f"Match: {verified_ciphertext == ciphertext}")
print()

# Verifikasi dengan dekripsi
verified_plaintext = otp_decrypt(ciphertext, key)
print(f"Dekripsi C dengan K: {verified_plaintext}")
print(f"Plaintext asli:      {plaintext}")
print(f"Match: {verified_plaintext == plaintext}")
print()

print("Penjelasan Rumus OTP:")
print("- Enkripsi: C = (P + K) mod 26")
print("- Dekripsi: P = (C - K) mod 26")
print("- Key Recovery: K = (C - P) mod 26")
print()
print("Catatan: +26 digunakan untuk menghindari hasil negatif")
print()