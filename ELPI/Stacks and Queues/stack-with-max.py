from collections import namedtuple

class Stack:
    EWCM = namedtuple('EWCM', ('x', 'max'))# EWCM is element with cached max

    def __init__(self):
        self._s = []

    def empty(self):
        return len(self._s) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._s[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._s.pop().element

    def push(self, x):
        self._s.append(
            self.EWCM(x, x if self.empty() else max(x, self.max())))
        # print(self.max())

st = Stack()
st.push(5)
st.push(8)
st.push(8)
print(st.max())
