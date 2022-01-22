
def reversal(arr , first , second) :
    while first < second :
        arr[first]  ,arr[second]  = arr[second]  ,arr[first]
        first +=1
        second -=1
def rotation_array(arr , d , n) :

    reversal(arr,0,d-1)
    reversal(arr,d,n-1)
    reversal(arr,0,n-1)
    # arr[:] = arr[:n-d] + temp
    print(arr)    
