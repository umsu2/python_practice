from matplotlib import pyplot as plt
from matplotlib import animation
from monty_hall_simulation.monty_hall import MontyHallSimulator

fig = plt.figure()
ax = plt.axes(xlim=(0, 2000), ylim=(-0, 1))
line, = ax.plot([], [], lw=2)

x = []
y = []
sim = MontyHallSimulator()
result_iter = sim.run()

def init():
    line.set_data([], [])
    return line,


def animate(i):
    prob, _, games = next(result_iter)
    x.append(games)
    y.append(prob)
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=20000, interval=20, blit=True)

anim.save('monty_hall_simulation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
if __name__ == '__main__':
    plt.show()