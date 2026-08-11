def trap_water(n, heights):
    if n < 3: 
        return 0  
        
    left = 0
    right = n - 1
    
    left_max = heights[left]
    right_max = heights[right]
    total_water = 0
    
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, heights[left])
            total_water += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            total_water += right_max - heights[right]
            
    return total_water

n = 6
heights = [3, 0, 0, 2, 0, 4]
print(trap_water(n, heights))