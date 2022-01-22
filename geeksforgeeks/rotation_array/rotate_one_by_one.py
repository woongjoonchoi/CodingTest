def rotation_array(arr, d , n) :
    d = d% n
    
    # for i in range(d) :
    #     for j in range(n) :
            
    
    for j in range(d) :
        temp  = arr[0]
        for  i in range(n-1) :
            arr[i] = arr[i+1]
        arr[n-1] = temp
    print(arr)
    
rotation_array(arr= [1, 2, 3, 4, 5, 6, 7], d = 2, n =7)