# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ret, node = head, head
        if head == None:
            return head
        idx = 0
        prv = None
        #value를 바꿔주자
        while node:
            if idx % 2 == 0:
                prv = node
            else:
                node.val, prv.val = prv.val, node.val
            node = node.next
            idx += 1
        return ret


def printLN(head):
    print(head.val)
    if head.next:
        printLN(head.next)

arr = []
arr = [1, 2, 3, 4, 5, 6]

head = ListNode(arr[0])
node = head
for i in range(1, len(arr)):
    node.next = ListNode(arr[i])
    node = node.next
printLN(Solution().swapPairs(head))
