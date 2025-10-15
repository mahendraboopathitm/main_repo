try:
    n=int(input())
    a=10/n
    print(a)
except ZeroDivisionError:
    print("cannot divided by zero")
except ValueError:
    print("give the valid integer")    
try:
    a = int(input())
    print("Result:", 10 / a)
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("No exception occurred.")
finally:
    print("Program execution completed.")
