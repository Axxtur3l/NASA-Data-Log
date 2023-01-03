file = open("NASA_access_log_Jul95")
ip_adresses = []
Files = []
Times = []
FileType = []

try:
    for line in file:
         ip_adresses.append(line.split(" ")[0])
         Files.append(line.split(" ")[6])
         Times.append(line.split(" ")[3].split(":")[0])
         FileType.append(line.split(" "))
except UnicodeDecodeError:
         print("uh-oh")



from collections import Counter
import matplotlib.pyplot as plt

c = Counter(ip_adresses)
k = Counter(Files)
# t = Counter(Times)
# f = Counter(FileType)

Logs = Counter(ip_adresses)
Filess = Counter(Files)

newDicts = dict()
for (key, value) in Filess.items():
         if value > 1000 :
                newDicts[key] = value

newDict = dict()
for (key, value) in Logs.items():
        if value > 350 :
                newDict[key] = value


print(newDict)
print(newDicts)

print(Logs.keys)
print(Logs.values)

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.bar(newDict.keys(), newDict.values(), color = "red", ) 
plt.xticks(rotation=30, ha='right')
plt.title("Ip Adresses", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font1)
plt.ylabel("Number of Ip Adresses", fontdict = font2)

plt.show()

plt.bar(newDicts.keys(), newDicts.values(), color = "red") 
plt.xticks(rotation=50, ha='right')
plt.show()


# print(c)
# print(k)
# print(t)
# print(f)
#
