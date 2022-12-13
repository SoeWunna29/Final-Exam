class Fibonacci:
    def __init__(self):
        self.val = 0
        self.next_number = 1

    def nxt(self):
        ans = Fibonacci()
        ans.val = self.next_number
        ans.next_number = self.val + self.next_number
        return ans

    def __repr__(self):
        return str(self.val)


a = Fibonacci()
print(a)
print(a.nxt())
print(a.nxt().nxt())
print(a.nxt().nxt().nxt())
print(a.nxt().nxt().nxt().nxt())
print(a.nxt().nxt().nxt().nxt().nxt())
print(a.nxt().nxt().nxt().nxt().nxt().nxt())
