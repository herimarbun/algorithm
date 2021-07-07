# Finding peak element 1D of array of int

def findPeakRec(arr,low,high,n):
    mid = low + (low + high) / 2
    mid = int(mid)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
        (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return arr[mid]
    elif arr[mid] < arr[mid-1]:
        #find left
        return findPeakRec(arr,low,mid-1,n)
    else:
        #find right
        return findPeakRec(arr,mid+1,high,n)

def findPeak(arr, n):
 
    return findPeakRec(arr, 0, n - 1, n)
    
# Driver code
arr = [1,3,20,5,4,1,0,5,23,15,1]
n = len(arr)
print("Peak value is", findPeak(arr,n))
