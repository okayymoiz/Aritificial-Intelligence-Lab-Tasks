# ------ QUESTION 1 ----
print("Question no 1 : A*")
import heapq
def astar(graph,h,start,goal):
 pq=[(h[start],0,start,[start])]; best={start:0}
 expanded=[]
 while pq:
  f,g,node,path=heapq.heappop(pq)
  if node==goal: return g,path,expanded
  if g!=best[node]: continue
  expanded.append(node)
  for nxt,w in graph.get(node,[]):
   ng=g+w
   if ng < best.get(nxt,float("inf")):
    best[nxt]=ng
    heapq.heappush(pq,(ng+h[nxt],ng,nxt,path+[nxt]))
g={"S":[("A",1),("B",4)],"A":[("C",2)],"B":[("G",5)],"C":[("G",3)],"G":[]}
h={"S":5,"A":4,"B":4,"C":2,"G":0}
cost,path,expanded=astar(g,h,"S","G")
print("Path: ",path)
print("Total Cost: ",cost)
print("Expanded Node: ",expanded)
print("Expanded Node Count: ",len(expanded))

# ------ QUESTION 2 : UCS PART ----
print("\n Question no 2 : A* and UCS")
import heapq
def UCS(graph,h,start,goal):
 pq=[(h[start],0,start,[start])]; best={start:0}
 expanded=[]
 while pq:
  f,g,node,path=heapq.heappop(pq)
  if node==goal: return g,path,expanded
  if g!=best[node]: continue
  expanded.append(node)
  for nxt,w in graph.get(node,[]):
   ng=g+w
   if ng < best.get(nxt,float("inf")):
    best[nxt]=ng
    heapq.heappush(pq,(ng+h[nxt],ng,nxt,path+[nxt]))
g={"S":[("A",1),("B",4)],"A":[("C",2)],"B":[("G",5)],"C":[("G",3)],"G":[]}
h={"S":0,"A":0,"B":0,"C":0,"G":0}
cost,path,expanded=UCS(g,h,"S","G")
print("Path: ",path)
print("Total Cost: ",cost)
print("Expanded Node: ",expanded)
print("Expanded Node Count: ",len(expanded))

# ------ QUESTION 3 ----
print("\n Question no 3 : Overestimated Heuristic C(h) = 10")
import heapq
def astar(graph,h,start,goal):
 pq=[(h[start],0,start,[start])]; best={start:0}
 expanded=[]
 while pq:
  f,g,node,path=heapq.heappop(pq)
  if node==goal: return g,path,expanded
  if g!=best[node]: continue
  expanded.append(node)
  for nxt,w in graph.get(node,[]):
   ng=g+w
   if ng < best.get(nxt,float("inf")):
    best[nxt]=ng
    heapq.heappush(pq,(ng+h[nxt],ng,nxt,path+[nxt]))
g={"S":[("A",1),("B",4)],"A":[("C",2)],"B":[("G",5)],"C":[("G",3)],"G":[]}
h={"S":5,"A":4,"B":4,"C":10,"G":0}
cost,path,expanded=astar(g,h,"S","G")
print("Path: ",path)
print("Total Cost: ",cost)
print("Expanded Node: ",expanded)
print("Expanded Node Count: ",len(expanded))