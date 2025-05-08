import random

# Cel programu: Generowanie i analiza losowej sekwencji DNA w formacie FASTA

# MODYFIKACJA 1: Walidacja długości sekwencji
while True:
    try:
        seq_length = int(input("Podaj długość sekwencji: "))
        if seq_length <= 0:
            raise ValueError
        break
    except ValueError:
        print("Podaj poprawną dodatnią liczbę całkowitą.")

# MODYFIKACJA 2: Walidacja ID sekwencji
while True:
    seq_id = input("Podaj ID sekwencji (bez spacji): ").strip()
    if seq_id and " " not in seq_id:
        break
    print("ID nie może być puste ani zawierać spacji.")

description = input("Podaj opis sekwencji: ")
name = input("Podaj imię: ")

nucleotides = ['A', 'C', 'G', 'T']
dna_seq = ''.join(random.choices(nucleotides, k=seq_length))

insert_index = random.randint(0, len(dna_seq))
final_seq = dna_seq[:insert_index] + name + dna_seq[insert_index:]

filename = f"{seq_id}.fasta"

# MODYFIKACJA 3: Formatowanie FASTA po 60 znaków
# ORIGINAL:
# with open(filename, 'w') as file:
#     file.write(f">{seq_id} {description}\n")
#     file.write(final_seq + "\n")
# MODIFIED:
with open(filename, 'w') as file:
    file.write(f">{seq_id} {description}\n")
    for i in range(0, len(final_seq), 60):
        file.write(final_seq[i:i+60] + "\n")

print(f"Sekwencja została zapisana do pliku {filename}")

count_A = dna_seq.count('A')
count_C = dna_seq.count('C')
count_G = dna_seq.count('G')
count_T = dna_seq.count('T')
total = len(dna_seq)

perc_A = (count_A / total) * 100
perc_C = (count_C / total) * 100
perc_G = (count_G / total) * 100
perc_T = (count_T / total) * 100

cg_at_ratio = ((count_C + count_G) / (count_A + count_T)) * 100 if (count_A + count_T) != 0 else 0

print("Statystyki sekwencji:")
print(f"A: {perc_A:.1f}%")
print(f"C: {perc_C:.1f}%")
print(f"G: {perc_G:.1f}%")
print(f"T: {perc_T:.1f}%")
print(f"%CG: {cg_at_ratio:.1f}")
