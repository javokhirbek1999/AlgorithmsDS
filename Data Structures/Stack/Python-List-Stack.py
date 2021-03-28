class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):    
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values) 

    # isEmpty
    def isEmpty(self):
        return len(self.list)==0    

    # push
    def push(self,value):
        self.list.append(value)

    # pop
    def pop(self):
        if self.isEmpty():
            raise Exception('Empty Stack')
        else:
            return self.list.pop() 

    # peek
    def peek(self):
        if self.isEmpty():
            raise Exception('Empty Stack')   
        else:
            return self.list[-1]          

    # clear
    def clear(self):
        self.list=[]  
