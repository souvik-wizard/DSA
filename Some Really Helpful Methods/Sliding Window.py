 #Sliding window technique

 
def fixed_sliding_window(arr: List[int] , k: int) -> List[int] :
    # Sum up the first subarray and add it to the result
    curr_subarray = sum(arr[:k])
    result = [curr_subarray]
    # To get each subsequent subarray, add the next value in
    # the list and remove the first value
    for i in range(1, len(arr)-k+1) :
        curr_subarray = curr_subarray - arr[i-1]
        curr_subarray = curr_subarray + arr[i+k-1]
        result.append(curr_subarray)
    return result





#Dynamic Sliding window technique


def dynamic_sliding_window(arr: List[int] , x: int) -> int:
    # Track our min value
    min_length = float( ' int')
    # The current range and sum of our sliding window
    start = 0
    end = 0
    current_sum = 0
    # Extend the sliding window until our criteria is met
    while end < len(arr):
        current_sum = current_sum + arr[end]
        end = end + 1
        # Then contract the sliding window until it
        # no longer meets our condition
        while start < end and current_sum >= x:
            current_sum = current_sum - arr[start]
            start = start + 1
            # Update the min_length if this is shorter
            #than the current min
            min_length = min(min_length, end-start+1)
    return min_length