import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:

    rw = RandomWalk(5000) # better to keep at this rate!
    rw.fill_walk()
    plt.style.use('classic')
    fig , ax = plt.subplots(figsize=(12,9))
    point_running = range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values, c = point_running, cmap=plt.cm.Blues ,
        edgecolors='none',s=10)
    #ax.plot(rw.x_values,rw.y_values,c= 'green' , linewidth = 3)
    ax.scatter(0, 0, c = 'green', edgecolors='none' , s =100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1], c= 'red' , edgecolors='none', s = 100)
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("make another walk (y)/(n)")
    if keep_running == "n":
        break