class Solution:    
    def binarysearch(self, arr, n, k):
        # code here
        mid = n//2
#         left = arr[:mid+1]
#         right = arr[mid+1:]
        if k>arr[mid]:
            for i in range(mid+1,n,1):
                if k == arr[i]:
                    return i
            return -1
        elif k<arr[mid]:
            for i in range(0,mid+1,1):
                if k == arr[i]:
                    return i
            return -1
        elif k == arr[mid]:
            return mid
        else:
            return -1