'''import random

list = ['a', 'b', 'c', 'd', 'e']
print("The original list is : " + str(list))
for i in range(len(list) - 1, 0, -1):
    j = random.randint(0, i + 1)


    list[i], list[j] = list[j], list[i]

print("The shuffled list is : " + str(list))

'''

