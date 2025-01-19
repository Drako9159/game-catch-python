# Catcher Game

## Description
Catcher Game is a fun and engaging game where you control a basket to catch falling apples. The game is controlled using the arrow keys on your keyboard. The main configuration file allows you to adjust the difficulty level to HARD, MEDIUM, or EASY. The game keeps track of the number of catches and misses, managing a score and increasing the falling speed of the apples with each catch. Additionally, the basket's movement speed slightly increases as well.

## Requirements
- Python 3.6 or higher
- Pygame library

## Installation
1. Clone the repository:
    ```sh
    git clone <REPOSITORY_URL>
    cd game-catch-python
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.md
    ```

## Usage
To start the game, run the [game.py](http://_vscodecontentref_/0) script:

```sh
python game.py
```

Controls
- Use the left and right arrow keys to move the basket.

## Controls
- Use the left and right arrow keys to move the basket.

## Configuration
You can adjust the difficulty level in the game.py file by setting the difficulty variable to one of the following options:


## Game Mechanics
- Score: The game keeps track of the number of apples caught.
- Lives: The player starts with a set number of lives. Missing an apple decreases the number of lives.
- Apple Velocity: The falling speed of the apples increases with each catch.
- Basket Velocity: The movement speed of the basket slightly increases with each catch.

Example

```python
# filepath: /home/master/apps/game-catch-python/game.py

# Set difficulty level
difficulty = MEDIUM
```



License
This project is licensed under the MIT License. See the LICENSE file for details.