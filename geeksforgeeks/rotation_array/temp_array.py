def rotation_array(arr , d , n) :
    d = d% n

    temp = arr[0:d]

    count = d
    while count < n :
        arr[count-d] = arr[count]
        count+=1

    # count = n-1
    # ind = -1
    # while count >= n-d :
    #     arr[count] = temp[ind]
    #     count-=1
    #     ind-=1
    arr[:] = arr[:n-d] + temp
    print(arr)    


rotation_array(arr= [1, 2, 3, 4, 5, 6, 7], d = 2, n =7)