import matplotlib.pyplot as plt

x_values = [1,2,3,4,5,6,7,8,9,10]
y_values = [1,4,9,16,25,36,48,64,81,100]


plt.style.use('bmh')
fig,ax = plt.subplots()
ax.scatter(x_values,y_values, s=50)

ax.set_title ("Plotting",fontsize = 24)
ax.set_xlabel("numbers",fontsize = 20)
ax.set_ylabel("answers",fontsize = 21)
ax.tick_params(axis = "both", which = "major", labelsize = 14)

plt.show()