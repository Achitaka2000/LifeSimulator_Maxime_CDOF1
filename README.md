# Life Simulator - Maxime_CDOF1

Life Simulator is a simple implementation of Conway's Game of Life in Python console, enhanced with the pygame library for a graphical representation.

## Getting Started

### Prerequisites
To run this application, you need to have Python installed on your system. The application is compatible with Python 3.x.

### Installation
This game requires the pygame library. Install it using the following command:

```bash
pip install pygame
```

## Running the App

Launch the main.py in your preferred IDE.

```bash
python main.py
```

## Usage

Once the application starts, it will present you with a grid to place your cells. After placing the cells, start the simulation by pressing the 'Escape' key. You can pause the simulation at any time using the same key.
Game Logic

The game follows Conway's Game of Life rules, where cells evolve based on their neighbors. The pygame library provides a visual representation of the evolving cells on a grid.
Game Controls

- Escape Key: Start/Pause the simulation.
- Mouse Click: Place cells on the grid.

Feel free to experiment with different cell patterns and observe their evolution!
Code Structure

The Python script main.py uses the pygame library to create a window and visualize the Game of Life simulation. The game logic is implemented using the numpy library to handle cell states and their updates.

Enjoy simulating life and creating unique patterns in the evolving cellular automaton!
