#!/usr/bin/python3
import numbers

class InvalidMatrixException(Exception):
	pass

class Matrix:
	def __init__(self, *rows):
		self.rows = rows

	def __getitem__(self, idx):
		return self.rows[idx]

	def __setitem__(self, key, item):
		item_length = len(item)
		if item_length != self.size:
			raise InvalidMatrixException(
				"You passed row with invalid length of {}, should be {}"
				.format(item_length, self.size))
		self._rows[key] = item

	def __add__(self, matrix_or_int):
		if isinstance(matrix_or_int, numbers.Integral):
			new_matrix = [matrix_or_int] * self.size**2
			return self + Matrix.construct(*new_matrix)
		if matrix_or_int.size != self.size:
			raise InvalidMatrixException("Matrixes' sizes are different!")
		
		new_matrix = []
		for i in range(self.size):
			for j in range(self.size):
				new_matrix.append(self.rows[i][j] + matrix_or_int[i][j])
		return Matrix.construct(*new_matrix)
	
	def __radd__(self, matrix):
		return self.__add__(matrix)

	def __mul__(self, matrix_or_int):
		if isinstance(matrix_or_int, numbers.Integral):
			new_matrix = Matrix.construct(*[0]*self.size**2)
			for i in range(self.size):
				for j in range(self.size):
					new_matrix[i][j] = matrix_or_int * self.rows[i][j]
			return new_matrix

		if matrix_or_int.size != self.size:
			raise InvalidMatrixException("Matrixes' sizes are different!")

		new_matrix = Matrix.construct(*[0]*self.size**2)
		for i in range(self.size):
			for j in range(self.size):
				s = 0
				for k in range(self.size):
					s += self.rows[i][k] * self.rows[k][j]
				new_matrix[i][j] = s
		return new_matrix
	
	def __rmul__(self, matrix_or_int):
		return self.__mul__(matrix_or_int)

	def __str__(self):
		return '\n'.join(
			[''.join(['{:4}'.format(item) for item in row]
			) for row in self.rows])

	def __eq__(self, matrix):
		if matrix.size != self.size:
			return False
		for i in range(self.size):
			for j in range(self.size):
				if self.rows[i][j] != matrix.rows[i][j]:
					return False
		return True

	@property
	def rows(self):
		return self._rows

	@rows.setter
	def rows(self, rows):
		self._size = len(rows)
		if self._size == 0:
			raise InvalidMatrixException("You passed 0 arguments!")
		for row in rows:
			if len(row) != self._size:
				raise InvalidMatrixException("You passed no square matrix!") 
		self._rows = [list(row) for row in rows]

	@property
	def size(self):
		return self._size

	@staticmethod
	def construct(*args):
		size_square = len(args)
		if size_square == 0:
			raise InvalidMatrixException("Cannot create Matrix of size 0.")
		
		size = int(size_square**0.5)
		if size_square**0.5 != size:
			raise InvalidMatrixException("Cannot create not square matrix.")
		return Matrix(*[args[i*size:(i+1)*size] for i in range(size)])