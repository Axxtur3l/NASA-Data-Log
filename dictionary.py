from collections import Counter
import matplotlib.pyplot as plt

fruits = [
   'banana',
   'apple', 'apple',
   'orange', 'orange', 'orange',
   'cherry', 'cherry', 'cherry', 'cherry'
]

fruit_counter = Counter(fruits)

print(fruit_counter.keys())
print(fruit_counter.values())

plt.bar(fruit_counter.keys(), fruit_counter.values())

plt.show()
