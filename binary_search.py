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

    for i, value in enumerate(arr):
        ax.text(i, value + 0.5, str(value), ha='center', fontsize=8, color='black')
    
    return fig, ax, bars

    return fig, ax, bars

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

def binary_search_visualized(arr, target, bars, ax, pause_time=3.0):
    """
    Perform binary search of sorted array with visualization. 
    Parameters: 
    - arr: A sorted array (list or numpy array)
    - target: the value to search for in the array
    - bars: the bar chart objects
    - ax: the matplotlib axes
    - pause_time: time to pause between steps for visualization

    Returns: 
    - the index of the target if found, or -1 if not found
    """
    # define colors
    original_color = 'skyblue'
    range_color = '#ae7181' # color for current search range
    mid_color = '#650021'       # Color for the middle element
    target_color = '#01ff07' # color for the target (if found)

    # initialize pointers
    left, right = 0, len(arr) - 1

    # add text annotations for current state
    state_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, bbox=dict(facecolor='white', alpha=0.8))

    # binary search loop
    while left <= right: 
        for bar in bars:
            bar.set_color(original_color)

        # current search color
        for i in range(left, right + 1):
            bars[i].set_color(range_color)

        # calculating the middle index
        mid = (left + right) // 2

        # highlight the middle element
        bars[mid].set_color(mid_color)

        # update the state text
        state_text.set_text(f"Searching: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")

        # pause to show the current state
        plt.pause(pause_time)

        # check if the middle element is the target
        if arr[mid] == target: 
            for index in range(len(arr)):
                if index != mid:
                    bars[index].set_color(original_color)
            bars[mid].set_color(target_color)
            state_text.set_text(f"Found target {target} at index {mid}!")
            plt.pause(pause_time)
            return mid
        elif arr[mid] < target: 
            left = mid + 1
            state_text.set_text(f"Searching: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        else:
            right = mid - 1
            state_text.set_text(f"Searching: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        
    # exiting loop
    state_text.set_text(f"Target {target} not found in the array!")
    plt.pause(pause_time)
    return -1 # target not found

if __name__ == "__main__":
    print("Binary Search Visualization Program")

    array_size = 20
    random_array = np.random.randint(1, 100, size=array_size)

    print("Random array:", random_array)

    sorted_array = np.sort(random_array)

    print("Sorted array:", sorted_array)

    # prompting the user for input
    target = int(input("Enter the target value to search for: "))

    # set up the visualization
    fig, ax, bars = setup_visualization(sorted_array)
    plt.show(block=False)
    plt.pause(1)


    # run the binary search visualization algorithm
    index = binary_search_visualized(sorted_array, target, bars, ax)
    if index != -1: 
        print(f"Found target {target} at index {index}")
    else:
        print(f"Target {target} not found in the array")

    plt.show()