import os, time, sys, psutil

from dijkstra import *

t_start = 0

def main():
    menu()

def menu():
    print("\n----Description----\nLowest weight (height of a road) algorithm (modified dijkstra).")
    print("A truck driver is going from a to b with the objective of going through roads with the\nlowest possible height(weight).")
    while True:
        print("\nChoose an option:")
        print("1. Normal test data.")
        print("2. Large test data.")
        print("3. Quit.\n")
        try:
            inp = int(input("").strip().strip("."))
            if inp == 2:
                o1, o2, o3, o4, o5, o6, o7 = os.listdir(os.path.abspath("graph_large_testdata"))
                try:
                    inp = int(input("\nChoose a file (1-7):").strip().strip("."))
                    if inp == 1:
                        print("\nOpening graph_ADS2018_200.txt\n")
                        openandrun(os.path.abspath("graph_large_testdata\graph_ADS2018_200.txt"))
                    elif inp == 2:
                        print("\nOpening graph_ADS2018_300.txt\n")
                        openandrun(os.path.abspath("graph_large_testdata\graph_ADS2018_300.txt"))
                    elif inp == 3:
                        print("\nOpening graph_ADS2018_500.txt\n")
                        openandrun(os.path.abspath("graph_large_testdata\graph_ADS2018_500.txt"))
                    elif inp == 4:
                        print("\nOpening graph_ADS2018_750.txt\n")
                        openandrun(os.path.abspath("graph_large_testdata\graph_ADS2018_750.txt"))
                    elif inp == 5:
                        print("\nOpening graph_ADS2018_1000.txt\n")
                        openandrun(os.path.abspath("graph_large_testdata\graph_ADS2018_1000.txt"))
                    elif inp == 6:
                        print("\nOpening graph_ADS2018_1500.txt\n")
                        openandrun(os.path.abspath("graph_large_testdata\graph_ADS2018_1500.txt"))
                    elif inp == 7:
                        print("\nOpening graph_ADS2018_2000.txt\n")
                        openandrun(os.path.abspath("graph_large_testdata\graph_ADS2018_2000.txt"))
                    else:
                        print("\nThat input is not available.\n")
                except ValueError:
                    print("\nOnly input integers, please\n")
            elif inp == 1:
                o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11 = os.listdir(os.path.abspath("graph_testdata"))
                try:
                    inp = int(input("\nChoose a file (1-11):").strip().strip("."))
                    if inp == 1:
                        print("\nOpening graph_ADS2018_10_1.txt\n")
                        openandrun(os.path.abspath("graph_testdata\graph_ADS2018_10_1.txt"))
                    elif inp == 2:
                        print("\nOpening graph_ADS2018_10_2.txt\n")
                        openandrun(os.path.abspath("graph_testdata\graph_ADS2018_10_2.txt"))
                    elif inp == 3:
                        print("\nOpening graph_ADS2018_20.txt\n")
                        openandrun(os.path.abspath("graph_testdata\graph_ADS2018_20.txt"))
                    elif inp == 4:
                        print("\nOpening graph_ADS2018_30.txt\n")
                        openandrun(os.path.abspath("graph_testdata\graph_ADS2018_30.txt"))
                    elif inp == 5:
                        print("\nOpening graph_ADS2018_40.txt\n")
                        openandrun(os.path.abspath("graph_testdata\graph_ADS2018_40.txt"))
                    elif inp == 6:
                        print("\nOpening graph_ADS2018_50.txt\n")
                        openandrun(os.path.abspath("graph_testdata\graph_ADS2018_50.txt"))
                    elif inp == 7:
                        print("\nOpening graph_ADS2018_60.txt\n")
                        openandrun(os.path.abspath("graph_testdata\graph_ADS2018_60.txt"))
                    elif inp == 8:
                        print("\nOpening graph_ADS2018_70.txt\n")
                        openandrun(os.path.abspath("graph_testdata\graph_ADS2018_70.txt"))
                    elif inp == 9:
                        print("\nOpening graph_ADS2018_80.txt\n")
                        openandrun(os.path.abspath("graph_testdata\graph_ADS2018_80.txt"))
                    elif inp == 10:
                        print("\nOpening graph_ADS2018_90.txt\n")
                        openandrun(os.path.abspath("graph_testdata\graph_ADS2018_90.txt"))
                    elif inp == 11:
                        print("\nOpening graph_ADS2018_100.txt\n")
                        openandrun(os.path.abspath("graph_testdata\graph_ADS2018_100.txt"))
                    else:
                        print("\nThat input is not available.\n")
                except ValueError:
                    print("\nOnly input integers, please\n")
            elif inp == 3: #Näyttää hyvästelyviestin 1.5 sekunnin ajan ja sulkee pelin.
                print("\nSee ya' later, alligator!\n")
                time.sleep(1.5)
                sys.exit()
            else:
                print("\nThat input is not available.\n")
        except ValueError:
            print("\nOnly input integers, please.\n")

def openandrun(path):
    timer("start")
    try:
        with open(path, "r") as f:
            destination, verticeamount = f.readline().split()
            g = Graph(int(destination))
            for line in range(int(verticeamount)):
                cityStart, cityEnd, roadHeight = f.readline().split()
                add_edge(g, int(cityStart), int(cityEnd), int(roadHeight))
            dijkstra(g,1)
            print("\nPath from 1 to {} with the lowest peak height of a single road is:".format(int(destination)))
            print_path(g, int(destination))
            print("\nMaximum height of a single road: {}".format(g.distance[g.numOfVertices]))
    
    except IOError:
        print("\nThere was a problem opening the file.\n")
    memUsage = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
    timer("end")
    print("Program used {:.2f} MB of memory.".format(memUsage))
    

def timer(var):
    global t_start
    if var == "start":
        t_start = time.time()  
    elif var == "end":
        t_end = time.time()
        t_final = t_end - t_start
        if t_final >= 1:
            print("\nCode ran in {:.2f} seconds\n".format(t_final))
        elif t_final < 0:
            print("\nTime was negative, something went wrong.\n")
        else:
            print("\nCode ran in {:.1f} milliseconds\n".format(t_final * 1000))
    else:
        print("\nThere was a problem with the timer.\n")

main()
