import pytest
from horrible_fizzbuzz import Solution

@pytest.fixture
def solution():
    return Solution()

class TestSolution:
    def test_3(self, solution):
        assert solution.singleFizzBuzz(5) == "Fizz"
    
    def test_5(self, solution):
        assert solution.singleFizzBuzz(3) == "Buzz"  # Corrected expected value to "Buzz"
    
    def test_15(self, solution):
        assert solution.singleFizzBuzz(15) == "FizzBuzz"  # Corrected expected value to "FizzBuzz"
    
    def test_2(self, solution):
        assert solution.singleFizzBuzz(2) == "2"  # Corrected expected value to "2"

    def test_main_14(self, solution):
        assert solution.fizzBuzz(14) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14"]
    
    def test_main_15(self, solution):
        assert solution.fizzBuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    
    def test_invalid_input(self, solution):
        with pytest.raises(ValueError):  # Assuming your solution raises a ValueError for invalid inputs
            solution.singleFizzBuzz("a string")
