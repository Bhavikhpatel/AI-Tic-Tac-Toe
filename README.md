# AI Tic Tac Toe

A simple, unbeatable Tic-Tac-Toe game where you can challenge an AI opponent. This web application is built with Python and the [Streamlit](https://streamlit.io/) library. The AI's logic is powered by the Minimax algorithm with Alpha-Beta pruning, ensuring it always plays the optimal move.

---

## ✨ Features

-   **Unbeatable AI Opponent**: Play against an AI that will never make a losing move.
-   **Choose Your Symbol**: Start the game as either 'X' or 'O'. 'X' always goes first.
-   **Interactive Web Interface**: A clean, simple, and responsive UI built entirely in Python with Streamlit.
-   **Clear Game State**: Get immediate feedback on wins, draws, and whose turn it is.
-   **Restart Functionality**: Easily start a new game with a single click.

---

## 🧠 How the AI Works

The core of the AI opponent lies in the **Minimax algorithm**, a classic decision-making algorithm for two-player, zero-sum games.

### 1. Minimax Algorithm
The algorithm simulates all possible moves and their outcomes to find the best possible move. It works by assigning a score to each possible game state:
-   **AI Win**: A high positive score (e.g., +10).
-   **Human Win**: A high negative score (e.g., -10).
-   **Draw**: A neutral score (e.g., 0).

The AI, as the "maximizer," aims to choose a move that leads to the highest possible score. It assumes the human player, the "minimizer," will always play optimally to achieve the lowest possible score.

### 2. Alpha-Beta Pruning
This is an optimization technique for the Minimax algorithm. It reduces the number of game states the algorithm needs to evaluate by "pruning" branches of the game tree that are guaranteed to be worse than a move already found. This makes the AI's decision-making process significantly faster without sacrificing the quality of its move.

The `best_move()` function orchestrates this process by evaluating the Minimax score for every empty cell on the board and selecting the move that leads to the best outcome for the AI.

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You need to have Python 3.7+ installed.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone <url>
    cd your-repo-name
    ```

2.  **Install the required Python libraries:**
    ```sh
    pip install streamlit numpy
    ```

### Running the App

1.  Save the provided code as a Python file (e.g., `main.py`).

2.  Open your terminal, navigate to the project directory, and run the following command:
    ```sh
    streamlit run main.py
    ```

3.  Your default web browser will open a new tab with the game running locally.

---

## 📂 Code Overview

-   `app.py`: The single script containing the entire application.
    -   **`minimax(...)`**: The core recursive function implementing the Minimax algorithm with alpha-beta pruning to evaluate game states.
    -   **`best_move(...)`**: Iterates through all possible moves and uses `minimax` to find the optimal one for the AI.
    -   **`check_winner(...)`**: Checks the board for a winning line.
    -   **`is_board_full(...)`**: Checks if the board is full, resulting in a draw.
    -   **`reset_game()`**: A function to reset the game state using `st.session_state`.
    -   **Streamlit UI**: The main body of the script renders the web interface, handles user input through button clicks, and manages the game flow using `st.session_state` to maintain state across user interactions and reruns.
