from typing import List

class Solution:
    def singleFizzBuzz(self, n: int) -> str:
        if n % 15 == 0:  # First check for divisibility by both 3 and 5 (15)
            return "FizzBuzz"
        elif n % 3 == 0:  # Check for divisibility by 3
            return "Fizz"
        elif n % 5 == 0:  # Check for divisibility by 5
            return "Buzz"
        else:
            return str(n)  # Return the number as a string if it's not divisible by 3 or 5

    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):  # Loop from 1 to n inclusive
            ans.append(self.singleFizzBuzz(i))
        return ans
