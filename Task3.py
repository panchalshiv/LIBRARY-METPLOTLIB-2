import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

zomato = [120, 150, 180, 200, 250]
swiggy = [100, 140, 160, 210, 230]

plt.plot(months, zomato, color='red', linestyle='-', label='Zomato')

plt.plot(months, swiggy, color='orange', linestyle='--', label='Swiggy')

plt.title('Zomato vs Swiggy Orders')
plt.xlabel('Months')
plt.ylabel('Number of Orders')

plt.legend()
plt.show()