class Stack:
    def __init__(self, start=[]):
        self.stack = []
        for each in start:
            self.push(each)

    def isEmpty(self):
        return not self.stack

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if not self.stack:
            print("警告：栈为空")
        else:
            return self.stack.pop()

    def top(self):
        if not self.stack:
            print("警告：栈为空")
        else:
            print(self.stack[0])
            return self.stack[0]

    def bottom(self):
        if not self.stack:
            print("警告：栈为空")
        else:
            print(self.stack[-1])
            return self.stack[-1]

print("修改")
start2 = [-1, 0, 1]
stack2 = Stack(start)
stack2.push(2)
stack2.bottom()
stack2.top()
stack2.pop()
print(stack2.isEmpty())
start = [-1, 0, 1]
stack1 = Stack(start)
stack1.push(2)
stack1.bottom()
stack1.top()
stack1.pop()
print(stack1.isEmpty())
