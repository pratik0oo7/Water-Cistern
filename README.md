# Water-Cistern
A cylindrical water cistern was built in an apartment complex in Aquatown. The bottom rests on concrete and is not accessible. It has a height h and a radius r,
# Problem Description
![image](https://user-images.githubusercontent.com/65437627/156709664-2c55e198-ffe6-43ce-8f56-c8933542bdf2.png)

A cylindrical water cistern was built in an apartment complex in Aquatown. cyllender

The bottom rests on concrete and is not accessible. It has a height h and a radius r,

A mathematical bug is sitting on the cistern at point A, and has established a coordinate system to cover the entire accessible area. The bug is sitting a distance s from the top of the cistern, and the nearest point at the top is B.

For a point C on the curved surface, the nearest point D on the top is determined, and the distance CD is taken as t. The angle p (in degrees) subtended at the centre of the circle E by the arc BD is measured (in a counterclockwise manner). The coordinates of C are taken as the pair (t,p), with t being greater than 0 and less than h, and with p being between 0 and 359 (inclusive).

For a point on the top surface, F, the distance to the centre E is taken (a), and the counterclockwise angle (in degrees) between EF and EB is taken. The coordinates of the point F are then taken as (-a,q). The value of a is between 0 and r, and the value of q is between 0 and 359.

All coordinates are integers, and if the point is on the top surface of the cylinder, the first coordinate is negative, and if it is on the curved surface of the cylinder, the first coordinate is positive.

From its staring point A, the bug needs to go to its destination, which is a point (like C or F) either on the curved surface or the top surface. The coordinates of the destination are given. The bug would like to go by the shortest path to its destination.

The goal is to determine the length of the shortest path the bug can take.

# Input
The first line has three comma separated positive integers giving r (the radius), h (the height of the cylinder) and s (the distance from the top of the starting point of the bug)

The next line has two comma separated integers (d and g) giving the coordinates of the destination. If the first integer (d) is negative, it is on top surface of the cylinder, and else it is on the curved surface of the cylinder

# Output
The output is a single integer giving the shortest distance that the bug can travel. The computed distance must be rounded to the nearest integer
