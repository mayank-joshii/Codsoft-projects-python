def calc(a, b, c):
    if c=='+':
        return print(f"The desired solution is :{a+b}")
    elif c=='-':
        return print(f"The desired solution is :{a-b}")
    elif c=='/':
        return print(f"The desired solution is :{a/b}")
    elif c=='*':
        return print(f"The desired solution is :{a*b}")
    elif c=='%':
        return print(f"The desired solution is :{a%b}")
    else:
        return print("Enter a valid operation")
    

a = int(input("Enter a number: "))
b = int(input("Enter the second number: "))
c = input("Enter the operation : ")

ans = calc(a,b,c)
print(ans)
