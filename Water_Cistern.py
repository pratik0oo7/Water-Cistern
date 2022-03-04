import math
pi = 3.14


def distance(select, degree_distance):
    sortest_distance = 0.0

    if(select != 0 and select > 0):
        sortest_distance = (2*pi*radius)*degree_distance/360
    elif(select !=0 and select<0):
        sortest_distance = (starting_point+radius+abs(select))

    return sortest_distance


print('insert the value in order to Radius, Height, Starting point distance')
bug = list(map(int, input().split(',')))

radius = bug[0]
height = bug[1]
starting_point = bug[2]


print('insert the value in order to surfce or degree')
select_surface = list(map(int, input().split(',')))

surface = select_surface[0]
degree = select_surface[1]

sum = 0

sum = sum + distance(surface, degree)

print(round(sum, 2))
