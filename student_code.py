from math import sqrt
from queue import PriorityQueue

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def buildPath(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    
    return path

def shortest_path(M,start,goal):
    explored = set()
    frontier = PriorityQueue()

    frontier.put(start, 0)
    
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()
        explored.add(current)

        if current == goal:
            buildPath(came_from, start, goal)
            
        for next in M.roads[current]:
            if next in explored:
                pass
            
            new_cost = cost_so_far[current] + heuristic(M.intersections[current], M.intersections[next])
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(M.intersections[goal], M.intersections[next])
                frontier.put(next, priority)
                came_from[next] = current

    return buildPath(came_from, start, goal)
