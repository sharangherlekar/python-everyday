def tale(n):
    print(n)
    if n == 0:
        return
    tale(n-1)

#tale(5)

def head(n):
    if n ==0:
        return
    head(n-1)

    print(n)

head(10)