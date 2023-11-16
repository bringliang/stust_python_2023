def add0to10(num):
    if num:
        return num+add0to10(num-1)
    else:
        return 0
 
ans=add0to10(10)
print(ans)