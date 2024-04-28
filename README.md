# Conway's Game of Life

## Description
Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. The game starts with a grid of cells, each cell can be either alive or dead. The cells evolve through generations according to a set of rules.

## Rules
The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.

1. **Underpopulation**: Any live cell with fewer than two live neighbours dies, as if by loneliness.
2. **Survival**: Any live cell with two or three live neighbours lives on to the next generation.
3. **Overcrowding**: Any live cell with more than three live neighbours dies, as if by overcrowding.
4. **Reproduction**: Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Installation
1. Clone or download the repository.
2. Navigate to the directory containing the files.
3. Ensure you have Python installed on your system.
4. Run the game using the following command:

```bash
python game_of_life.py
