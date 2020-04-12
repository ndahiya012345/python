
"Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary"

a=[('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] 
s="A"


def itineary(a,s):
 it=[s]
 b=[]
 for i in range(len(a)):
   for j in range(len(a)):
       if a[j] not in b:
        if(it[len(it)-1]==a[j][0]):
            it.append(a[j][1])
            b.append(a[j])
 print(it)
            
            
itineary(a,s)
           
           