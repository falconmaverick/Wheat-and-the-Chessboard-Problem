import numpy as np
import matplotlib.pyplot as plt

def create_chessboard(n: int, m: int) -> np.ndarray:
    """Creates an n x m chessboard filled with wheat counts using NumPy broadcasting."""
    indices = np.arange(n * m, dtype=np.uint64).reshape(n, m)  # Ensure correct dtype
    board = 2 ** indices  # Broadcasting used here
    return board

def total_wheat(board: np.ndarray) -> int:
    """Calculates the total number of grains on the chessboard."""
    return np.sum(board)

def plot_wheat_distribution(board: np.ndarray):
    """Plots a heatmap to visualize the wheat distribution on the chessboard."""
    plt.xlabel("Column")
    plt.ylabel("Row")
    plt.title("Wheat Distribution on Chessboard")
    plt.pcolor(board, cmap='viridis', shading='auto')  # Better color map & proper shading
    plt.colorbar(label="Number of grains")
    plt.show()

def plot_column_averages(board: np.ndarray):
    """Calculates and plots the average number of wheat grains per column."""
    col_means = np.mean(board, axis=0)
    plt.figure(figsize=(10, 5))
    plt.bar(range(1, board.shape[1] + 1), col_means, color='orange')
    plt.xlabel("Column")
    plt.ylabel("Average Wheat Count")
    plt.title("Average Wheat Count per Column")
    plt.show()

def compare_first_second_half(board: np.ndarray):
    """Compares the wheat count in the first half vs. the second half of the chessboard."""
    half = board.size // 2  # Total elements divided by 2
    first_half = np.sum(board.flat[:half])  # First half of flattened array
    second_half = np.sum(board.flat[half:])  # Second half of flattened array
    return second_half / first_half

# Performance measurement code (Jupyter Notebook)
def measure_performance():
    import timeit
    
    setup_code = "import numpy as np"
    
    list_append_time = timeit.timeit(
        stmt="[2 ** i for i in range(64)]", setup=setup_code, number=10000
    )
    
    np_append_time = timeit.timeit(
        stmt="np.append(np.array([], dtype=np.uint64), [2 ** i for i in range(64)])",
        setup=setup_code, number=10000
    )
    
    np_broadcast_time = timeit.timeit(
        stmt="2 ** np.arange(64, dtype=np.uint64)", setup=setup_code, number=10000
    )
    
    print(f"List append time: {list_append_time:.6f} seconds")
    print(f"np.append time: {np_append_time:.6f} seconds")
    print(f"NumPy broadcasting time: {np_broadcast_time:.6f} seconds")

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
    
    # Plot column averages
    plot_column_averages(chessboard)

    # Measure performance
    measure_performance()
