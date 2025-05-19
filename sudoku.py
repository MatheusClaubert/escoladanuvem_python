#sudoku em python
import random
import time
import math
import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import matplotlib.animation as animation
import matplotlib.ticker as ticker
from matplotlib.widgets import Button
from matplotlib import gridspec
from matplotlib import rcParams
from matplotlib import rc

# Configurações do matplotlib
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']
rcParams['font.size'] = 12
rcParams['axes.titlesize'] = 16
rcParams['axes.labelsize'] = 14
rcParams['xtick.labelsize'] = 12
rcParams['ytick.labelsize'] = 12
rcParams['legend.fontsize'] = 12
rcParams['figure.titlesize'] = 16
rcParams['figure.figsize'] = (8, 8)
rcParams['figure.dpi'] = 100
rcParams['axes.labelweight'] = 'bold'
rcParams['axes.titleweight'] = 'bold'
rcParams['axes.grid'] = True
rcParams['axes.grid.axis'] = 'both'
rcParams['axes.grid.which'] = 'major'
rcParams['axes.grid.color'] = 'gray'
rcParams['axes.grid.linestyle'] = '--'
rcParams['axes.grid.linewidth'] = 0.5
rcParams['axes.grid.alpha'] = 0.7
rcParams['grid.color'] = 'gray'
rcParams['grid.linestyle'] = '--'
rcParams['grid.linewidth'] = 0.5
rcParams['grid.alpha'] = 0.7
rcParams['xtick.major.size'] = 5
rcParams['xtick.minor.size'] = 3
rcParams['xtick.major.width'] = 1
rcParams['xtick.minor.width'] = 0.5
rcParams['ytick.major.size'] = 5
rcParams['ytick.minor.size'] = 3
rcParams['ytick.major.width'] = 1
rcParams['ytick.minor.width'] = 0.5
rcParams['legend.frameon'] = True
rcParams['legend.framealpha'] = 0.8
rcParams['legend.loc'] = 'best'
rcParams['legend.borderpad'] = 0.5
rcParams['legend.labelspacing'] = 0.5
rcParams['legend.handlelength'] = 2
rcParams['legend.handleheight'] = 0.5


# Função para criar um tabuleiro de Sudoku vazio
def create_empty_board():
    return [[0 for _ in range(9)] for _ in range(9)]
# Função para verificar se um número pode ser colocado em uma posição específica
def is_valid(board, row, col, num):
    # Verifica se o número já está na linha
    if num in board[row]:
        return False

    # Verifica se o número já está na coluna
    for r in range(9):
        if board[r][col] == num:
            return False

    # Verifica se o número já está no quadrante 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True
# Função para resolver o Sudoku usando backtracking
def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Sudoku resolvido

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Desfaz a atribuição se não funcionar

    return False
# Função para encontrar a próxima célula vazia
def find_empty_cell(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None
# Função para gerar um tabuleiro de Sudoku completo
def generate_complete_board():
    board = create_empty_board()
    fill_board(board)
    return board
# Função para preencher o tabuleiro de Sudoku
def fill_board(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                num = random.randint(1, 9)
                while not is_valid(board, r, c, num):
                    num = random.randint(1, 9)
                board[r][c] = num

    return board
# Função para remover números do tabuleiro para criar um quebra-cabeça
def remove_numbers(board, num_to_remove):
    count = num_to_remove
    while count > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            count -= 1
    return board
# Função para gerar um quebra-cabeça de Sudoku
def generate_sudoku_puzzle(num_to_remove):
    board = generate_complete_board()
    puzzle = remove_numbers(board, num_to_remove)
    return puzzle
# Função para exibir o tabuleiro de Sudoku
def display_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))
    print()
# Função para verificar se o Sudoku está completo
def is_complete(board):
    for row in board:
        if 0 in row:
            return False
    return True
# Função para verificar se o Sudoku está correto
def is_correct(board):
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num != 0 and not is_valid(board, r, c, num):
                return False
    return True
# Função para verificar se o Sudoku é válido
def is_valid_sudoku(board):
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num != 0 and not is_valid(board, r, c, num):
                return False
    return True
# Função para verificar se o Sudoku é resolvível
def is_solvable(board):
    return solve_sudoku(copy.deepcopy(board))
# Função para verificar se o Sudoku é único
def is_unique(board):
    count = 0
    def count_solutions(board):
        nonlocal count
        empty_cell = find_empty_cell(board)
        if not empty_cell:
            count += 1
            return

        row, col = empty_cell

        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                count_solutions(board)
                board[row][col] = 0

    count_solutions(copy.deepcopy(board))
    return count == 1
# Função para verificar se o Sudoku é válido e resolvível
def is_valid_and_solvable(board):
    return is_valid_sudoku(board) and is_solvable(board)
# Função para verificar se o Sudoku é único e resolvível
def is_unique_and_solvable(board):
    return is_unique(board) and is_solvable(board)
# Função para verificar se o Sudoku é completo e correto
def is_complete_and_correct(board):
    return is_complete(board) and is_correct(board)
# Função para verificar se o Sudoku é válido, completo e correto
def is_valid_complete_and_correct(board):
    return is_valid_sudoku(board) and is_complete_and_correct(board)
# Função para verificar se o Sudoku é válido, completo e correto
