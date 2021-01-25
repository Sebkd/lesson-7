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


class Matrix:
    def __init__(self, lines = []):
        self.lines = lines

    def __str__(self):
        for row in self.lines:
            print(f'{" ".join(map(str, row))}')
        return ''

    def __add__(self, other):
        try:
            if (sum([len(element) for element in self.lines]) == sum([len(elements) for elements in other.lines])):
                for line in range(len(self.lines)):
                    for index in range(len(self.lines[0])):
                        self.lines[line][index] = self.lines[line][index] + other.lines[line][index]
                return self

            else:
                raise IndexError
        except IndexError:
            print(f'Нет возможности сложить эти две матрицы')
            return self


matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_two = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
matrix_three = Matrix([[15, 25, 35], [45, 55, 65], [75, 86]])

print(f'Матрица 1: {matrix} \n')
print(f'Матрица 2: {matrix_two}\n')
print(f'Матрица 3: {matrix_three}\n')

print(f'Матрица 1 = Матрица 1 + Матрица 2 {matrix + matrix_two} \n')
print(f'Матрица 1 = Матрица 1 + Матрица 3 {matrix + matrix_three} \n')
