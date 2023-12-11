# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/

def strStr(haystack: str, needle: str) -> int:
    a = len(haystack)
    b = len(needle)
    if a >= b:
        for i in range(0,a-b+1):
            if haystack[i:b+i] == needle:
                return i
            
            if i == a-b:
                return -1
    else:
        return -1
        
haystack = "sabutsad"
needle = "sad"
# haystack = "leetcode"
# needle = "leeto"

print(strStr(haystack,needle))