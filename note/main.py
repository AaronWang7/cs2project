import matplotlib.pyplot as plt
import numpy as np
som = 10
user = 1
usero = 2
fig, ax = plt.subplots()

# Example data
stats = ('attack', 'defense', 'speed')

y_pos = np.arange(len(stats))

ax.barh(0, xerr=0, align='center',height=1,width=10)
ax.barh(1, user, xerr=0, align='center')
ax.barh(2, 10, xerr=0, align='center')
ax.set_yticks(y_pos, labels=stats)
ax.invert_yaxis()  
ax.set_title("Player stats")
plt.show()