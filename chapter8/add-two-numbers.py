# leete no. 2

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return first(l1, l2)

def first(l1, l2):
    ret = None
    up = 0
    l1_tail = l1
    l2_tail = l2
    same_len = False
    while l1_tail and l2_tail:
        pls = l1_tail.val + l2_tail.val + up
        l1_tail.val, l2_tail.val = pls % 10, pls % 10
        up = pls // 10
        if not l1_tail.next and not l2_tail.next:
            same_len = True
            break
        l1_tail, l2_tail = l1_tail.next, l2_tail.next
    if same_len:
        if up != 0:
            l1_tail.next = ListNode(up)
        return l1
    else:
        if l1_tail:
            li = l1_tail
            ret = l1
        elif l2_tail:
            li = l2_tail
            ret = l2
        while li:
            pls = li.val + up
            li.val = pls % 10
            up = pls // 10
            if not li.next:
                break
            li = li.next
        if up != 0:
            li.next = ListNode(up)
    return ret

def second(l1, l2):
    l1_len, l2_len = get_length(l1), get_length(l2)
    if l1_len < l2_len:
        l1, l2 = l2, l1
    l1_tail, l2_tail, up = l1, l2, 0
    while l1_tail:
        if l2_tail:
            up, m = divmod(l1_tail.value+l2_tail.value+up, 10)
        else:
            up, m = divmod(l1_tail.value+up, 10)
        l1_tail.value = m
        if not l1_tail.next:
            if up != 0:
                l1_tail.next = ListNode(up)
            break
        if l2_tail:
            l1_tail, l2_tail = l1_tail.next, l2_tail.next
        else:
            l1_tail = l1_tail.next
    return l1
            
    

def get_length(ln):
    ret = 0
    while ln:
        ret += 1
        ln = ln.next
    return ret

arr1 = [9,9,9,9,9,9,9]
arr2 = [9,9,9,9]

arr1 = [2,4,9]
arr2 = [5,6,4,9]

print(arr1, arr2)
l1 = ListNode(arr1[0])
node = l1
for i in range(1, len(arr1)):
    node.next = ListNode(arr1[i])
    node = node.next
l2 = ListNode(arr2[0])
node = l2
for i in range(1, len(arr2)):
    node.next = ListNode(arr2[i])
    node = node.next

ret = Solution().addTwoNumbers(l1, l2)

while ret:
    print(ret.val)
    ret = ret.next