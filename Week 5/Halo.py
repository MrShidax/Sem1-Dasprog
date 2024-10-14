import random
X1,Y1 = map(int,input("Baris dan Kolom Matriks 1 : ").split())
X2,Y2 = map(int,input("Baris dan Kolom Matriks 2 : ").split())
matrix1 = []
matrix2 = []
matrix1 = [[random.randint(0,10) for _ in range(X1)] for _ in range(Y1)]
matrix2 = [[random.randint(0,10) for _ in range(X2)] for _ in range(Y2)]

result = [[0 for _ in range(Y2)] for _ in range(X1)]

for i in range(X1):
        for j in range(Y2):
            for k in range(Y2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

print(matrix1)
print(matrix2)
print(result)