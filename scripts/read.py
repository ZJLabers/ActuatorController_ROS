import matplotlib.pyplot as plt
import numpy as np

count=0
action=[]
num_act=6

for line in open('data.txt'):
    count+=1
    if count % 11 == 8:
        action.append(line[line.rfind("[")+1:line.rfind("]")].split(', '))

for i in range(len(action)):
    for j in range(num_act):
        action[i][j]=float(action[i][j])

hz = 100

size=127
joint=0

x = np.linspace(0.16,0.16+float(size)/hz,size)
y = np.zeros(size)

for i in range(size):
    y[i]=action[i][joint]

print(len(action))
plt.plot(x,y,color='b')

size1=112
count=0
hz1=100
action1=[]

for line in open('data1.txt'):
    count+=1
    if count % 11 == 8:
        action1.append(line[line.rfind("[")+1:line.rfind("]")].split(', '))

for i in range(len(action1)):
    for j in range(num_act):
        action1[i][j]=float(action1[i][j])

y1 = np.zeros(size1)

for i in range(size1):
    y1[i]=action1[i][joint]

x1 = np.linspace(0,float(size1)/hz,size1)
print(len(action1))
plt.plot(x1,y1,color='r')


plt.show()
