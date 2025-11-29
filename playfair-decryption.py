# SOAL 2: Dekripsi Playfair Cipher
# Key: MONARCHY
# Ciphertext: GATLMZCLRQX

def create_playfair_matrix(key):
    """Membuat matriks Playfair 5x5"""
    # Hilangkan duplikat dari key
    key = key.upper().replace('J', 'I')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Tanpa J
    
    matrix_str = ""
    used = set()
    
    # Tambahkan huruf dari key
    for char in key:
        if char not in used and char.isalpha():
            matrix_str += char
            used.add(char)
    
    # Tambahkan sisa huruf
    for char in alphabet:
        if char not in used:
            matrix_str += char
    
    # Buat matriks 5x5
    matrix = []
    for i in range(5):
        matrix.append(list(matrix_str[i*5:(i+1)*5]))
    
    return matrix

def find_position(matrix, char):
    """Mencari posisi huruf dalam matriks"""
    char = char.upper().replace('J', 'I')
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None, None

def playfair_decrypt(ciphertext, key):
    """Dekripsi Playfair Cipher"""
    matrix = create_playfair_matrix(key)
    plaintext = ""
    steps = []
    
    # Proses per digram (2 huruf)
    for i in range(0, len(ciphertext), 2):
        c1 = ciphertext[i]
        c2 = ciphertext[i+1] if i+1 < len(ciphertext) else 'X'
        
        r1, col1 = find_position(matrix, c1)
        r2, col2 = find_position(matrix, c2)
        
        # Terapkan aturan Playfair (dekripsi)
        if r1 == r2:  # Baris sama
            p1 = matrix[r1][(col1 - 1) % 5]
            p2 = matrix[r2][(col2 - 1) % 5]
            rule = "Baris sama - geser kiri"
        elif col1 == col2:  # Kolom sama
            p1 = matrix[(r1 - 1) % 5][col1]
            p2 = matrix[(r2 - 1) % 5][col2]
            rule = "Kolom sama - geser atas"
        else:  # Persegi panjang
            p1 = matrix[r1][col2]
            p2 = matrix[r2][col1]
            rule = "Persegi panjang"
        
        plaintext += p1 + p2
        
        steps.append({
            'digram': c1 + c2,
            'pos1': f"({r1},{col1})",
            'pos2': f"({r2},{col2})",
            'rule': rule,
            'result': p1 + p2
        })
    
    return plaintext, matrix, steps

# Main Program
key = "MONARCHY"
ciphertext = "GATLMZCLRQX"

print("="*60)
print("SOAL 2: DEKRIPSI PLAYFAIR CIPHER")
print("="*60)
print(f"Key: {key}")
print(f"Ciphertext: {ciphertext}")
print()

# Dekripsi
plaintext, matrix, steps = playfair_decrypt(ciphertext, key)
print(f"Plaintext: {plaintext}")
print()

# Tampilkan Matriks
print("Matriks Playfair 5x5:")
print("-"*25)
for row in matrix:
    print("  ".join(row))
print("-"*25)
print()

# Tampilkan Langkah Dekripsi
print("Langkah Dekripsi:")
print("-"*70)
print(f"{'Digram':<10} {'Pos1':<10} {'Pos2':<10} {'Aturan':<25} {'Result':<10}")
print("-"*70)

for step in steps:
    print(f"{step['digram']:<10} {step['pos1']:<10} {step['pos2']:<10} "
          f"{step['rule']:<25} {step['result']:<10}")

print("-"*70)
print()