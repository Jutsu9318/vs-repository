class vector():
    def __init__(self, x = None, y = None, z = None):
        #x,y,z = map(int, input().split(','))
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2)**(1/2)
    def __add__(self, other):
        if isinstance(other, vector):
            return(vector(self.x + other.x, self.y + other.y, self.z + other.z))
        elif isinstance((other, int)) or isinstance(other, float):
            return (vector(self.x + other, self.y + other, self.z + other))

    def __sub__(self, other):
        if isinstance(other, vector):
            return(vector(self.x - other.x, self.y - other.z, self.z - other.z))
        elif isinstance((other, int)) or isinstance(other, float):
            return (vector(self.x - other, self.y - other, self.z - other))
    def __mul__(self, other):
        if isinstance(other, vector):
            return self.x * other.x + self.y * other.z + self.z * other.z
    def __mul_number__(self, a):
        return (vector(self.x * a, self.y * a, self.z * 1))
    def __str__(self):
        return f'{self.x} {self.y} {self.z}'
v1 = vector(1,1,3)
v2 = vector(1,2,3)
print(str(v1.__add__(v2)))
print(1)
#111