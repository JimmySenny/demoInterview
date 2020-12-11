#!/usr/bin/env python3 


class CQueue:
    def __init__(self):
        self.stack1 = [];
        self.stack2 = [];
#    def appendTail(self,value:int)->None:
    def appendTail(self,value):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value);
        while self.stack2:
            self.stack1.append(self.stack2.pop());
        return self.stack1;            
#    deleteHead(self) -> int:
    def deleteHead(self):
        if not self.stack1:
            return -1;
        return self.stack1.pop();

def main():
    q = CQueue();
    q.appendTail(1);
    q.appendTail(2);
    print(q.stack1);
    q.appendTail(3);
    q.appendTail(4);
    print(q.stack1);
    q.deleteHead();
    print(q.stack1);
    q.appendTail(7)
    print(q.stack1);



if __name__ == '__main__':
    main()
