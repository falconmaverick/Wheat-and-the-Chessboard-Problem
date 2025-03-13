import numpy as np
import matplotlib.pyplot as plt

def create_chessboard(n: int, m: int) -> np.ndarray:
    """Creates an n x m chessboard filled with wheat counts based on the doubling rule."""
    indices = np.arange(n * m).reshape(n, m)
    board = 2 ** indices.astype(np.uint64)
    return board

def total_wheat(board: np.ndarray) -> int:
    """Calculates the total number of grains on the chessboard."""
    return np.sum(board)

def plot_wheat_distribution(board: np.ndarray):
    """Plots a heatmap to visualize the wheat distribution on the chessboard."""
    plt.xlabel("Column")
    plt.ylabel("Row")
    plt.title("Wheat Distribution on Chessboard")
    plt.pcolor(board, cmap='plasma')
    plt.colorbar(label="Number of grains")
    plt.show()

def compare_first_second_half(board: np.ndarray):
    """Compares the wheat count in the first half vs. the second half of the chessboard."""
    half = board.shape[0] // 2
    first_half = np.sum(board[:half, :])
    second_half = np.sum(board[half:, :])
    return second_half / first_half

if __name__ == "__main__":
    # Create an 8x8 chessboard
    chessboard = create_chessboard(8, 8)
    
    # Calculate total wheat grains
    total = total_wheat(chessboard)
    print(f"Total wheat grains on an 8x8 chessboard: {total}")
    
    # Visualize wheat distribution
    plot_wheat_distribution(chessboard)
    
    # Compare first and second half of the board
    ratio = compare_first_second_half(chessboard)
    print(f"The second half contains {ratio:.2f} times more wheat than the first half.")
