class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s= "".join(ch for ch in s if ch.isalnum())
        s_new=s[::-1]
        if s==s_new:
            return True
        else:
            return False


        