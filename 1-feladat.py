m = [[1, 1, 1, 2, 1], [2, 3, 2, 2, 2], [3, 3, 2, 3, 3], [4, 4, 4, 3, 4]]

resz_eredmeny = []

for p in m:
  # egy tetszőleges méretű mátrix elemeit összegzi és beleteszi a 'rész_eredmeny' mátrixba
  resz_eredmeny.append(sum(p[0:]))

# a (tetszőleges méretű) 'resz_eredmeny' mátrix elemeit osszegzi
eredmeny = sum(resz_eredmeny[0:])


print(resz_eredmeny)
print(f'Az eredmény: {eredmeny}')