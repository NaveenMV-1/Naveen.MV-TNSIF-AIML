import matplotlib.pylab as plt

month = ["January", "February", "March", "April", "May", "June"]
sales = [25000, 32000, 28000, 40000, 45000, 38000]

plt.plot(month,sales,marker="o",label = "monthly sales")

plt.title("Monthly sales")
plt.xlabel("Months")
plt.ylabel("sales ($)")
plt.legend()
plt.show()

plt.bar(month,sales,label="monthly sales")

plt.title("Monthly sales")
plt.xlabel("Months")
plt.ylabel("sales ($)")
plt.legend()
plt.show()