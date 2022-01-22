def gcd(a,b) :
    if a%b == 0 :
        return b 
    return gcd(b,a%b)
def rotation_array(arr, d , n) :
    index = 0
    value = arr[0]
    count = 0
    k = gcd(n,d)
    while k>0:
        count = 0
        while count <= n/gcd(n,d):
            temp = (index -d)%n
            temp_value = arr[temp]
            arr[temp] = value
            index = temp
            value = temp_value
            count+=1
        k-=1
        index +=1
    print(arr)
rotation_array(arr= [1, 2, 3, 4, 5, 6, 7], d = 2, n =7)
# print(-3%7)



rotation_array(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] , d = 3 ,n=12)

