"""
This is a project which reads a text file and prits the percentage of each alphabetical char in a file
"""


file = open("sampleFile.txt", "r")
data = file.read()

alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
countlistlow = []
countlistupp = []


def countper(list, char):
    count = 0
    for fchar in data:
        if fchar == char:
            count += 1
    per = count/len(data)*100
    list.append(round(per))


for lchar in alphalist:
    countper(countlistlow, lchar)
    countper(countlistupp, lchar.upper())

for i in range(26):
    print("{0} = {1}%  and  {2} = {3}%".format(
        alphalist[i], countlistlow[i], alphalist[i].upper(), countlistupp[i]))
print("Max={0}% and  Min = {1}%".format(max(max(countlistlow), max(
    countlistupp)), min(min(countlistlow), min(countlistupp))))
