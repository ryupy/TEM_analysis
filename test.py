import sys
import math
#標準入力は
#N
#1 x y
#...
#N x_N y_N
#を想定
#N = int(input())
#axon = [list(map(int, input().split())) for _ in range(N)]
with open('Results.csv', 'r') as result:
    N = int(result.readline())
    axon = result.readlines()
    for i in range(N):
        axon[i] = axon[i].split(',')
result.close()

cluster_dis = 0.3
cluster = []
alredy = []
Average_list = []

for i in range(N):
    for j in range(N):
        alredy.append(i)
        if j not in alredy:
            dis = math.sqrt((float(axon[i][1]) - float(axon[j][1])) ** 2 + (float(axon[i][2]) - float(axon[j][2])) ** 2)
            #Average_list.append(dis)
            if dis <= cluster_dis and dis != 0:
                cluster.append(str(i+1)+'-'+str(j+1))
                cluster.append(dis)
print(cluster)
#Average = sum(Average_list) / N
#print(Average)
