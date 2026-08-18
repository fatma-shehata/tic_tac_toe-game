# Tic Tac Toe — Django

A classic Tic Tac Toe game built with Django, rendered as an HTML/CSS/JavaScript template served through a Django view.

## Features
- 3x3 interactive game board
- Turn-based play for Player X and Player O
- Win and draw detection
- Restart button to start a new round

## Tech Stack
- Python / Django (backend, serves the template)
- HTML, CSS, JavaScript (game logic runs client-side)

## Project Structure
```
tic_tac_toe_game/
├── game/
│   ├── templates/
│   │   └── game/
│   │       └── index.html
│   ├── views.py
│   └── urls.py
├── tic_tac_toe_game/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## Setup & Run

1. Clone the repository
   ```bash
   git clone https://github.com/fatma-shehata/tic_tac_toe-game.git
   cd tic_tac_toe-game
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install Django
   ```bash
   pip install django
   ```

4. Run the development server
   ```bash
   python manage.py runserver
   ```

5. Open your browser at
   ```
   http://127.0.0.1:8000/
   ```

## How to Play
- Players take turns clicking empty cells to place X or O.
- The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.
- If all cells fill with no winner, the game ends in a draw.
- Click **Restart** to play again.

## Author
Fatma shehata ewas — Artificial Intelligence student, Kafr El-Sheikh University
