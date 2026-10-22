import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
steps = [4000, 5500, 6000, 4500, 7000, 8000, 6500]

plt.plot(days, steps, color='green', linewidth=2)

plt.title('Daily Steps Walked')
plt.xlabel('Days')
plt.ylabel('Steps')

plt.show()