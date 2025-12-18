import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk.
while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10,6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=3)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    #ax.plot(0,0, c='green', edgecolors='none', s=100)
    #ax.plot(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.show()

    keep_running = input("make another walk? (y/n): ")
    if keep_running =='n':
        break
