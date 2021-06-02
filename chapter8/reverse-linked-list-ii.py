#leete no.92

# from 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def makeSingleLinked(arr):
    head = ListNode(arr[0])
    node = head
    for i in range(1, len(arr)):
        node.next = ListNode(arr[i])
        node = node.next
    return head
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        return first(head, left, right)

def first(head, left, right):
    ret = head
    idx = 1
    origin = []
    if left == right:
        return head
    if left == 1:
        prev = None
    while idx <= right:
        if idx == left-1:
            prev = head
        if left <= idx <= right:
            origin.append(head)
        if idx == right:
            end = head.next
        head = head.next
        idx += 1
    print(origin)
    for i in range(len(origin)-1, 0, -1):
        print(origin[i].val, origin[i-1].val)
        origin[i].next = origin[i-1]
    if origin:
        if prev:
            prev.next = origin[-1]
        origin[0].next = end
    return ret

def second(head, left, right):
    idx = 1
    if left == 1:
        prev, end = None, None
        
    ret = head

    pass


arr, left, right = [1,2,3,4,5], 2, 4
arr, left, right = [3, 5], 1, 2

head = makeSingleLinked(arr)

ret = Solution().reverseBetween(head, left, right)

while ret:
    print(ret.val)
    ret = ret.next