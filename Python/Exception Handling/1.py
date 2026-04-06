# Zero division error

num1 = int(input("Enter 1st number - "))
num2 = int(input("Enter 2nd number - "))

try:
    result = num1/num2
    print(resul)
except ZeroDivisionError as e:
    print(f"[Error] Division issue : {e}")
    
except NameError as e:
    print(f"[Critical] Unexpected error: {e}")


print("Rest of the code")
