import sys
import os


def palindrome(s):
    if s == s[::-1]:
        return s + " is a palindrome"
    return s + " is not a palindrome"

 
def solution(s):
    return palindrome(s)


if __name__ == "__main__":
 if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))
        
        print(solution(sys.argv[1]))
    