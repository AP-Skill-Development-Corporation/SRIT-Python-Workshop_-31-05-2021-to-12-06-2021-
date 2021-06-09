def even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"


def leapyears(l,u):
    for year in range(l,u+1):
        if year%400==0 or (year%4==0 and year%100!=0):
            print(year,end=" ")
            
            
#l=[12,12,13,14,14,15]--->[12,13,14,15]            
def duplicates(l):
    li=[] #12,13,14,15
    for i in l:#12,12,13,14,14,15
        if i not in li:
            li.append(i)
    print(li)