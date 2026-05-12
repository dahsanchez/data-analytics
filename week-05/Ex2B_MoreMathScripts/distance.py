# findind distance between two points
import math

x1 = 3
y1 = 8
x2 = 9
y2 = 4

distance = math.sqrt(pow((x2 - x1),2) + pow((y2 -y1),2))
print(f"{round(distance,2)} is the distance between {x1},{y1} and {x2},{y2}")