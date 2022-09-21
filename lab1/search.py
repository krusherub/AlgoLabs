# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import sys

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue # util queue
    # Create an empty queue to store the coordinates of the matrix
    queueCoordinates = Queue()

    path = [] # a path from A to B
    visited = [] # visited coordinates

    # Initialize queue with the source cell having a distance of 0 from the source, marking it as visited.
    if(problem.isGoalState(problem.getStartState())):
        return []
    # Checking if source and destination cell have value 1

    # Add source cell and path
    queueCoordinates.push((problem.getStartState(),[]))


    while(1):
       # print(queueCoordinates.list)
        if(queueCoordinates.isEmpty()):
            return []

        # Dequeue the front cell
        curr = queueCoordinates.pop()
        # Add visited state
        visited.append(curr[0])
        # If we have reached the destination cell, return the final distance
        if(problem.isGoalState(curr[0])):
            return curr[1]
        # Enqueue passable cells
        passCells = problem.getSuccessors(curr[0]) #wave
        check = 0
        if passCells:
            for passCell in passCells:
                if passCell[0] not in visited:
                    for xy in queueCoordinates.list:
                        if passCell[0] == xy[0]:
                            check = 1
                            break
                    if check != 1:
                        path = curr[1] + [passCell[1]]
                        queueCoordinates.push((passCell[0],path))









    #problem.
    #util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    print(problem.getCostOfActions([]))
    from util import PriorityQueue
    queueCoordinates = PriorityQueue()
    # check = 0
    path = [] # path from A to B
    visited = [] # marked states

    if(problem.isGoalState(problem.getStartState())):
        return []

    firstItem = (problem.getStartState(),[])
    # print(firstItem[0])
    queueCoordinates.push(firstItem,(f(problem,firstItem,heuristic)))
    # print((f(problem,firstItem,heuristic)))
    while(1):
        # if (check == 45):
            # return curr[1]
        if(queueCoordinates.isEmpty()): # no solutions
            return []

        curr = queueCoordinates.pop()

        if curr[0] in visited:
            continue
        visited.append(curr[0])

        if(problem.isGoalState(curr[0])):
            return curr[1]
        succ = problem.getSuccessors(curr[0])

        if succ:
            for item in succ:
                if item[0] not in visited:
                    # print(check)
                    # check += 1
                    path = curr[1] + [item[1]]
                    newItem = (item[0],path)
                    queueCoordinates.push(newItem,(f(problem,newItem,heuristic)))


def greedyAstarSearch(problem: SearchProblem, heuristic=nullHeuristic):

    from util import PriorityQueue
    queueCoordinates = PriorityQueue()

    path = []  # path from A to B
    visited = []  # marked states

    if (problem.isGoalState(problem.getStartState())):
        return []

    firstItem = (problem.getStartState(), [])

    queueCoordinates.push(firstItem, (heuristic(firstItem[0],problem)))
    # print((heuristic(firstItem[0],problem)))
    # check = 0
    while (1):

       # print(check)
        # if(check == 45):
            # return curr[1]
        if (queueCoordinates.isEmpty()):  # no solutions
            return []

        curr = queueCoordinates.pop()

        if curr[0] in visited:
            continue

        visited.append(curr[0])

        if (problem.isGoalState(curr[0])):
            return curr[1]
        succ = problem.getSuccessors(curr[0])

        if succ:
            for item in succ:
                if item[0] not in visited:
                    # print(check)
                    # check += 1
                    path = curr[1] + [item[1]]
                    newItem = (item[0], path)
                    queueCoordinates.push(newItem, (heuristic(newItem[0],problem)))
                    #print((heuristic(newItem[0],problem)))





# function f = g + h
def f(problem,item,heuristic):
    return problem.getCostOfActions(item[1]) + heuristic(item[0],problem)





# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
gastar = greedyAstarSearch