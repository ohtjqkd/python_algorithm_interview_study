# leete no. 328

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        return first(head)

def first(head):
    ret = head
    if not head or not head.next:
        return ret
    odd_first, odd_tail = head, head
    even_first, even_tail = head.next, head.next
    while odd_tail and odd_tail.next and odd_tail.next.next:
        
        odd_tail.next, even_tail.next = odd_tail.next.next if odd_tail.next else None, even_tail.next.next if even_tail.next else None
        odd_tail, even_tail = odd_tail.next, even_tail.next

    odd_tail.next = even_first
    return ret

def convert_to_LN(arr):
    head = ListNode(arr[0])
    node = head
    for i in range(1, len(arr)):
        node.next = ListNode(arr[i])
        node = node.next
    return head

arr = [2, 1, 3, 5, 6, 4, 7, 8]
head = convert_to_LN(arr)

ret = Solution().oddEvenList(head)
while ret:
    print(ret.val)
    ret = ret.next