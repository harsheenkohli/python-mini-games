import re

first = input("Enter the first name: \n")
first = first.upper()
pattern = r"[^a-zA-Z]"
first = re.sub(pattern, "", first)
firstList = list(first)

second = input("Enter the second name :\n")
second = second.upper()
second = re.sub(pattern, "", second)
secondList = list(second)

combinedList = []

for i in range(len(firstList)):
    flag = 0
    for j in range(len(secondList)):
        if (firstList[i] == secondList[j]):
            flag = 1
            secondList[j] = "-1"
            break
    if (flag == 0):
        combinedList.append(firstList[i])

for elem in secondList:
    if (elem != "-1"):
        combinedList.append(elem)

print(combinedList)

count = len(combinedList)
flames = ["F", "L", "A", "M", "E", "S"]
flames_dict = {"F": "Friends", "L": "Lovers", "A": "Adore",
               "M": "Marriage", "E": "Enemies", "S": "Siblings"}

while len(flames) > 1:
    remove_index = (count - 1) % len(flames)
    flames.pop(remove_index)
    if (remove_index < len(flames)):
        temp = flames[:remove_index]
        flames = flames[remove_index:]
        flames += temp

print("You got :\n" + flames_dict[flames[0]] + "!")
