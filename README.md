# Classic Snake Game in Python 🐍

A classic, fully functional Snake game built using Python's built-in `turtle` module. Navigate the snake, eat the food, and try to beat your high score!

## Features
* **Classic Gameplay:** Control the snake using the arrow keys.
* **Dynamic Growth:** The snake extends its tail every time it eats food.
* **High Score Tracking:** Your highest score is automatically saved and persists across different game sessions using local file storage.
* **Collision Detection:** The game resets if you hit the screen borders or collide with your own tail.

## File Breakdown
* **`game.py`**: The main entry point that sets up the screen, listens for key strokes, and runs the main loop.
* **`snake.py`**: Contains the `Snake` class handling segment creation, continuous movement, and directional changes.
* **`food.py`**: Contains the `Food` class that spawns the food at random coordinates within the screen boundaries.
* **`scoreboards.py`**: Manages the UI text for the current score and interacts with `data.txt` to read/write the all-time high score.
* **`data.txt`**: A simple text file used for persistent high score storage.

## Getting Started

### Prerequisites
* **Python 3.x**: Ensure you have Python installed. The `turtle` module comes pre-installed with the standard Python library.

### How to Run
1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/snake-game-python.git](https://github.com/YOUR-USERNAME/snake-game-python.git)
