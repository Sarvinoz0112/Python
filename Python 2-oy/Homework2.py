# Python Code Examples

This repository contains examples of Python code for performing various tasks. It includes three examples:

1. Finding the indices of the minimum and maximum elements in a list.
2. Calculating the sum and count of positive odd numbers in a list.
3. Sorting parts of a list in different orders.

## Examples

### Example 1: Finding Indices of Minimum and Maximum Elements

This example demonstrates how to find the indices of the minimum and maximum elements in a list of 16 elements.

**Code:**

```python
def find_min_max_indices(my_list):
    min_index = my_list.index(min(my_list))
    max_index = my_list.index(max(my_list))
    return min_index, max_index
    
num_list = [2.2, 5.3, 8.5, 1.8, 4.3, 7.8, 3.4, 6.9, 9.1, 14.1, 25.0, 11.5, 21.6, 15.9, 22.4, 23.7, 17.1]

min_index, max_index = find_min_max_indices(num_list)

print(f"Index of the minimal element: {min_index}")
print(f"Index of the maximal element: {max_index}")
