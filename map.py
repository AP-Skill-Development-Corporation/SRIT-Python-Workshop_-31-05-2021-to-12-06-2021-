def find_length(word):
    return len(word)

''' li=list(map(find_length,['hi','i am','ruthu']))
print(li) '''


li=list(map(find_length,input().split()))
print(li)
