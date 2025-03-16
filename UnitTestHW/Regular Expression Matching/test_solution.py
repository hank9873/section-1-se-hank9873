import pytest
from solution_module import Solution  # Adjust this import based on where your solution is located

# Define a fixture to set up the solution instance
@pytest.fixture
def solution():
    return Solution()

# Test cases in the format [s, p, expected_result]
testcases = [
    # s, p, expected_res
    ["", "", True],
    ["aa", "a", False],
    ["aa", "a*", True],
    ["ab", ".*", True],
    ["a", ".*.", True],
    ["aab", "c*a*b", True],
    ["aaa", "ab*a*c*a", True]
]

# Parametrize the test function with the test cases
@pytest.mark.parametrize("s, p, expected", testcases)
def test_is_match(solution, s, p, expected):
    assert solution.isMatch(s, p) == expected

# Mark a broken solution test with xfail (expected failure)
@pytest.mark.xfail
def test_broken_solution(solution):
    # Replace this with the actual assertion you expect to fail
    assert solution.isMatch("test_case", "pattern") == False
