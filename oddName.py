"""Gurdev"""

try:
    name = input("Enter your name")
    if not name:
        raise ValueError('empty string')
except ValueError as empty:
    print(empty)

for i in range(0,len(name),2):
    print(name[i])




