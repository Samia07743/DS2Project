import geocoder
import geopy
import numpy as np
import geopy.distance
from geopy.geocoders import Nominatim
from Final_pairing_heap import *

#get locaiton of the user directly
def choose1():
    ip = geocoder.ip('me')
    user_loc=ip.latlng
    user_loc=(user_loc[1], user_loc[0])
    return user_loc

#get distance between 2 latitude longitude coordinates 
def distance(loc1, loc2):
    ans= geopy.distance.geodesic(loc1, loc2).km
    return ans

#find the closest node from a certain location
def nearest_node(userloc, G):
    # This function takes a user location (userloc) and a graph (G) as inputs
    em=[]
    # Create an empty list to store the distance between userloc and each node in the graph
    for i in G:
        # Loop through each node in the graph
        coords_1 = (userloc[0], userloc[1]) #coordinats of user
        # Get the coordinates of the user
        value = G[i]
        # Get the value (i.e. coordinates) of the current node
        lng_h, lat_h = value[0], value[1]
        # Get the longitude and latitude of the current node
        coords_2 = (lng_h, lat_h)            #coordinates of hospital
        # Combine the longitude and latitude to get the coordinates of the current node
        ans = geopy.distance.geodesic(coords_2, coords_1).km
        # Calculate the distance (in kilometers) between the user location and the current node
        em.append([i, ans])
        # Add the current node and its distance to the em list
    least=''
    #Create an empty string to store the name of the node that is closest to the user
    value=999999999999
    
    # Set the initial value of the closest distance to a very high number
    for i in em:       #i = [hospital name, distance]
        # Loop through each node and its distance from the user
        if i[1]<value:
            # If the distance is less than the current closest distance
            least = i[0]
            # Set the name of the current node as the closest node
            value = i[1]
            # Set the distance of the current node as the closest distance
    return least, value
    # Return the name and distance of the closest node to the user


def dijkstra(graph, start):
    heap = PairingHeap()    # create a new PairingHeap instance
    distance = {}           # create a dictionary to store the distance from the start vertex to each vertex in the graph
    previous = {}           # create a dictionary to store the previous vertex in the shortest path from the start vertex to each vertex in the graph
    for vertex in graph:    # initialize the distance and previous dictionaries
        distance[vertex] = float('inf')
        previous[vertex] = None

    distance[start] = 0     # set the distance from the start vertex to itself to 0
    heap.insert(0, start)   # insert the start vertex with a distance of 0 into the heap

    while not heap.is_empty():  # continue until the heap is empty
        min_distance, current_vertex = heap.delete_min()    # remove the vertex with the smallest distance from the heap
        for neighbor, weight in graph[current_vertex].items():   # for each neighbor of the current vertex
            new_distance = distance[current_vertex] + weight    # calculate the distance from the start vertex to the neighbor via the current vertex
            if new_distance < distance[neighbor]:   # if the new distance is smaller than the previous distance
                distance[neighbor] = new_distance  # update the distance dictionary
                previous[neighbor] = current_vertex    # update the previous dictionary
                heap.insert(new_distance, neighbor)    # insert the neighbor with its new distance into the heap
    print("Distance==", distance)
    print("Previous==", previous)
    return distance, previous   # return the distance and previous dictionaries


def getShortestPath(graph, start, end):
    distance, previous = dijkstra(graph, start)    # find the shortest path from the start vertex to every other vertex in the graph
    path = []   # create an empty list to store the shortest path
    while end is not None:   # starting from the end vertex, add each previous vertex in the shortest path to the list
        path.append(end)
        end = previous[end]
    path.reverse()  # reverse the list to get the correct order of vertices
    print(path)     # print the shortest path
    return path     # return the shortest path

