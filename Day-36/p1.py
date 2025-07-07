# def func(count):
#     if count==0:
#         return
    
#     print(count)
#     func(count-1)

# func(5)

def fun(n):
    if n==0:
        return 
    
    fun(n-1)
    print(n)
fun(5)