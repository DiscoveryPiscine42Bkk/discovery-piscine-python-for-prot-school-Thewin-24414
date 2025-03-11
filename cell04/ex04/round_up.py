x = input("Give me a number:")
if "." in str(x):  
    y = str(x).split(".")[1]  
    m = int(y)  
else:
    m = x 

print(m)
