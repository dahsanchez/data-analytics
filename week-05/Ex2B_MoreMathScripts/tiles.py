# You are going to tile a room whose dimensions are length by width feet. There are 
# twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need? You 
# can only buy full boxes, not a partial box.
# You also want to buy at least 10% more tiles than you need in order to handle chips, 
# breakage, and mess-ups. How many total boxes will you buy?
import math

lenght = float(input('Enter lenght: '))
width = float(input('Enter width: '))
area = lenght * width
tiles = area * 1.10
boxes_of_tiles = math.ceil(tiles / 12)

print(f"A {lenght}ft by {width}ft room would need {boxes_of_tiles} of boxes of tiles")