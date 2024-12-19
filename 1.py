
GC = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


class Star():
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self, m, radius, color,x,y,Vx,Vy,Fx,Fy, type):
        self.type = type
        self.m = m
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = Fx
        self.Fy = Fy

    def repr(self):
        return f'{self.type}, {self.m}, {self.x}, {self.y}, {self.Vx}, {self.Vy}, {self.Fx}, {self.Fy}, {self.R}, {self.color}, {self.image}'
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def set_Vx(self,Vx):
        self.Vx = Vx
    def set_Vy(self,Vy):
        self.Vy = Vy
    def set_Fx(self, Fx):
        self.Fx = Fx

    def set_Fy(self, Fy):
        self.Fy = Fy

    def move_space_object(self, dt):
        ax = self.Fx / self.m
        self.x = self.x + (ax * (dt) ** 2) / 2
        self.Vx = self.Vx + ax * dt
        ay = self.Fy / self.m
        self.y += self.y + (ay * (dt) ** 2) / 2
        self.Vy += self.Vy + ay * dt
        return f' {self.type} x: {self.x}, y: {self.y}'

    def calculate_force(body, space_objects: list):
        """Вычисляет силу, действующую на тело.

        Параметры:

        **body** — тело, для которого нужно вычислить дейстующую силу.

        **space_objects** — список объектов, которые воздействуют на тело.
        """
        body.Fx = body.Fy = 0
        for obj in space_objects:
            if (isinstance(obj, Star) or isinstance(obj, Planet)) and body.x != obj.x and body.y != obj.y:
                Fx = (obj.m * body.m * GC) / (obj.x - body.x) ** 2
        Fy = (obj.m * body.m * GC) / (obj.y - body.y) ** 2
        body.set_Fx(Fx)
        body.set_Fy(Fy)
        return f' {body.type} Fx: {body.Fx} Fy: {body.Fy} '


class Planet():
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    def __init__(self, m, radius, color, x, y, Vx, Vy, Fx, Fy,type):
        self.type = type
        self.m = m
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = Fx
        self.Fy = Fy
    def repr(self):
        return f'{self.type}, {self.m}, {self.x}, {self.y}, {self.Vx}, {self.Vy}, {self.Fx}, {self.Fy}, {self.R}, {self.color}, {self.image}'
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def set_Vx(self,Vx):
        self.Vx = Vx
    def set_Vy(self,Vy):
        self.Vy = Vy
    def set_Fx(self, Fx):
        self.Fx = Fx

    def set_Fy(self, Fy):
        self.Fy = Fy

    def move_space_object(self, dt):
        ax = self.Fx / self.m
        self.x = self.x + (ax * (dt) ** 2) / 2
        self.Vx = self.Vx + ax * dt
        ay = self.Fy / self.m
        self.y += self.y + (ay * (dt) ** 2) / 2
        self.Vy += self.Vy + ay * dt
        return f' {self.type} x: {self.x}, y: {self.y}'



    def calculate_force(body, space_objects: list):
        """Вычисляет силу, действующую на тело.

        Параметры:

        **body** — тело, для которого нужно вычислить дейстующую силу.

        **space_objects** — список объектов, которые воздействуют на тело.
        """
        body.Fx = body.Fy = 0
        for obj in space_objects:
            if (isinstance(obj, Star) or isinstance(obj, Planet)) and body.x != obj.x and body.y != obj.y:
                Fx = (obj.m * body.m * GC) / (obj.x - body.x) ** 2
                Fy = (obj.m * body.m * GC) / (obj.y - body.y) ** 2
                body.set_Fx(Fx)
                body.set_Fy(Fy)
        return f' {body. type} Fx: {body.Fx} Fy: {body.Fy} '



def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

def move_space_object(self, dt):
    ax = self.Fx / self.m
    self.x = self.x + (ax * (dt) ** 2) / 2
    self.Vx = self.Vx + ax * dt
    ay = self.Fy / self.m
    self.y += self.y + (ay * (dt) ** 2) / 2
    self.Vy += self.Vy + ay * dt
    return f' {self.type} x: {self.x}, y: {self.y}'


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """
    p=0
    s=0
    for body in space_objects:
        body.calculate_force(space_objects)
        if isinstance(body, Star):
            s += 1
            print(f' №{s} {body.move_space_object(dt)}')
        elif isinstance(body, Planet):
            p += 1
            print(f' №{p} {body.move_space_object(dt)}')
superstarstar = Star(1, 1, 1, 8, 9, 1, 1, 1, 1, 'superstar')
planetura_ono_rabotaet = Planet(2, 2, 1, 5, 5, 1, 4, 1, 1, 'planetacool')
planet_i_eta_toge = Planet(3, 5, 4, 8, 2, 1, 7, 3, 7, 'planeta great btitan')
space_objects = [planetura_ono_rabotaet, superstarstar, planet_i_eta_toge]
print(superstarstar.move_space_object(5))
print(planetura_ono_rabotaet.move_space_object(4))
print(planet_i_eta_toge.calculate_force(space_objects))
print()
recalculate_space_objects_positions(space_objects, 7)

if __name__ == "__main__":
    print("This module is not for direct call!")
    #запушся плиз
print('1')