# test.py
from Person import Person
# count  = input()
people  = []
number = input("请输入初始人数")
number = int (number)
def dispaly():
    print("各党人数:\n工党%d;"%num[0])
    print("保守党%d"%num[1])
    print("自由党%d"%num[2])
def count():
    for i in range(0, people.__len__()):
        num[people[i].get_value()]+= 1
for i in range(0,3*number):
   people.append(Person(i%3))
print(people[5].get_value())
num = [0,0,0]
count()
dispaly()
cnt =  input("请输入需要演算的代数：")
for i in range(0,len(people)):
    people[i].last(int (cnt))
count()
dispaly()
