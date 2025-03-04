sets = {
    'A': {'a', 'b', 'c', 'd', 'f', 'g'},
    'B': {'b', 'c', 'h', 'l', 'm', 'o'},
    'C': {'h', 'i', 'j', 'k', 'c', 'd', 'f'}
}

print("")
print("=" * 58)
print("|            ~ VENN DIAGRAM SET OPERATIONS ~             |")
print("|                 By Pauline Erika Mapoy                 |")
print("=" * 58)

A_union_B = sets['A'] | sets['B']
print("\n[a] Elements in A and B (A ∪ B):", len(A_union_B))

B_only = sets['B'] - (sets['A'] | sets['C'])
print("[b] Elements in B that are not in A and C (B - (A ∪ C)):", len(B_only))

print("")
print("=" * 58)
print("|             CATEGORIZED SET RELATIONSHIPS              |")
print("=" * 58)
print("|                                                        |")

results = {
    '                i   ': sorted((sets['C'] - (sets['A'] | sets['B'])) | ((sets['C'] & sets['B']) - sets['A'])),
    '                ii  ': sorted(sets['C'] & sets['A']),
    '                iii ': sorted((sets['A'] & sets['B']) | (sets['B'] & sets['C'])),
    '                iv  ': sorted((sets['A'] & sets['C']) - sets['B']),
    '                v   ': sorted(sets['A'] & sets['B'] & sets['C']),
    '                vi  ': sorted(sets['B'] - (sets['A'] | sets['C']))
}

for key, value in results.items():
    print(f"{key}: {value}") 
print("|                                                        |")
print("=" * 58)
print("\n")