import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
data_usage = [20, 25, 22, 30, 35, 40]

plt.plot(months, data_usage)

plt.title('Monthly Data Usage Trend')
plt.xlabel('Month')
plt.ylabel('Data Used (GB)')

plt.show()