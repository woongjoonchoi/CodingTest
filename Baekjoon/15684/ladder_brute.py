import sys
import itertools
N  ,M ,H = list(map(int,sys.stdin.readline().split()))
command = []
for i in range(M) :
    command.append(list(map(int , sys.stdin.readline().split())))
    

combi = [itertools.combinations()]