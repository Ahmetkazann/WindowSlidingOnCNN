def bruteforce(arr, c):
    maxtotal = 0
    for i in range(len(arr) - c + 1):
        total = 0
        for j in range(c):
            total += arr[i + j]
        if total > maxtotal:
            maxtotal = total
    return maxtotal

def slidingwindow(arr, c):
    maxtotal = 0
    window = 0
    for j in range(c):
        window += arr[j]
        
    maxtotal = window
    for i in range(len(arr) - c):
        window = window - arr[i] + arr[i + c]
        if window > maxtotal:
            maxtotal = window
    return maxtotal


array = [8,16,4,15,1,24,9,5,13,21,3,2]
c = 3

maxtotal = bruteforce(array, c)
print(maxtotal)

maxtotal = slidingwindow(array, c)
print(maxtotal)

def bruteforcecnn(arr, c):
    newarray = []
    
    for i in range(len(arr) - c + 1):
        subarray = []
        for j in range(len(arr[0])- c + 1):
            total = 0
            for k in range(c):
                for s in range(c):
                    total += arr[i + k][j + s]
            subarray.append(total)
        newarray.append(subarray)
    return newarray
    
def slidingwindowcnn(arr, c):
    newarray = []
    rows = len(arr)
    cols = len(arr[0])
    
    for i in range(rows - c + 1): # calculete first window for each row
        subarray = []
        window = 0
        for a in range(c):
            for b in range(c):
                window += arr[i + a][b]
        subarray.append(window) 
        
        for j in range(1, cols - c + 1):

            for a in range(c):
                window -= arr[i + a][j - 1]
                window += arr[i + a][j + c - 1]
            subarray.append(window)
        newarray.append(subarray)
    
    return newarray

array = [[6,16,42,5,13,12],
         [9,86,36,15,31,23],
         [83,56,4,79,10,98],
         [81,8,34,8,19,14],
         [90,16,4,60,92,74],
         [1,64,43,17,1,44]]

c = 3 # 3x3 convolution
newarray = bruteforcecnn(array,3)
print(newarray)

newarray = slidingwindowcnn(array,3)
print(newarray)


