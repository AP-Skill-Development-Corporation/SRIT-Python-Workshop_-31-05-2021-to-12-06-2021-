''' filter function returns an iterator(true/false) from elements of iterable
    by default it will return false



def filter_vowels(ch):
    v=('a','e','i','o','u')
    if ch in v:
        return True
    else:
        return False

vowels=filter(filter_vowels,st)
for vowel in vowels:
    print(vowel)
# without using filter()
random_list=[1,0,False,True,9.4]
flt_list=filter(None,random_list)
for item in flt_list:
    print(item)  

li=list(map(int,input().split()))
flt_list=filter(lambda x:x%2==0,li)
for num in flt_list:
    print(num,end=" ") '''



def is_prime(n):
    count=0
    for num in range(1,n+1):
        if n%num==0:
            count+=1
    if count==2:
        return True
    else:
        return False

li=list(map(int,input().split()))
flt_list=filter(lambda num:is_prime(num),li)
for num in list(flt_list):
    print(num,end=" ")
