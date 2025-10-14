def hello():
    print("hello!!welcome to diggibyte")
hello()

def mul(x,y):
    return x*y 
print(mul(2,5))

def hi(name="user"):
    print(f"welcome {name}")
hi()
hi("mahi")

def mat(a,b):
    return a+b,a-b
print(mat(5,6))

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
 
