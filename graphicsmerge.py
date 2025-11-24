from graphics import rectangle, circle
from graphics.graphics_3d import cuboid, sphere

l = float(input("Rectangle length: "))
w = float(input("Rectangle width: "))
print("Area:", rectangle.area(l, w))
print("Perimeter:", rectangle.perimeter(l, w))


r = float(input("Circle radius: "))
print("Area:", circle.area(r))
print("Perimeter:", circle.perimeter(r))

l = float(input("Cuboid length: "))
w = float(input("Cuboid width: "))
h = float(input("Cuboid height: "))
print("Surface Area:", cuboid.area(l, w, h))
print("Perimeter:", cuboid.perimeter(l, w, h))

r = float(input("Sphere radius: "))
print("Surface Area:", sphere.area(r))
print("Circumference:", sphere.perimeter(r))
