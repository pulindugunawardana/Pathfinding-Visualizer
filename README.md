
# Pathfinding Visualizer

> [!summary] Goal
> An application that can visualize pathfinding algorithms on graphs.

**Status:** `planning`  
**Started:**  `11/13/2026`
**Last Updated:** `11/22/2026`

## Objective

- To write a program in python which can visualize BFS and DFS on tree graphs using the python language.

## Background

- [[Breadth First Search]]
- [[Depth First Search Traversal]]

## Approach

- A tree graph is defined with nodes and edges intially.
- BFS and DFS algorithms return an array in the order the nodes each are visited.
- Two buttons are defined for the relevant algorithms and if clicked on, they will change the value that decides the current algorithm.
- Once an algorithm is chosen the nodes are highlighted in the relevant order.
- If an algorithm was already chosen the selected nodes are cleared.
- The other algorithm will start from the source node once again.


## Problems & Decisions

- To make sure the animation runs smooth the graphs are travelled beforehand and the nodes visited are returned in order.
- To increase the quality of animation once a node is reached the edges ending with its coordinates are colorized.
- To show a button has been pressed the color of the rectangle is changed and to a boolean value is used to prevent the program from running without it. 

## Results

![[Pasted image 20261122213818.png|333]]

![[Screenshot 2026-11-22 213744.png|336]]

## What I Learned

- Using pygame for visualization and user input.
- Advanced use of loops and conditional statement.

## Next Steps

- Make the edges in the graph random such that each time the graph is unique.
- Giving the user the ability to select the source node.
## Sources

- [[W3schools]]
- [[Geeks for Geeks]]
- [[Wikipedia]]


