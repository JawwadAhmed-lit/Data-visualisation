import matplotlib.pyplot as plt
input_numebrs = [1,2,3,4,5,6,7,8,9,10]
sqaures = [1,4,9,16,25,36,49,64,81,100]

plt.style.use('bmh')
fig ,ax =plt.subplots()
ax.plot(input_numebrs,sqaures, linewidth = 3)


#setting chart title and labels
ax.set_title ("Sqaure Numbers", fontsize = 24)
ax.set_xlabel ("Numbers From 1 to 10", fontsize = 14)
ax.set_ylabel("Squared ", fontsize = 14)


# Set size of tick labels.
ax.tick_params(axis = "both", labelsize = 14)
plt.show()