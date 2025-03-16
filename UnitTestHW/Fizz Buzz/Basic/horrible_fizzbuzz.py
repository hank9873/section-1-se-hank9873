def fizzBuzz(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"  # Check for divisibility by both 3 and 5 first
    if n % 3 == 0:
        return "Fizz"  # Check for divisibility by 3
    if n % 5 == 0:
        return "Buzz"  # Check for divisibility by 5
    return str(n)  # If not divisible by 3 or 5, return the number as a string
