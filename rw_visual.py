import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:

    rw = RandomWalk()
    rw.fill_walk()
    plt.style.use('classic')
    fig , ax = plt.subplots()
    point_running = range(rw.num_points)

    ax.scatter(rw.x_values,rw.y_values, c = point_running, cmap=plt.cm.Blues ,
        edgecolor='none',s=15)
    plt.show()
    keep_running = input("make another walk (y)/(n)")
    if keep_running == "n":
        break