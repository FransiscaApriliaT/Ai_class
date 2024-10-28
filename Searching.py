def find_indices(x, y1, y2):
    index_y1 = x.index(y1) if y1 in x else 0
    index_y2 = x.index(y2) if y2 in x else 0

    return index_y1, index_y2

x = [5, 5, 10, 3, 2, 6, 7]
y1 = 4
y2 = 2

index_y1, index_y2 = find_indices(x, y1, y2)
print(f"Indeks y1: {index_y1}, Indeks y2: {index_y2}")
