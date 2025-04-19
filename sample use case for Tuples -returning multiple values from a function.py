import math

def circle_info(radius):
    area = math.pi * radius**2
    circumference = 2*math.pi*radius
    return area, circumference

circle_data = circle_info(5)
print(f"Area : {circle_data[0]},  circumference:{circle_data[1]}")