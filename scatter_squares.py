import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]


plt.style.use('bmh')
fig,ax = plt.subplots()
ax.scatter(x_values,y_values,c=y_values, cmap=plt.cm.Blues, s=10) # o to 1 only

ax.set_title ("Plotting",fontsize = 24)
ax.set_xlabel("numbers",fontsize = 20)
ax.set_ylabel("answers",fontsize = 11)
ax.tick_params(axis = "both", which = "major", labelsize = 14)
ax.axis=([0,1100,0,110000])
#plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')