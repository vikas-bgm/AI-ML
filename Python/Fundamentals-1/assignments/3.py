# In a list find the value using loops

nums = [10,1,3,17,15,27,174,201]
x = 27
index = 0

for val in nums:
    if val == x:
        print(f"Index at position - " index)
        break
    index+= 1