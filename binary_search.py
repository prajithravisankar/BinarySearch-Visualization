import matplotlib.pyplot as plt
import numpy as np

def setup_visualization(arr, figsize=(10, 6)):
    """
    Set up the initial visualization of the array. 


    Parameters:
    - arr: The array to visualize
    - figsize: the size of the figure (width, height)

    Returns: 
    - fig: the matplotlib figure
    - ax: the axes object
    - bars: bar chart representing the array
    """

    # create the matplotlib figure and axes object
    fig, ax = plt.subplots(figsize=figsize)

    # plot bar chart of the array
    positions = np.arange(len(arr))
    bars = ax.bar(positions, arr, color='skyblue')

    # add x-axis labels, y-axis labels, and title
    ax.set_xticks(positions)
    ax.set_xticklabels([str(i) for i in range(len(arr))])
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title('Binary Search Visualization')

    return fig, ax, bars


if __name__ == "__main__":
    print("Binary Search Visualization Program")

    array_size = 20
    random_array = np.random.randint(1, 100, size=array_size)

    print("Random array:", random_array)

    sorted_array = np.sort(random_array)

    print("Sorted array:", sorted_array)

    # set up the visualization
    fig, ax, bars = setup_visualization(sorted_array)
    plt.show()