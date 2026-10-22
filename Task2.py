import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
users = [1000, 1500, 1800, 2200, 2700, 3200]

plt.plot(months, users, marker='o', markerfacecolor='red', markeredgecolor='red')

plt.title('Monthly Active Users')
plt.xlabel('Months')
plt.ylabel('Active Users')

plt.show()