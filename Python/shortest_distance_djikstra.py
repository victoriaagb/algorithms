#!/usr/bin/python
import sys
import heapq

### The Colonel Motors Corporation of Frankfort, Kentucky has produced a new line of vehicles which require chicken droppings for fuel.
### Because of this unusual fuel requirement, there are only certain fueling stations in the country where the vehicles can be refilled.
### Thus, to get from one place to another, an owner must plan a route that ensures that he can get refills along the way.
### The Colonel Motors Corporation has hired Professor Sanders of the Kentucky Institute of Technology as a consultant to prepare an online route-finding service.
### To use the computerized service, an owner will enter:
###     the driving range of his vehicle (the distance the vehicle can go on a single fill-up)
###     the "distance to empty" (the distance the vehicle can go with the fuel that's now in the tank)
###     his/her initial location (source), and his/her desired destination.
### The service will either respond with a shortest route from the source to the destination such that:
###     the owner never runs out of fuel
###     or it will deem that no such route exists.
### Model the professor's problem in terms of a weighted, directed graph in which:
###     streets are edges
###     intersections are vertices
###     intersections have fueling stations.
### Assume that a driver's source and destination are also at intersections.

def main(argv):

    while True:
        cityList = []
        fuelStation = []
        vertices = []

        #populate list of cities and fuel stations
        n = eval(input("Enter the number of cities: "
))
        for i in range (n):
            city, fuel = input().strip().split(",")
            cityList.append(city)
            fuelStation.append(eval(fuel))

        #populate vertices
        for i in range(n):
            miles = input().split(",")
            vList = []
            for j in range(n):
                if (eval(miles[j]) != 0):
                    vList.append((eval(miles[j]),j))
            vertices.append(vList)
        print()
        
        try:
            while True:
                #populate travel information
                source = input("Enter the source: ").strip()
                destination = input("Enter the destination: ").strip()
                startFuel = eval(input("Enter the starting fuel amount: "))
                capFuel = eval(input("Enter the fuel tank capacity: "))
                print()

                startI = cityList.index(source) 
                endI = cityList.index(destination)
                
                parents = [None] * n
                dist = [sys.maxsize] * n
                fuel = [sys.minsize] * n
                path = []
                doneQ = []
                
                dist[startI] = 0
                fuel[startI] = startFuel
                heapq.heapify(doneQ)
                heapq.heappush(doneQ, (0,startI))

                #Djikstra
                while len(doneQ) > 0:
                    #extract min vertex from heap
                    minV = heapq.heappop(doneQ)
                    i = minV[1]
                    print (minV)
                    #iterate adjacent vertices of min vertex
                    for vertex in vertices[i]:
                        j = vertex[1]
                        newDist = dist[i] + vertex[0]
                        #Relax adjacent vertex
                        if dist[j] > newDist :
                            dist[j] = newDist
                            parents[j] = i
                            #add adjacent vertex to heap
                            heapq.heappush(doneQ, vertex)

                #construct path through parents
                i = endI
                while i != None:
                    path.insert(0,i)
                    i = parents[i]
                
                print("The shortest route found is: ")
                for i in path:
                    print(cityList[i])
                
        except KeyboardInterrupt:
            pass
            
if __name__ == "__main__":
    main(sys.argv[1:])
