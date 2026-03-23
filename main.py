"""
Andrew Curtis Knoll
CSCI 332 Spring 2025
Programming Assignment #9
I acknowledge that I have worked on this assignment independently, except where explicitly noted
and referenced. Any collaboration or use of external resources has been properly cited. I am
fully aware of the consequences of academic dishonesty and agree to abide by the university's
academic integrity policy. I understand the importance the consequences of plagiarism.
"""

from typing import List, Tuple

def orientation(p1:tuple[int, int],  p2: tuple[int, int], p3: tuple[int, int]):
    val = ((p2[1]-p1[1]) * (p3[0]-p2[0]) - (p2[0]-p1[0]) *(p3[1]-p2[1]))

    if val == 0:
        return 0 #Colinear
    
    if val > 0:
        return 1 #Clockwise
    
    if val < 0: 
        return 2 #Counter Clockwise

Point = Tuple[float, float]

def convex_hull_jarvis(points: List[Point]) -> List[Point]:

    n = len(points)

    if n < 3:
        return points

    left_most = min(points, key=lambda p: p[0])

    p = left_most

    
    hull = []

    while True:
        hull.append(p)
        
        
        
        if points[0] != p:
            q = points[0]
        else:
            q = points[1]

        for r in points:
            if orientation(p, q, r) == 2:
                q = r

        p = q

        if p == left_most:
            break
    
    if len(hull) == 1:
        return -1
    if len(hull) == 2:
        return -2
    return hull


if __name__ == "__main__":
    points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)] 
    hull = convex_hull_jarvis(points) 
    print("Convex Hull:", hull)


#Convex Hull: [(0, 0), (0, 3), (3, 3), (3, 0)]