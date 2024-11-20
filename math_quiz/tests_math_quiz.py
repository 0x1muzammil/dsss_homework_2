import unittest
from math_quiz import generate_random_number, calculate_square, generate_math_problem

class TestMathQuiz(unittest.TestCase):

    def test_generate_random_number(self):
        """Test if the random number is within the specified range."""
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test multiple random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"Random number {rand_num} is out of range")

    def test_calculate_square(self):
        """Test if the square of a number is calculated correctly."""
        test_cases = [
            (3, 9),
            (0, 0),
            (-4, 16),
            (5, 25)
        ]
        for num, expected in test_cases:
            result = calculate_square(num)
            self.assertEqual(result, expected, f"Square of {num} should be {expected}, got {result}")

    def test_generate_math_problem(self):
        """Test if the math problem is generated and answered correctly."""
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24),
            (9, 3, '/', '9 / 3', 3)
        ]
        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_math_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Expected problem: {expected_problem}, got: {problem}")
            self.assertEqual(answer, expected_answer, f"Expected answer: {expected_answer}, got: {answer}")

if __name__ == '__main__':
    unittest.main()
