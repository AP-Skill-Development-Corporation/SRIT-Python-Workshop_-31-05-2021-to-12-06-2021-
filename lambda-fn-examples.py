''' lambda fun- An anonymous function means function without name
     It can take any no.of arguments at a time but contain only single expression
     used to return fun objects
     restricted to only single exp. 
syntax:lambda arg(s): exp 

rem= lambda num:num%2
print(rem(9))
num=int(input())
print("remainder is ",rem(num))

sq=lambda x:x**2
print(sq(int(input())))
product=lambda x,y:x*y
print(product(2,3)) 

quotient=lambda x,y:x/y
print(quotient(9,5)) 


def test_fun(num):
    return lambda x:x*num
res=test_fun(20)
res2=test_fun(int(input("enter first number:")))
print("result is ",res(5))
print("2nd result is ",res2(int(input("enter second number:")))) 

num_li=[8,11,23,8,4,5,10,34,3]
filtered_list = list(filter(lambda num: (num > 7), num_li))
print(filtered_list) '''

num_li=[8,11,23,8,4,5,10,34,3]
even_list=list(map(lambda num:num%2,num_li))
print(even_list)




