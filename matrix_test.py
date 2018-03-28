#Shaid3r

import matrix
import unittest
from log_writer import LogWriter

class MatrixTest(unittest.TestCase):
	def setUp(self):
		self.arguments = (1,2,3,5)
		self.test_instance = Matrix(arguments)

	def test_init(self):
		assertEquals(self.test_instance.rows, self.arguments)

	def test_add(self):
		assertEquals(Matrix(2,3,4,6), Matrix(1,1,1,1))
		assertEquals(Matrix(2,3,4,6), 1)
		with self.assertRaises(InvalidMatrixException):
			self.test_instance + Matrix(1,2)

	def test_radd(self):
		assertEquals(1, self.Matrix(2,3,4,6))

	def test_eq(self):
		assertEquals(self.test_instance, Matrix(1,2,3,5))
		assertNotEquals(Matrix(2,3,4,6), self.test_instance)
