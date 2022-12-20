import matplotlib.pyplot as plt

file = open('NASA_access_log_Jul95')

ip_address = []
files = []
time = []


try:
    for line in file:
        ip_address.append(line.split(" ")[0])
        files.append(line.split(" ")[6])
        time.append(line.split(" ")[3].split(":")[0])

except:
        print("uh-oh")

from collections import Counter

a = Counter(ip_address)#.most_common(1)
# b = Counter(files).most_common(1)
# c = Counter(time).most_common(1)
print(a.keys())
print(a.values())

plt.plot(a.keys(), a.values())
plt.show()
# print(b)
# print(c)

