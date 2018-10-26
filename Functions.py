def calc_circle_area(radius):
    area = 3.1415926 * float(radius) ** 2
    print('Circle area is'+ str(area))

radius = input('What is the radius of circle? ')
calc_circle_area(radius)