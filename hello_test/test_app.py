import unittest
from app import summation, multiply

# AAA in unit test   Arrange, Act, Assert


class CalculatorTest(unittest.TestCase):

    def setUp(self) -> None:
        print("salam setUp")
        return super().setUp()
    
    @classmethod
    def setUpClass(cls):
        print("salam class set up")

    def tearDown(self) -> None:
        print("by tear down")
        return super().tearDown()

    @classmethod
    def tearDownClass(cls) -> None:
        print("bye  class tear down")

    def test_summation(self):
        print("salam test")
        # Arrange
        a = 5
        b = 8

        # Act
        result = summation(a, b)

        # Assert
        self.assertEqual(result, 13) # assert result == 13
        
        # test float
        a = 5.8
        b = 8.3
        result = summation(a, b)
        self.assertEqual(result, 14.1)

    def test_multiply(self):
        print("salam multiply test")
        self.assertEqual(multiply(3, 6), 18)