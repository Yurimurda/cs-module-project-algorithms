'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    for i in range(arr):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
            
    while count < arr:
        arr[count] = 0
        count += 1
    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")