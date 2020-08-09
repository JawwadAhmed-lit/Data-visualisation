import matplotlib.pyplot as plt 

countries = ['USA','Brazil','India','Russia','South Africa','Mexico']
Totalcases = [5150060,3013369,2156443,882347,553188,475902]


plt.style.use('bmh')
fig ,ax =plt.subplots()
ax.plot(countries,Totalcases, c=(0,0.5,0.9),linewidth = 3)

ax.set_xlabel('Countires',fontsize = 24)
ax.set_ylabel('Cases',fontsize = 19)
ax.set_title('COVID CASES',fontsize = 23)

#ax.tick_params(axis= 'both', which = 'major', labelsize= 14)
plt.show()