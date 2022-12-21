import math

class City:

    def __init__(self, x, y, gui) -> None:
        self.x, self.y = x, y
        self.gui = gui
    
    def draw_city(self):
        self.gui.canvas.create_oval(
            self.gui.field_size * self.x,
            self.gui.field_size * self.y,
            self.gui.field_size * self.x + self.gui.field_size,
            self.gui.field_size * self.y + self.gui.field_size,
            fill = 'white'
        )
    
    @staticmethod
    def get_distance(city1, city2):
        return math.sqrt((city1.x-city2.x)**2 + (city1.y-city2.y)**2)
    
    @staticmethod
    def draw_egde(city1, city2):
        field_size = city1.gui.field_size
        city1.gui.canvas.create_line(
            city1.x * field_size + field_size/2,
            city1.y * field_size + field_size/2,
            city2.x * field_size + field_size/2,
            city2.y * field_size + field_size/2,
            fill = 'green',
            width = 1
        )