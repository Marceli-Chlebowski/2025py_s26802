import random

# Cel programu:
# Program generuje losową sekwencję DNA, zapisuje ją w formacie FASTA
# oraz wyświetla statystyki procentowe zawartości nukleotydów.
# wszystkie modyfikacje maja swoj oddzielny branch na github do wyboru sa:
# main
# modyfikacja1
# modyfikacja1+2
# modyfikacja1+2+3

# Pobranie danych od użytkownika
seq_length = int(input("Podaj długość sekwencji: "))
seq_id = input("Podaj ID sekwencji: ")
description = input("Podaj opis sekwencji: ")
name = input("Podaj imię: ")

# Generowanie losowej sekwencji DNA
nucleotides = ['A', 'C', 'G', 'T']
dna_seq = ''.join(random.choices(nucleotides, k=seq_length))

# Wstawienie imienia użytkownika w losowe miejsce
insert_index = random.randint(0, len(dna_seq))
final_seq = dna_seq[:insert_index] + name + dna_seq[insert_index:]

# Zapis do pliku FASTA
filename = f"{seq_id}.fasta"
with open(filename, 'w') as file:
    file.write(f">{seq_id} {description}\n")
    file.write(final_seq + "\n")

print(f"Sekwencja została zapisana do pliku {filename}")

# Statystyki (bez imienia)
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

# Wyświetlenie statystyk
print("Statystyki sekwencji:")
print(f"A: {perc_A:.1f}%")
print(f"C: {perc_C:.1f}%")
print(f"G: {perc_G:.1f}%")
print(f"T: {perc_T:.1f}%")
print(f"%CG: {cg_at_ratio:.1f}")
