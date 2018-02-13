class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def printStack(self):
        for x in range(0, len(self.items)):
            print(self.items[len(self.items)-(1+x)])
        

def main():
    s=Stack()
    
    print(s.isEmpty())
    s.push(True)
    s.push('dog')
    print(s.peek())
    s.push('8.4')
    print(s.size())
    print(s.isEmpty())
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s.pop())
    print(s.pop())
    s.push('this')
    s.push('dog')
    s.push('is')
    s.push('cute')
    s.printStack()
    
if __name__ == "__main__":
    main()
