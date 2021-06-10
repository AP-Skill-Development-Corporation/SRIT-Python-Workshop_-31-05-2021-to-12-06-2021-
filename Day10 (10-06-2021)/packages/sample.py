class cal:
    def add(n1,n2):
        return n1+n2
    def sub(n1,n2):
        return n1-n2
    def mul(n1,n2):
        return n1*n2
    def div(n1,n2):
        return n1/n2
    def mod(n1,n2):
        return n1%n2
    
class Math:
    def __init__(abc,v1,v2):
        abc.v1=v1
        abc.v2=v2
    def show(abc):
        print(abc.v1)
        print(abc.v2)
    def add(abc,v3):
        print(abc.v1+abc.v2+v3)
