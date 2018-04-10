#Shaid3r

from matrix import Matrix
from matrix import InvalidMatrixException
import unittest

class MatrixTest(unittest.TestCase):
	def setUp(self):
		self.arguments = [[1,2],[3,5]]
		self.tested_matrix = Matrix(*self.arguments)

	def test_create_valid(self):
		self.assertEqual(self.tested_matrix.rows, self.arguments)

	def test_create_invalid(self):
		with self.assertRaises(InvalidMatrixException):
			Matrix([2,3])

	def test_construct_valid(self):
		self.assertEqual(Matrix.construct(1,2,3,5), self.tested_matrix)

	def test_construct_invalid(self):
		with self.assertRaises(InvalidMatrixException):
			Matrix([2,3])

	def test_eq(self):
		self.assertTrue(self.tested_matrix == Matrix([1,2],[3,5]))
		self.assertFalse(Matrix([2,3],[4,6]) == self.tested_matrix)

	def test_getitem(self):
		self.assertEqual(1, self.tested_matrix[0][0])

	def test_setitem(self):
		value = 5
		self.tested_matrix[0][0] = value
		self.assertEqual(value, self.tested_matrix[0][0])

	def test_str(self):
		printed_text = "   1   2\n   3   5"
		self.assertEqual(str(self.tested_matrix), printed_text)

	def test_add_valid_matrix(self):
		value = 2
		valid_result = Matrix(*[[element+value for element in row] for row in self.tested_matrix.rows])
		matrix_to_add = Matrix(*[[value for element in row] for row in self.tested_matrix.rows])
		self.assertEqual(valid_result, self.tested_matrix + matrix_to_add)

	def test_radd_valid_matrix(self):
		value = 2
		valid_result = Matrix(*[[element+value for element in row] for row in self.tested_matrix.rows])
		matrix_to_add = Matrix(*[[value for element in row] for row in self.tested_matrix.rows])
		self.assertEqual(valid_result, matrix_to_add + self.tested_matrix)

	def test_add_integer(self):
		integer = 1
		valid_result = Matrix(*[[element+integer for element in row] for row in self.tested_matrix.rows])
		self.assertEqual(valid_result, self.tested_matrix + integer)

	def test_radd_integer(self):
		value = 1
		valid_result = Matrix(*[[element+value for element in row] for row in self.tested_matrix.rows])
		self.assertEqual(valid_result, value + self.tested_matrix)

	def test_add_invalid_matrix(self):
		invalid_matrix = Matrix([2])
		with self.assertRaises(InvalidMatrixException):
			self.tested_matrix + invalid_matrix

	def test_radd_invalid_matrix(self):
		invalid_matrix = Matrix([2])
		with self.assertRaises(InvalidMatrixException):
			invalid_matrix + self.tested_matrix

	# Causing error, in __mul__ function there is a small mistake
	# Is: self.rows[i][k] * self.rows[k][j]
	# Should be: self[i][k] * matrix_or_int[k][j]
	def test_mul_valid_matrix(self):
		zero_matrix = Matrix(*[[0 for element in row] for row in self.tested_matrix.rows])
		self.assertEqual(self.tested_matrix*zero_matrix, zero_matrix)

	def test_rmul_valid_matrix(self):
		zero_matrix = Matrix(*[[0 for element in row] for row in self.tested_matrix.rows])
		self.assertEqual(zero_matrix, zero_matrix*self.tested_matrix)

	def test_mul_invalid_matrix(self):
		zero_matrix = Matrix([0])
		with self.assertRaises(InvalidMatrixException):
			self.assertEqual(self.tested_matrix*zero_matrix, zero_matrix)

	def test_rmul_invalid_matrix(self):
		zero_matrix = Matrix([0])
		with self.assertRaises(InvalidMatrixException):
			self.assertEqual(zero_matrix*self.tested_matrix, zero_matrix)

	def test_mul_integer(self):
		zero_matrix = Matrix(*[[0 for element in row] for row in self.tested_matrix.rows])
		self.assertEqual(zero_matrix, self.tested_matrix*0)

	def test_rmul_integer(self):
		zero_matrix = Matrix(*[[0 for element in row] for row in self.tested_matrix.rows])
		self.assertEqual(zero_matrix, 0*self.tested_matrix)

if __name__ == '__main__':
	unittest.main()
