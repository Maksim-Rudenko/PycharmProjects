import platform
#import


double = lambda x: x * 2
#map(double, [1, 2, 3])
print(double(4))
avg = lambda * args: sum(args) / float(len(args))
print(avg(1, 2, 3))

users = [{'name': 'ivan', 'age': 29},
         {'name': 'juan', 'age': 31}]
aa = [user['name'] for user in users if user['age'] > 30]
print(aa)

x = 1
x += 1.5
print(int(x))

for x in [234, 223, 4353, 222]:
    print('{0:.^20.2f}'.format(x))

value = []
print(value is None)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Joan", 34)
print(p1.age)

hf = platform.system()
print(hf)

name = input('name: ')
print(name)