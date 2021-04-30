class Application():
    def sum(self,n,m):
        return n+m
    def subtract(self,n,m):
        return n-m
    def multiply(self,n,m):
        return n*m
    def divide(self,n,m):
        return n/m
    def power(self,n,m):
        p=1
        if m >=0:
            for i in range(m):
                p=p*n
        else:
            m*=-1
            for i in range(m):
                p=p/n
        return p

    def calcval(self, c, v):
        if v == '+' or v == '-':
            return 0 + c * 3
        if v == '*' or v == '/':
            return 1 + c * 3
        if v == '^':
            return 2 + c * 3

