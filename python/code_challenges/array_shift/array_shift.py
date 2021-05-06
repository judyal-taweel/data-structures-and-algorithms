def shiftarray(arr,num):
    arr[int(len(arr)/2):int(len(arr)/2)] = [num]
    return arr

print(shiftarray([2,4,6,8], 5)) 