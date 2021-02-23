import os
import sys
import time

from algorithm import *

t_start = 0

def main():
    timer("start")
    opentxt()
    timer("end")

def opentxt():
    try:
        with open("Python\Tietorakenteet ja Algoritmit\Lopputyö\graph_testdata\graph_ADS2018_20.txt", "r") as f:
            dest = f.readline().split()
            g = WeightedGraph(dest[0])
            for line in range(int(dest[1])):
                data = f.readline().split()
                #DEBUGCODE# print("{}, {}, {}".format(data[0], data[1], data[2]))
                add_edge(g,int(data[0]),int(data[1]),int(data[2]))
            dijkstra(g,1)
            print('Path from 1 to {} with cumulative weights:'.format(int(dest[0])))
            print_path(g,int(dest[0]))
                
    except IOError:
        print("\nThere was a problem opening the file.\n")

def timer(var):
    global t_start
    if var == "start":
        t_start = time.time()  
    elif var == "end":
        t_end = time.time()
        t_final = t_end - t_start
        if t_final >= 1:
            print("Code ran in {:.4f} seconds".format(t_final))
        elif t_final < 0:
            print("Time was negative, something went wrong.")
        else:
            print("Code ran in {:.4f} milliseconds".format(t_final * 1000))
    else:
        print("\nThere was a problem with the timer.\n")

main()
