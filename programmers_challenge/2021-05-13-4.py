#다시푸세요 runtime error

from collections import deque
def solution(values, edges, queries):
    answer = []
    mgmt = Mgmt(Node(1, values[0]))
    for edge in edges:
        target_node = mgmt.find_node(edge[0])
        target_node.children.append(Node(edge[1], values[edge[1]-1], target_node))
    
    for q in queries:
        if q[1] == -1:
            answer.append(mgmt.find_node(q[0]).sum_children())
        else:
            mgmt.find_node(q[0]).replace_value(q[1])
    return answer

class Node:
    def __init__(self, idx, value, parent=None):
        self.idx = idx
        self.value = value
        self.parent = parent
        self.children = []
    def sum_children(self):
        ret = 0
        if not self.children:
            return self.value
        for child in self.children:
            ret += child.sum_children()
        return ret + self.value
    
    def replace_value(self, value):
        print(self.idx)
        if self.idx == 1:
            self.value = value
            return
        self.value = self.parent.value
        self.parent.replace_value(value)
    
    def find_node(self, idx):
        if self.idx == idx:
            return self
        for child in self.children:
            ret = child.find_node(idx)
            if ret != None:
                return ret
class Mgmt:
    def __init__(self, node):
        self.root = node
    
    def find_node(self, idx):
        return self.root.find_node(idx)

    def print(self):
        node = self.root
        need_visit = deque([[node]])
        while need_visit:
            same_lvl = []
            level = need_visit.popleft()
            for n in level:
                print((n.idx, n.value), end='')
                same_lvl.extend(n.children)
            if same_lvl:
                need_visit.append(same_lvl)
            print()



values, edges, queries = [1,10,100,1000,10000], [[1,2],[1,3],[2,4],[2,5]], [[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[4,1000],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[2,1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1]]
sol = solution(values, edges, queries)
result = [11111,11010,100,1000,10000,11111,10011,100,10,10000,11111,11010,100,10,10000]

print(sol == result)