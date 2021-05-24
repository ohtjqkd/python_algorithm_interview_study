# leete no. 206

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        return first(head)
        

def first(head): # recursively
    ret = None
    if not head.next: # 마지막 노드에 다다르면 마지막 노드를 return
        return head
    next = head.next # 다음 노드가 있다면 next에 저장
    ret = first(next) # recursive and get last node
    head.next = None # 기존의 연결을 삭제
    next.next = head # 기존의 다음 노드의 next를 현재 pointer 노드로 연결
    return ret # 마지막 노드값을 return




arr = [1, 2, 3, 4, 5]

head = ListNode(arr[0])
node = head
for i in range(1, len(arr)):
    node.next = ListNode(arr[i])
    node = node.next

result = Solution().reverseList(head)
while result:
    print(result.val)
    result = result.next

