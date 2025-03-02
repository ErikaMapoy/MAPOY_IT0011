sets = {
    'A': {'a', 'b', 'c', 'd', 'f', 'g'},
    'B': {'b', 'c', 'h', 'l', 'm', 'o'},
    'C': {'c', 'h', 'i', 'j', 'k'}
}

print("")
print("=" * 58)
print("|            ~ VENN DIAGRAM SET OPERATIONS ~             |")
print("|                    By Pauline Mapoy                    |")
print("=" * 58)

A_union_B = sets['A'] | sets['B']
print("\n[a] Elements in A and B (A ∪ B):", len(A_union_B))

B_only = sets['B'] - (sets['A'] | sets['C'])
print("[b] Elements in B that are not in A and C (B - (A ∪ C)):", len(B_only))

print("")
print("-" * 58)
print("|             SHOWING SPECIFIC SET OPERATIONS            |")

results = {
    '[c] i': (sets['C'] - sets['A'] - sets['B']),  
    '[c] ii': (sets['A'] & sets['B'] & sets['C']),  
    '[c] iii': (sets['B'] & sets['C']), 
    '[c] iv': (sets['A'] & sets['B']), 
    '[c] v': (sets['A'] & sets['B'] & sets['C']), 
    '[c] vi': (sets['B'] - (sets['A'] | sets['C']))  
}

context = {
    '[c] i': "Elements that belong only to C (C - A - B)",
    '[c] ii': "Elements common to all three sets (A ∩ B ∩ C)",
    '[c] iii': "Elements that belong to both B and C (B ∩ C)",
    '[c] iv': "Elements that belong to both A and B (A ∩ B)",
    '[c] v': "Elements common to A, B, and C (A ∩ B ∩ C)",
    '[c] vi': "Elements that belong only to B (B - (A ∪ C))"
}

for key, value in results.items():
    print("=" * 58)
    print(f"{key}: {value}")
    print(f"    • {context[key]}")
print("=" * 58)
print("")