def email_validator(n):
    if '@'in n and '.' in n:
        return True
    else:
        return False

email=input()
email=email[1:len(email)-1] 
print(email_validator(email))