#!/usr/bin/python
import sys
import copy
import heapq

### Private instructions and requirements. I cannot post.

def main(argv):

    while True:
        cityList = []
        fuelStation = []
        vertices = []

        #populate list of cities and fuel stations
        n = eval(input("Enter the number of cities: "))
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
        printVertices(vertices)

        try:
            while True:
                try:
                    print()
                    #populate travel information
                    source = input("Enter the source: ").strip()
                    destination = input("Enter the destination: ").strip()
                    startFuel = eval(input("Enter the starting fuel amount: "))
                    capFuel = eval(input("Enter the fuel tank capacity: "))
                    print()

                    startI = cityList.index(source) 
                    endI = cityList.index(destination)
                    path = []


                    endV, path, distV, fuelV = (shortestPath((0,startI),
                                                             startI,
                                                             endI,
                                                             vertices,
                                                             path, 0 ,
                                                             startFuel,
                                                             capFuel,
                                                             fuelStation))

                    #construct path with results
                    if endV:
                        print("The shortest route found is: ")
                        for i in path:
                            print(cityList[i])
                        print()
                        print("Total miles: " +  str(distV))
                        print("Current fuel: " + str(fuelV))
                    else:
                        print("No such path from " +
                              str(cityList[startI]) + " to " +
                              str(cityList[endI]) + " exists")
                        print("with and initial " + str(startFuel) + " fuel amount " +
                              " and " + str(capFuel) + " tank capacity.")
                        
                except Exception as e:
                    print()
                    print(e)
                    pass
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print()
            print(e)
            pass

def shortestPath(startV, startI, endI, vertices, path, miles, fuel, capFuel, fuelStation):

    parent = None if len(path) == 0 else path[-1]
    i = startV[1]
    fuel = capFuel if fuelStation[i] else fuel
    endV = None
    distV = miles
    path = path + [i]
    pathV = copy.deepcopy(path)
    fuelV = fuel
    
    #iterate adjacent vertices
    if (startI == endI):
        endV = startV
        return (endV, pathV, distV, fuelV)
    for vertex in vertices[i]: 
        j = vertex[1]
        inPath = j in path
        #calculate new distances and fuel to current vertex
        newDist = miles + vertex[0]
        newFuel = fuel - vertex[0]
        #vertex is destination
        if newFuel >= 0 and vertex[1] == endI:
            if not endV or distV > newDist:
                endV = vertex
                pathV = path + [j]
                distV = newDist
                fuelV = newFuel
        #vertex recurrence until end of tree
        elif (newFuel >= 0 and not inPath):
            endT, pathT, distT, fuelT = shortestPath(vertex, startI, endI, vertices, path, newDist, newFuel, capFuel, fuelStation)
            if (endT):
                if not endV or distV > distT:
                    endV = endT
                    pathV = pathT
                    distV = distT
                    fuelV = fuelT

    return (endV, pathV, distV, fuelV)    

def printVertices(vertices):
    for line in vertices:
        print(line)
    print()        
            
if __name__ == "__main__":
    main(sys.argv[1:])
