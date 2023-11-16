def calc(a,b):
    def add(a,b):
        return a+b
   
    sum=add(a,b)
    return sum+5
 
ans=calc(5,10)
print(ans)