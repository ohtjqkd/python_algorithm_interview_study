# leete no. 125

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 공백, 특수문자를 trim한 list 생성
        new_str = [c.lower() for c in s if c.isalnum()] # isalnum() if [a-zA-Z0-9] return True
        for i in range(len(new_str)//2+1):
            if new_str[i] != new_str[-(i+1)]:
                return False
        return True

## 정규표현식과 문자열 슬라이싱을 이용하면 더 빠른시간 내에 해결 가능
## python의 문자슬라이싱은 C로 빠르게 구현되어 있다!! 중요한듯
# import re
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = re.sub(r'[\W\_]', '', s.lower())
#         return s == s[::-1]
