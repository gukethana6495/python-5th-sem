import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20, 35, 30, 45, 50]

plt.plot(months, sales)

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()