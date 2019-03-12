This project's implements and uses A* algorithm for pathfinding. This particular project uses a 2D grid system and Node objects to create open paths and obstacles. MazeView handles the user input and view, and Maze handles the data management. There are two implementations, a command prompt representation and Tkinter module representation.

@ Credit to Jackson Williams (jwill319)

INSTALL
- Tkinter Module (cmd: python pip tkinter)

TODO
- Add user draw functionality to create custom Maze objects
- Add custom Tkinter themes for UI

CHANGELOG
v1.0: Initial implementation of A* with command prompt visuals (found in /cmd prompt)
v1.1: Added user bounds to graph, created obstacles, and added a No Solution state
v1.2: Fixed Maze's start and end point to be variable, fixed evaluation bug that caused A* to chose wrong path
v2.0: Added MazeView GUI
v2.1: Modularized MazeView to only take an application parameter (i.e. root = Tk())
