class Node:
    def __init__(self, min=float('inf'), max=-float('inf')):
        self.min = min
        self.max = max

class SegTree:
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.tree = [Node() for _ in range(self.n * 4)]
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.build(data)
    
    def build(self, data):
        start = self.size
        for i in range(self.n):
            self.tree[start + i].min = self.tree[start + i].max = self.data[i]
        for i in range(start - 1, 0, -1):
            left = 2 * i
            right = 2 * i + 1
            self.tree[i].min = min(self.tree[left].min, self.tree[right].min)
            self.tree[i].max = max(self.tree[left].max, self.tree[right].max)
    
    def query(self, left, right, node=1, start=0, end=None):
        if end == None:
            end = self.size - 1
        
        if end < left or right < start:
            return float('inf'), -float('inf')

        if left <= start and end <= right:
            return self.tree[node].min, self.tree[node].max
        
        mid = (start + end) // 2
        leftMin, leftMax = self.query(left, right, node * 2, start, mid)
        rightMin, rightMax = self.query(left, right, node * 2 + 1, mid + 1, end)

        return min(leftMin, rightMin), max(leftMax, rightMax)

input = open(0).readline

n, m = map(int,input().split())
data = [int(input()) for _ in range(n)]
segTree = SegTree(data)
for _ in range(m):
    a, b = map(int,input().split())
    result = segTree.query(a - 1, b - 1)
    print(*result)