# task1
'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
 (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
 складываем с первым элементом первой строки второй матрицы и т.д.
'''
from itertools import cycle

class Matrix:
    def __init__(self, lines = []):
        self.lines = lines

    def __str__(self):
        for row in self.lines:
            print(f'{" ".join(map(str, row))}')
        return ''

    def __add__(self, other):
        if ((len(self.lines) == len(other.lines)) and (len(self.lines[0]) == len(other.lines[0]))):
            try:
                for line in range (len (self.lines)):
                    for index in range (len (self.lines[0])):
                        self.lines[line][index] = self.lines[line][index] + other.lines[line][index]
                return self
            except IndexError:
                print (f'Нет возможности сложить эти две матрицы')
                return 0





matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80]])
matrix_3 = Matrix()

print(f'Матрица 1: {matrix} \n')
print(f'Матрица 2: {matrix2}\n')

matrix_3 = matrix + matrix2
print(f'Матрица 3: {matrix_3} \n')
print(f'Матрица 1: {matrix} \n')