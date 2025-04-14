import matplotlib.pyplot as plt
import numpy as np
import time


def setup_visualization(arr, figsize=(10, 6)):
    """
    Set up the initial visualization of the array.
    
    Parameters:
    - arr: The sorted array to visualize
    - figsize: Size of the figure (width, height)
    
    Returns:
    - fig: The matplotlib figure
    - ax: The axes object
    - bars: The bar chart representing the array
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Create a bar chart of the array
    positions = np.arange(len(arr))
    bars = ax.bar(positions, arr, color='skyblue')
    
    # Customize the chart
    ax.set_xticks(positions)
    ax.set_xticklabels([str(i) for i in range(len(arr))])
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title('Binary Search Visualization')
    
    return fig, ax, bars

def binary_search_visualized(arr, target, bars, ax, pause_time=3.0):
    """
    Visualized binary search algorithm that shows each step.
    
    Parameters:
    - arr: The sorted array to search
    - target: The value to find
    - bars: The bar chart objects
    - ax: The matplotlib axes
    - pause_time: Time to pause between steps for visualization
    
    Returns:
    - The index of the target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    # Original bar colors
    original_color = '#be0119'
    
    # Color for the current range
    range_color = '#ae7181'
    
    # Color for the middle element
    mid_color = '#650021'
    
    # Color for the target (if found)
    target_color = '#01ff07'
    
    # Add a text annotation for current state
    state_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, 
                          bbox=dict(facecolor='white', alpha=0.8))
    
    while left <= right:
        # Reset all bars to original color
        for bar in bars:
            bar.set_color(original_color)
        
        # Color the current range
        for i in range(left, right + 1):
            bars[i].set_color(range_color)
        
        # Calculate the middle index
        mid = (left + right) // 2
        
        # Color the middle element
        bars[mid].set_color(mid_color)
        
        # Update the state text
        state_text.set_text(f"Searching: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        
        # Pause to show the current state
        plt.pause(pause_time)
        
        # Check if the middle element is the target
        if arr[mid] == target:
            bars[mid].set_color(target_color)
            state_text.set_text(f"Found target {target} at index {mid}!")
            plt.pause(pause_time)
            return mid
        elif arr[mid] < target:
            left = mid + 1
            state_text.set_text(f"arr[mid]={arr[mid]} < target={target}, moving left to {left}")
        else:
            right = mid - 1
            state_text.set_text(f"arr[mid]={arr[mid]} > target={target}, moving right to {right}")
        
        plt.pause(pause_time)
    
    # Target not found
    state_text.set_text(f"Target {target} not found in the array")
    plt.pause(pause_time)
    return -1

if __name__ == "__main__":
    arr = sorted([np.random.randint(1, 100) for _ in range(20)])
    print(f"Sorted array: {arr}")
    target = int(input("enter a number to search for: "))
    
    # Set up visualization
    fig, ax, bars = setup_visualization(arr)
    plt.show(block=False)
    
    # Run the visualized binary search
    result = binary_search_visualized(arr, target, bars, ax)
    print(f"Found {target} at index {result}")
    
    # Keep the plot open until user closes it
    plt.show()