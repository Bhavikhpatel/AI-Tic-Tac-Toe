import streamlit as st
import numpy as np

def minimax(board, depth, is_maximizing, alpha, beta, ai_symbol, human_symbol):
    winner = check_winner(board)
    if winner == ai_symbol:
        return 10 - depth
    elif winner == human_symbol:
        return depth - 10
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = ai_symbol
                    eval = minimax(board, depth + 1, False, alpha, beta, ai_symbol, human_symbol)
                    board[i][j] = ""
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = human_symbol
                    eval = minimax(board, depth + 1, True, alpha, beta, ai_symbol, human_symbol)
                    board[i][j] = ""
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board, ai_symbol, human_symbol):
    best_score = -np.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = ai_symbol
                score = minimax(board, 0, False, -np.inf, np.inf, ai_symbol, human_symbol)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != "" for row in board for cell in row)

def reset_game():
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.turn = "human"
    st.session_state.human_symbol = "X"
    st.session_state.ai_symbol = "O"
    st.session_state.game_over = False
    st.session_state.chosen = False
    st.session_state.last_click = None

def on_click_cell(i, j):
    if st.session_state.board[i][j] == "" and not st.session_state.game_over:
        st.session_state.last_click = (i, j)

st.set_page_config(page_title="AI Tic Tac Toe", layout="centered")
st.title("AI Tic Tac Toe")

if "board" not in st.session_state:
    reset_game()

if not st.session_state.chosen:
    st.subheader("Choose your symbol:")
    choice = st.radio("Select", ["X", "O"])
    if st.button("Start Game"):
        st.session_state.human_symbol = choice
        st.session_state.ai_symbol = "O" if choice == "X" else "X"
        st.session_state.turn = "human" if choice == "X" else "ai"
        st.session_state.chosen = True
        st.experimental_rerun = None

if st.session_state.chosen:
    if st.session_state.turn == "ai" and not st.session_state.game_over:
        move = best_move(st.session_state.board, st.session_state.ai_symbol, st.session_state.human_symbol)
        if move != (-1, -1):
            st.session_state.board[move[0]][move[1]] = st.session_state.ai_symbol
            winner = check_winner(st.session_state.board)
            if winner:
                st.session_state.game_over = True
                st.success(f"{winner} wins!")
            elif is_board_full(st.session_state.board):
                st.session_state.game_over = True
                st.info("It's a draw!")
            else:
                st.session_state.turn = "human"

    if "last_click" not in st.session_state:
        st.session_state.last_click = None

    st.subheader("Game Board:")
    cols = st.columns(3)
    for i in range(3):
        for j in range(3):
            with cols[j]:
                key = f"{i}-{j}"
                val = st.session_state.board[i][j]
                if val == "" and not st.session_state.game_over:
                    st.button(" ", key=key, use_container_width=True, on_click=on_click_cell, args=(i,j))
                else:
                    st.markdown(
                        f"<div style='text-align:center; font-size: 30px;'>{val}</div>",
                        unsafe_allow_html=True,
                    )

    if st.session_state.last_click and not st.session_state.game_over:
        i, j = st.session_state.last_click
        if st.session_state.board[i][j] == "":
            st.session_state.board[i][j] = st.session_state.human_symbol
            st.session_state.last_click = None
            winner = check_winner(st.session_state.board)
            if winner:
                st.session_state.game_over = True
                st.success(f"{winner} wins!")
            elif is_board_full(st.session_state.board):
                st.session_state.game_over = True
                st.info("It's a draw!")
            else:
                st.session_state.turn = "ai"

    if st.session_state.game_over:
        if st.button("🔁 Restart Game"):
            reset_game()
