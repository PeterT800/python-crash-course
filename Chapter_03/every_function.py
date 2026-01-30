things = ['mountains', 'rivers', 'countries', 'cities', 'languages']
print("Original:", things)
print("Length:", len(things))

things.append('foods')
print("\nAfter append:", things)

things.insert(1, 'oceans')
print("\nAfter insert:", things)

print("\nSorted (copy):", sorted(things))
print("Still original:", things)

things.sort()
print("\nAfter sort (in place):", things)

things.sort(reverse=True)
print("\nAfter sort reverse (in place):", things)

things.reverse()
print("\nAfter reverse (in place):", things)

removed_item = things.pop()
print("\nPopped item:", removed_item)
print("After pop:", things)

things.remove('oceans')
print("\nAfter remove('oceans'):", things)
