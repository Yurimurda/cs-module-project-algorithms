'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    
    count = 0
    # Your code here
    # loop within the range of the array it's length
    for i in range (len(arr)):
        # if the interger in the array does not equal 0, add 1
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
            
    while count < len(arr):
        arr[count] = 0
        count += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")