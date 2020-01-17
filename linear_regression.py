import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
value=pd.read_csv('E:\\linear_regression.txt')
X=value['X'][:80]
Y=value['Y'][:80]
tx=value['X'][81:]
ty=value['Y'][81:]
a=len(X)
rate=0.01
theta0=0
theta1=0
for i in range(5):
    hyp=(theta0*1)+(theta1*X.values)
    cost=0
    dos=0
    print(hyp[0],'Y is ',Y[0])
    for j in range(len(hyp)):
        cost=cost+(hyp[j]-Y.values[j])*1
        dos=dos+(hyp[j]-Y.values[j])*X.values[j]
    print('cost is :',cost,' dos is :',dos)
    theta0=theta0-(rate*((1/a)*cost))
    theta1=theta1-(rate*((1/a)*dos))
    print('theat0 is :',theta0,'  theta1 is :',theta1)
pred=(theta0*1)+(theta1*tx)
plt.scatter(X,Y)
plt.plot(tx,pred)
plt.show()
