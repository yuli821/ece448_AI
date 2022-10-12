# search.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Jongdeog Lee (jlee700@illinois.edu) on 09/12/2018

"""
This file contains search functions.
"""
# Search should return the path and the number of states explored.
# The path should be a list of tuples in the form (alpha, beta, gamma) that correspond
# to the positions of the path taken by your search algorithm.
# Number of states explored should be a number.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (bfs,astar)
# You may need to slight change your previous search functions in MP1 since this is 3-d maze

from collections import deque
import heapq
from state import MazeState


# Search should return the path and the number of states explored.
# The path should be a list of MazeState objects that correspond
# to the positions of the path taken by your search algorithm.
# Number of states explored should be a number.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (astar)
# You may need to slight change your previous search functions in MP2 since this is 3-d maze
def search(maze, searchMethod):
    return {
        "astar": astar,
    }.get(searchMethod, [])(maze)

def astar(maze, ispart1=False):
    """
    This function returns an optimal path in a list, which contains the start and objective.

    @param maze: Maze instance from maze.py
    @param ispart1:pass this variable when you use functions such as getNeighbors and isObjective. DO NOT MODIFY THIS
    @return: a path in the form of a list of MazeState objects. If there is no path, return None.
    """
    # Your code here
    path = []
    starting_state = maze.getStart()
    visited_states = {starting_state: (None, 0)}
    frontier = []
    heapq.heappush(frontier, starting_state)
    while(frontier):
        state_curr = heapq.heappop(frontier)
        if(maze.isObjective(state_curr.state[0], state_curr.state[1], state_curr.state[2], ispart1)):
            path = backtrack(visited_states,state_curr)
            return path
        neibor_pos = maze.get_neighbors(state_curr.state[0], state_curr.state[1], state_curr.state[2], ispart1)
        neibor = []
        for i in neibor_pos:
            neibor.append(MazeState(i, maze.getObjectives(),1 + state_curr.dist_from_start, state_curr.mst_cache, state_curr.use_heuristic))
        for s in neibor:
            if s not in visited_states:
                heapq.heappush(frontier,s)
                visited_states[s] = (state_curr, s.dist_from_start)
            else:
                if s.dist_from_start < visited_states[s][1]:
                    visited_states[s] = (state_curr, s.dist_from_start)
                    heapq.heappush(frontier, s)
    return None

# This is the same as backtrack from MP2
def backtrack(visited_states, current_state):
    path = []
    state = current_state
    while(visited_states[state][1] != 0):
        path.insert(0,state)
        state = visited_states[state][0]
    path.insert(0,state)
    return path
        