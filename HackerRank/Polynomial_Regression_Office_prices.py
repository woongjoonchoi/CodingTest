# Enter your code here. Read input from STDIN. Print output to STDOUT


import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


F,N = map(int,input().split())



X = np.arange(F * N , dtype  = np.float64).reshape(N,F )
Y = np.arange(N, dtype = np.float64).reshape(N,1)
for i in range(N) :
    *feat , y = input().split()
    X[i][:] = feat
    Y[i][:] = y

m = int(input())

# print(m)

test_x = np.arange(m*F ,dtype = np.float64).reshape(m,F)



for i in range(m) :
    test_x[i][:] = input().split()
  

poly3 = PolynomialFeatures(3)

new_x = poly3.fit_transform(X)
new_test_x = poly3.fit_transform(test_x)

    
lr = LinearRegression()

lr.fit(new_x,Y)

prediction = lr.predict(new_test_x)

for p in prediction :
    # print(p)
    print(round(p[0],2))
    
