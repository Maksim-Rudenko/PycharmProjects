num1 = str(input())
num2 = str(input())
num1 = list(num1)
num2 = list(num2)
num3 = []
if len(num1) < len(num2):
    x = len(num1)
else:
    x = len(num2)

for i in range(- 1, -x - 1, -1):
    if int(num1[i]) + int(num2[i]) >= 10 and i != -x:
        num3.insert(0, int(num1[i]) + int(num2[i]) - 10)
        num1[i - 1] = str(int(num1[i - 1]) + 1)

    else:
        num3.insert(0, int(num1[i]) + int(num2[i]))
print(num3)
result = ''
for i in num3:
   result += str(i)
print(result)
print(num1)

'''if int(num1[i]) + int(num2[i]) >= 10 and i != 0:
    num3.insert(0, int(num1[i]) + int(num2[i]) - 10)
    num1[i - 1] = str(int(num1[i - 1]) + 1)
else:
    num3.insert(0, int(num1[i]) + int(num2[i]))'''