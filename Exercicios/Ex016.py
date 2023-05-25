import numpy as np

v = np.array([[22, 12, 54, 89, 11]])
t = np.array([[3, 2, 1, 4, 1]])
w = v + t
print(w)

# v = [22, 12, 54, 89, 11]
# for c in v:
#     var = c * 5
#     print(var)

notas = np.array([[90, 85, 70, 100]])
pesos = np.array([[0.2, 0.2, 0.3, 0.3]])
media = np.inner(notas, pesos)
print(media)
