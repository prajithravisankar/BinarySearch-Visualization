import matplotlib.pyplot as plt
import numpy as np

def binary_search(arr, target):
    """
    Perform binary search on a sorted array. 

    Parameters:
    - arr: A sorted array (list or numpy array)
    - target: The value to search for in an array

    Returns: 
    - index: the index of the target if found, else - 1 if not found
    """
    # Initialize left and right pointers
    left, right = 0, len(arr) - 1

    # search until the pointers cross each other
    while left <= right: 
        # calculate the middle index
        mid = (left + right) // 2

        # check if the middle element is the target
        if arr[mid] == target:
            return mid
        elif arr[mid] < target: 
            left = mid + 1
        else:
            right = mid - 1
    
    return - 1  # target not found


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
    plt.show(block=False)
    plt.pause(5)

    # testing binary search function
    targets = [sorted_array[0], sorted_array[-1], 999]

    for target in targets:
        print(f"Searching for {target}...")
        index = binary_search(sorted_array, target)
        if index != -1:
            print(f"Found {target} at index {index}")
        else:
            print(f"{target} not found in the array")