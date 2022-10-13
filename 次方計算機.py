import math
num = input("底數:")
n = input("次方:")
if int(n) >= 4000:
    print("次方數應小於4000")
else:
    print (num,"的", n, "次方為:", int(num) ** int(n))
