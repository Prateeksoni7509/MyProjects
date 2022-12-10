#Multiplication Table Application
class table:
    def __init__(self,num):
        self.num=num
    def printTable(self):
        for i in range(10):
            print(self.num,' x ',i+1,' = ',self.num*(i+1))
print('This is a multiplication table application.')
n=int(input('Enter the number : '))
for x in range(1,n+1):
    a=table(x)
    print('------------------')
    print('Table of',x,': ')
    a.printTable()
