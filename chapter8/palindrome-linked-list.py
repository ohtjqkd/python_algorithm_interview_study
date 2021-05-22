# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        return first(head)


def first(head): ## convert to list
    lntoli = []
    while head:
        lntoli.append(head.val)
        head = head.next
    for i in range(len(lntoli)//2):
        if lntoli[i] != lntoli[-(i+1)]:
            return False
    return True

def second(head): ## runner solution
    rev = None
    slow = fast = head
    # runner를 이용해 역순 연결 리스트를 구성
    ## fast pointer는 두 단계씩 점프, slow는 한 단계씩 점프를 하고 중간 이전 now를 역순으로 연결한다. (rev)
    while fast and fast.next: ## fast runner가 끝에 다다르면 정지
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast: ## 길이가 홀수인 경우를 처리해주기 위함
        slow = slow.next
    
    while rev and rev.val == slow.val: 
        slow, rev = slow.next, rev.next
    return not rev



array = [1,2,2,1]
head = ListNode(1)

for i in range(1, len(array)):
    head.next = ListNode(array[i])
    head = head.next

print(Solution().isPalindrome(head))