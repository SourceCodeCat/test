import unittest
from multiples import *


class TestMultiples(unittest.TestCase):


	def test_customrange_modifyMultiples(self):
		#this method tests if the modifyMultiples method returns a list of numbers in
		#the range  of 1-100 inclusive where the numbers multiple of 3 = Linio, multiples
		#of 5= IT or if number is multiple of 3 adn 5 = Linianos

		#REFERENCE holds the list with the correct values
		REFERENCE = ['Linianos','Linio', 'IT']
		CUSTOM_RANGE = [15,21,20]
		results = modifyMultiples(CUSTOM_RANGE)
		self.assertEqual(results == REFERENCE, True, "modifyMultiples with CUMSTOM_RANGE produced different values  with respect to REFERENCE")

	def test_challenge_modifyMultiples(self):
		#this method tests if the modifyMultiples method returns a list of numbers in
		#the range  of 1-100 inclusive where the numbers multiple of 3 = Linio, multiples
		#of 5= IT or if number is multiple of 3 adn 5 = Linianos

		#REFERENCE holds the list with the correct values
		REFERENCE = [1, 2, 'Linio', 4, 'IT', 'Linio', 7, 8, 'Linio', 'IT', 11, 'Linio', 13, 14, 'Linianos', 16, 17, 'Linio', 19, 'IT', 'Linio', 22, 23, 'Linio', 'IT', 26, 'Linio', 28, 29, 'Linianos', 31, 32, 'Linio', 34, 'IT', 'Linio', 37, 38, 'Linio', 'IT', 41, 'Linio', 43, 44, 'Linianos', 46, 47, 'Linio', 49, 'IT', 'Linio', 52, 53, 'Linio', 'IT', 56, 'Linio', 58, 59, 'Linianos', 61, 62, 'Linio', 64, 'IT', 'Linio', 67, 68, 'Linio', 'IT', 71, 'Linio', 73, 74, 'Linianos', 76, 77, 'Linio', 79, 'IT', 'Linio', 82, 83, 'Linio', 'IT', 86, 'Linio', 88, 89, 'Linianos', 91, 92, 'Linio', 94, 'IT', 'Linio', 97, 98, 'Linio', 'IT']
		results = modifyMultiples()
		self.assertEqual(results == REFERENCE, True, "modifyMultiples produced different values  with respect to REFERENCE")

	def test_calc_key_component(self):
		#this method tests if calc_key_component returns the correct values if we pass
		# numbers that are not multiple of 3,5 or both
		results = []
		NONE_MULTIPLES_OF_3_5_OR_BOTH = [1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19, 22, 23, 26, 28, 29, 31, 32, 34, 37, 38, 41, 43, 44, 46, 47, 49, 52, 53, 56, 58, 59, 61, 62, 64, 67, 68, 71, 73, 74, 76, 77, 79, 82, 83, 86, 88, 89, 91, 92, 94, 97, 98] 
		REFERENCE = [(3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0), (3.0, 5.0)]
		for i in NONE_MULTIPLES_OF_3_5_OR_BOTH:
			results.append((calc_key_component((3,i%3)),calc_key_component((5,i%5))))
		self.assertEqual(results == REFERENCE, True, "calc_key_component produced different values  with respect to REFERENCE")


if __name__ == '__main__':
	unittest.main()


	