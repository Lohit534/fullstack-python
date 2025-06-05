try:
    a=int(input())
    b=int(input())
    res=a/b
    print(f"result is:{res}")
except Exception as e:
    print(f"eroor is:{e}")
else:
    print("try block executed.")
finally:
    print("Done")

