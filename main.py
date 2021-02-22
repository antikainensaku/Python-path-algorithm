import os
import sys
import time

t_start = 0

def main():
    timer(True)
    try:
        with open("Python\Tietorakenteet ja Algoritmit\Lopputyö\graph_large_testdata\graph_ADS2018_500.txt", "r") as f:
            dest = f.readline().split()
            print("Number of cities: {} \nNumber of roads: {}\n".format(dest[0], dest[1]))
            timer(False)
    except IOError:
        print("\nThere was a problem opening the file.\n")

def timer(bool_var):
    global t_start
    if bool_var == True:
        t_start = time.time()  
    elif bool_var == False:
        t_end = time.time()
        t_final = t_end - t_start
        if t_final >= 1:
            print("Code ran in {:.4f} seconds".format(t_final))
        else:
            print("Code ran in {:.4f} milliseconds".format(t_final * 1000))
    else:
        print("\nThere was a problem with the timer.\n")

main()
