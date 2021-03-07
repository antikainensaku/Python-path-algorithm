'''
By Saku Antikainen
Student number: 2636168

'''
import os, time, sys
#import psutil #(psutil used for calculating memory usage)

from dijkstra import *

t_start = 0

def main():
    menu()

'''just an simple and not so pretty way of creating a menu with if statements'''
def menu():
    print("\n----Description----\nLowest weight (height of a road) algorithm (modified dijkstra).")
    print("A truck driver is going from a to b with the objective of going through roads with the\nlowest possible height(weight).")
    while True:
        print("\nChoose an option:")
        print("1. Normal test data.")
        print("2. Large test data.")
        print("3. Quit.\n")
        try:
            inp = int(input("").strip().strip("."))     #stripping out spaces and dots
            if inp == 1:          #normal testdata
                while True:
                    try:
                        inp = input("\nChoose a file between 1-11(c to cancel):").strip().strip(".").lower()
                        if inp == "1":
                            print("\nOpening graph_ADS2018_10_1.txt\n")
                            openandrun(os.path.abspath("graph_testdata\graph_ADS2018_10_1.txt"))
                            break
                        elif inp == "2":
                            print("\nOpening graph_ADS2018_10_2.txt\n")
                            openandrun(os.path.abspath("graph_testdata\graph_ADS2018_10_2.txt"))
                            break
                        elif inp == "3":
                            print("\nOpening graph_ADS2018_20.txt\n")
                            openandrun(os.path.abspath("graph_testdata\graph_ADS2018_20.txt"))
                            break
                        elif inp == "4":
                            print("\nOpening graph_ADS2018_30.txt\n")
                            openandrun(os.path.abspath("graph_testdata\graph_ADS2018_30.txt"))
                            break
                        elif inp == "5":
                            print("\nOpening graph_ADS2018_40.txt\n")
                            openandrun(os.path.abspath("graph_testdata\graph_ADS2018_40.txt"))
                            break
                        elif inp == "6":
                            print("\nOpening graph_ADS2018_50.txt\n")
                            openandrun(os.path.abspath("graph_testdata\graph_ADS2018_50.txt"))
                            break
                        elif inp == "7":
                            print("\nOpening graph_ADS2018_60.txt\n")
                            openandrun(os.path.abspath("graph_testdata\graph_ADS2018_60.txt"))
                            break
                        elif inp == "8":
                            print("\nOpening graph_ADS2018_70.txt\n")
                            openandrun(os.path.abspath("graph_testdata\graph_ADS2018_70.txt"))
                            break
                        elif inp == "9":
                            print("\nOpening graph_ADS2018_80.txt\n")
                            openandrun(os.path.abspath("graph_testdata\graph_ADS2018_80.txt"))
                            break
                        elif inp == "10":
                            print("\nOpening graph_ADS2018_90.txt\n")
                            openandrun(os.path.abspath("graph_testdata\graph_ADS2018_90.txt"))
                            break
                        elif inp == "11":
                            print("\nOpening graph_ADS2018_100.txt\n")
                            openandrun(os.path.abspath("graph_testdata\graph_ADS2018_100.txt"))
                            break
                        elif inp == "c":
                            break
                        else:       #prints error for invalid input
                            print("\nInvalid input.\n")
                    except ValueError:      #prints error for invalid input
                        print("\nInvalid input.\n")
            elif inp == 2:        #large testdata
                while True:
                    try:
                        inp = input("\nChoose a file between 1-7(c to cancel):").strip().strip(".").lower()
                        if inp == "1":
                            print("\nOpening graph_ADS2018_200.txt\n")
                            openandrun(os.path.abspath("graph_large_testdata\graph_ADS2018_200.txt"))
                            break
                        elif inp == "2":
                            print("\nOpening graph_ADS2018_300.txt\n")
                            openandrun(os.path.abspath("graph_large_testdata\graph_ADS2018_300.txt"))
                            break
                        elif inp == "3":
                            print("\nOpening graph_ADS2018_500.txt\n")
                            openandrun(os.path.abspath("graph_large_testdata\graph_ADS2018_500.txt"))
                            break
                        elif inp == "4":
                            print("\nOpening graph_ADS2018_750.txt\n")
                            openandrun(os.path.abspath("graph_large_testdata\graph_ADS2018_750.txt"))
                            break
                        elif inp == "5":
                            print("\nOpening graph_ADS2018_1000.txt\n")
                            openandrun(os.path.abspath("graph_large_testdata\graph_ADS2018_1000.txt"))
                            break
                        elif inp == "6":
                            print("\nOpening graph_ADS2018_1500.txt\n")
                            openandrun(os.path.abspath("graph_large_testdata\graph_ADS2018_1500.txt"))
                            break
                        elif inp == "7":
                            print("\nOpening graph_ADS2018_2000.txt\n")
                            openandrun(os.path.abspath("graph_large_testdata\graph_ADS2018_2000.txt"))
                            break
                        elif inp == "c":
                            break
                        else:
                            print("\nInvalid input.\n")
                    except ValueError:
                        print("\nInvalid input.\n")
            elif inp == 3:      #quit program
                print("\nSee ya' later, alligator!\n")
                time.sleep(1.5)
                sys.exit()
            else:       #prints error for invalid input
                print("\nInvalid input.\n")
        except ValueError:      #prints error for invalid input
            print("\nInvalid input.\n")

def openandrun(path):
    timer("start")
    try:
        with open(path, "r") as f:
            destination, verticeamount = f.readline().split()   #open first line to get destination
            g = Graph(int(destination))                         # and amount of vertices
            for line in range(int(verticeamount)):      #go through every line in file
                cityStart, cityEnd, roadHeight = f.readline().split()   #save values to variables
                add_edge(g, int(cityStart), int(cityEnd), int(roadHeight))  #create edge with the variables
            dijkstra(g,1)   #execute (modified)dijkstra algorithm on the graph
            print("\nPath from 1 to {} with the lowest peak height of a single road is:".format(int(destination)))
            print_path(g, int(destination))
            print("\nMaximum height of path: {}".format(g.distance[g.numOfVertices]))
    
    except IOError:
        print("\nThere was a problem opening the file.\n")
    except ValueError:
        print("No path from 1 to {} available.".format(int(destination)))
    else:
        timer("end")
    '''
    #print memory usage
    memUsage = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
    print("Program used {:.2f} MB of memory.".format(memUsage))
    '''

'''Timer for algorithm run times'''
def timer(var):
    global t_start
    if var == "start":      #start time
        t_start = time.time()  
    elif var == "end":      #end time
        t_end = time.time()
        t_final = t_end - t_start
        if t_final >= 1 and t_final <= 60:    #if time between 1 and 30 second(s)
            print("\nCode ran in {:.2f} seconds\n".format(t_final)) #display time in seconds
        elif t_final >= 0 and t_final < 1:   #if time under 1000 milliseconds
            print("\nCode ran in {:.1f} milliseconds\n".format(t_final * 1000)) 
            #display time in milliseconds
        else:       # if test too long (60 seconds)
            print("\nTest took over 60 seconds.\n")
    else:
        print("\nThere was a problem with the timer.\n")

main()
