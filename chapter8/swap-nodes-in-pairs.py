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
        prv, nxt = None, None
        while node:
            print(idx, node.val, node.next.val)
            if idx % 2 == 0:
                #홀수번째
                prv = node
                nxt = node.next
                if not node.next.next.next:
                    if not node.next.next:
                        node.next = None
                    else:
                        node.next = node.next.next
                else:
                    node.next = node.next.next.next
                node = nxt
            else:
                #짝수번째
                nxt = node.next
                node.next = prv
                node = nxt
            idx += 1
        return ret


def printLN(head):
    print(head.val)
    if head.next:
        printLN(head.next)

arr = []
arr = [1, 2, 3, 4]

head = ListNode(arr[0])
node = head
for i in range(1, len(arr)):
    node.next = ListNode(arr[i])
    node = node.next
printLN(Solution().swapPairs(head))
