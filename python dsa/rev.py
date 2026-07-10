# s = "abba"
# a = ""
# for i in range(len(s)-1,-1,-1):
#     a+=s[i]
# print(a)
# if s==a:
# if s[::-1]==s:
#     print("palindrome")
# else:
#     print("not Palindrome")

#Palindrome dsa

# s="abaaba"
# n=3
# mu=n*2
# for i in range(n):
#     print(i, mu-1-i)
#     print(s[i], s[mu-i-1])

s="abccba"
n1=len(s)//2
n2=len(s)
valid = True
for i in range(n1):
    l=s[i]
    r=s[n2-1-i]
    if l!=r:
        valid=False
        break
if valid:
    print("yes")
else:
    print("No")
