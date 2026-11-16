
#Given an integer x, return true if x is a palindrome, and false otherwise.

num = 1000021

class Solution:
    def isPalindrome(self, x: int) -> bool:
        print('num is: ',num)
        if x < 0:
            return False
        digits  = []

        for i in str(x):
            digits.append(int(i))

        reverse = digits[::-1]

        for i in range(len(digits)):
            print('this is i: ',i)
            print('digits[i]: ',digits[i])
            print('reverse[i]: ',reverse[i])
            if digits[i] != reverse[i]:
                print("not palindrome")
                return False
            elif i == reverse[i]:
                print('testing palindrome')
            print('succesful palidrome')
        return True



solver = Solution()
result = solver.isPalindrome(num)
#print(result)



