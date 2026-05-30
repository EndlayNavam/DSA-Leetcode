class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        i, j = 0, n - 1

        while i < j:
            if not s[i].isalnum():
            # not in almun means anything except numbers and characters like comma, colon etc.
            #If comma or colon comes we need to ignore, so +1
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
        
        return True