class Component(object):
    def __init__(self, value, unit):
        # Must be a real number
        self.value = value
        # Must be one of ['i', 'j', 'k']
        self.unit = unit
    
    def __add__(self, other):
        if self.unit == other.unit:
            return Component(self.value + other.value, self.unit)
    
    def __str__(self):
        return '{value}{unit}'.format(value=str(self.value), unit=(self.unit))

class Vector(object):
    def __init__(self, components):
        if len(components) == 3:
            self.i, self.j, self.k = components
        else:
            self.i, self.j = components
            self.k = Component(0, 'k')
    
    def __add__(self, other):
        new_i = self.i + other.i
        new_j = self.j + other.j
        new_k = self.k + other.k
        return Vector([new_i, new_j, new_k])
    
    def __str__(self):
        components = ', '.join([str(self.i), str(self.j), str(self.k)])
        return '<{}>'.format(components)


def create_components(integers):
    if len(integers) == 2:
        integers.append(0)
    components = []
    units = ['i', 'j', 'k']
    for i in range(len(integers)):
        value = integers[i]
        unit = units[i]
        components.append(Component(value, unit))
    return components


if __name__ == '__main__':
    a = create_components([3, -4, 2])
    b = create_components([2, 6, -3])
    va = Vector(a)
    vb = Vector(b)
    print(va)
    print(vb)
    print(va + vb)