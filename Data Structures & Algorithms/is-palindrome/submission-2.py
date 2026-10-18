class Solution:
    def isPalindrome(self, s: str) -> bool:

        #pre: string s 
        #post: isPalindrome returns true if Palindrome else false

        #Design idea
        #left = 0 
        #right = len(s) - 1

        # for loop
        # left == right
        # left += 1 and right -= 1 
        #Check if palindrome


        #if palindrome
        #return True 

        #else 
        # return False


        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1 

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1 
            right -= 1

        return True




        