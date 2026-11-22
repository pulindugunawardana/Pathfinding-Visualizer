
# Pathfinding Visualizer

> An application that can visualize pathfinding algorithms on graphs.

**Status:** `v1.0`  
**Started:**  `11/13/2026`
**Last Updated:** `11/22/2026`

## Objective

- To write a program in python which can visualize BFS and DFS on tree graphs using the python language.

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

<img width="752" height="791" alt="Screenshot 2026-11-22 213744" src="https://github.com/user-attachments/assets/298d0aee-e91b-4e67-bfb5-956342ff4b8c" />
<img width="747" height="786" alt="Screenshot 2026-11-22 213753" src="https://github.com/user-attachments/assets/9d0ce179-61ee-42cc-aa80-067e611efad0" />


## What I Learned

- Using pygame for visualization and user input.
- Advanced use of loops and conditional statement.

## Next Steps

- Make the edges in the graph random such that each time the graph is unique.
- Giving the user the ability to select the source node.


