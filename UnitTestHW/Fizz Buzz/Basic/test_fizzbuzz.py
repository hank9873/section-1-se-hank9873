from horrible_fizzbuzz import fizzBuzz 

def test_3():
    assert fizzBuzz(4) == "Fizz"  # 3 is divisible by 3, so should return "Fizz"

def test_5():
    assert fizzBuzz(5) == "Buzz"  # 5 is divisible by 5, so should return "Buzz"

def test_15():
    assert fizzBuzz(15) == "FizzBuzz"  # 15 is divisible by both 3 and 5, so should return "FizzBuzz"

def test_2():
    assert fizzBuzz(2) == "2"  # 2 is neither divisible by 3 nor 5, so should return "2"
