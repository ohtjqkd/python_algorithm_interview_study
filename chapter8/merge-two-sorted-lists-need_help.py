# leete no. 21

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = first(l1, l2)
        printLN(result)
        return result

def first(l1, l2):
    if l1.val < l2.val:
        head = l1
    else:
        head = l2
    while l1 and l2:
        if l1.val < l2.val:
            if not l1.next:
                l1.next = l2
                break
            else:
                while l1.next and l1.next.val < l2.val:
                    l1 = l1.next
                l1_next = l1.next
                l1.next = l2
                l1 = l1_next
        else:
            if not l2.next:
                l2.next = l1
                break
            else:   
                while l2.next and l2.next.val < l1.val:
                    l2 = l2.next
                l2_next = l2.next
                l2.next = l1
                l2 = l2_next
        # if l1 == None:
        #     l1 = l2
        # if l2 == None:
        #     l2 = l1
    # while head.next:
    #     head = head.next
    # if l1:
    #     while l1:
    #         result.append(l1.val)
    #         l1 = l1.next
    # if l2:
    #     while l2:
    #         result.append(l2.val)
    #         l2 = l2.next
    return head






def conver_to_LN(arr):
    head = ListNode(arr[0])
    node = head
    for i in range(1, len(arr)):
        node.next = ListNode(arr[i])
        node = node.next
    return head

def printLN(ln_head):
    while ln_head:
        print(ln_head.val)
        ln_head = ln_head.next
arr1, arr2 = [1,2,4], [1,3,4]

l1, l2 = conver_to_LN(arr1), conver_to_LN(arr2)

print(Solution().mergeTwoLists(l1, l2))
