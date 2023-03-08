import matplotlib.pyplot as plt

class Gui:

    def __init__(self, fields, cities):
        self.fig, self.ax = plt.subplots()
        self.fig.tight_layout(pad=0)
        self.fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
        self.ax.set_xlim(0, fields)
        self.ax.set_ylim(0, fields)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.X, self.Y = [city.x for city in cities], [city.y for city in cities]
        self.line, = self.ax.plot([],[], color='#990000', zorder=1)
        self.ax.scatter(self.X,self.Y, color='#0000FF', s=50, zorder=2)
    
    def draw(self, agent):
        agent_x = [self.X[x] for x in agent.gene]
        agent_y = [self.Y[x] for x in agent.gene]
        self.line.set_data(agent_x, agent_y)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(0.1) 