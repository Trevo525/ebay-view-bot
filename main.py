  GNU nano 4.7                                                                                                       main.py                                                                                                                 
import requests
import time
import multiprocessing.dummy as mp

#Made a global variable to pass through threading
listingURL = "www.ebay.com"

def view():
    print
    print (" --------------------------------------------")
    print (" viewbot v.1.0.0")
    print (" --------------------------------------------\n")
    global listingURL
    listingURL = input(" Link : ")
    print
    # viewCount = int(raw_input(" How many views? : "))
    viewCount = int(input(" How many views? : "))

    print
    print (" Watching ... ")
    print (" Do not close this window. ")

    print
    start_time = time.time()
    
    #adds threading support
    p=mp.Pool(4)
    p.map(addViews, range(0,viewCount))
    p.close()
    p.join()

    print (" Task completed! ")
    viewTime = float(time.time() - start_time)
    print(" Total time : " + " %s sec" % viewTime)
    viewRate = float(viewCount / viewTime)
    print (" View rate  : " +  " %s views/sec" % viewRate)
    print
    print

    # todo : iterate through other links in txt file, multithread, proxy support


def addViews(numIterations):
    r = requests.get(listingURL)


if __name__ == '__main__':
  view()

