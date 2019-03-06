import random
import math
import time
#----------
def pairing (alph,nodes) : # pair all node
    
    for i in range(len(alph)):
        
        for j in range(len(alph)):
            if j > i:
                pairsSet.append([alph[i],alph[j]])
                #pairs.append((alph[i],alph[j]))


    edges = math.ceil(len(pairsSet)/3 - round(len(pairsSet)*random.uniform(0.0,0.1))) # %
    

    for num in range(edges):
        choice = random.choice(pairsSet)
        graphSet.append(choice)
        pairsSet.remove(choice)

    print("Nodes = " + str(alph))
    print("Total nodes: "+ str(nodes))
    print("Total edges: "+str(edges))
    print("Graph:")
    print(graphSet)
    print("----------")
    exhaustive(graphSet,alph)
    greedy(graphSet,alph)
#----------
def greedy(graph,nodes):
    print("-----Greedy Search-----")
    start_time = time.time() #start time
    nodeCount = {} # dict
    subsubnode = [] # temp for find higher to lower
    subnode = [] # record all nodes random order
    hightolow = [] # record all nodes in edges from higher to lower
    candidate = []
    #marker = []
    for sets in range(len(graph)): # count nodes in edges
        for eachnode in range(len(graph[sets])):
            #print(graph[sets][eachnode])
            if graph[sets][eachnode] not in nodeCount:
                nodeCount[graph[sets][eachnode]]=1
            else:
                nodeCount[graph[sets][eachnode]]=nodeCount[graph[sets][eachnode]]+1
            #if graph[sets][eachnode] not in subsubnode:
                #subsubnode.append(graph[sets][eachnode])
    #print(nodeCount)
    subnode= sorted(nodeCount, key=nodeCount.get, reverse=True)
    hightolow= sorted(nodeCount, key=nodeCount.get, reverse=True)
    #print(subnode)
    #print(hightolow)
    #print("subsubonde: "+str(subsubnode))
    #print(nodeCount.keys())
    #while len(subsubnode)>0:
        #largest= 0
        #temp= subsubnode[0]
        #print(temp)
        #for sub in range(len(subsubnode)): # find highest node in temp subsubnode
            #print(" "+str(subsubnode[sub]))
            #if nodeCount[subsubnode[sub]] > largest:
                #largest = nodeCount[subsubnode[sub]]
                #temp = subsubnode[sub]
        #subnode.append(temp)
        #hightolow.append(temp)
        #subsubnode.remove(temp)
    #print("subnode"+str(subnode)) # highest to lowerest
    if len(subnode) != len(nodes): #missing node direct end
        elapsed_time = time.time() - start_time # end time
        print("")
        print("No hamiltonian path found")
        #print("Node missing: "+str(subnode))
        print("")
        print("Greedy search time used:")
        print(elapsed_time)
        print("")
    else:
        root =""
        marker = []
        # first greedy
        for node in range(len(subnode)):
            #print(node)
            if len(marker) == 0:
                marker.append(subnode[node])
                root = subnode[node]
            else:
                for sets in range(len(graph)):
                    #print(graph[sets])
                    if graph[sets][0] == root and graph[sets][1] == subnode[node] not in marker:
                        marker.append(subnode[node])
                        root = subnode[node]
                    if graph[sets][1] == root and graph[sets][0] == subnode[node] not in marker:
                        marker.append(subnode[node])
                        root = subnode[node]
        #print("marker: "+str(marker))
        if len(marker) == len(nodes):
            elapsed_time = time.time() - start_time # end time
            print("")
            print("Hamiltonian path found")
            #print("Best candidate:")
            #print(marker)
            print("")
            print("Greedy search time used:")
            print(elapsed_time)
            print("")
        else:
            # improve of first greedy
            #print("")
            #print(marker)
            root = marker[0]
            #print(root)
#            for i in range(len(graph)):
#                #print(graph[i])
#                if root == graph[i][0] and graph[i][1] not in marker:
#                    marker.insert(0,graph[i][1])
#                    #print(marker)
#                    root = graph[i][1]
#                    #print(root)
#                if root == graph[i][1] and graph[i][0] not in marker:
#                    marker.insert(0,graph[i][0])
#                    #print(marker)
#                    root = graph[i][0]
#                    #print(root)
#                if len(marker) == len(nodes):
#                    break
            #print(marker)
            
#            if len(marker) == len(nodes):
#                elapsed_time = time.time() - start_time # end time
#                print("")
#                print("Hamiltonian path found")
#                print("")
#                print(marker)
#                print("")
#                print("Greedy search time used:")
#                print(elapsed_time)
#                print("")
#            else:
            x = 0
            while x <= 50: #tabu search
                marker = []
                root = ""
                #print("before")
                #print(subnode)
                #print(hightolow)
                #---------- random change order for nodes
                tempindex = random.randint(0,len(subnode)-1)
                tempindex2 = random.randint(0,len(subnode)-1)
                tempnode = subnode[tempindex]
                subnode[tempindex] = subnode[tempindex2]
                subnode[tempindex2] = tempnode
                #----------
                edgeindex = random.randint(0,len(graph)-1)
                edgeindex2 = random.randint(0,len(graph)-1)
                tempedge = graph[edgeindex]
                graph[edgeindex] = graph[edgeindex2]
                graph[edgeindex2] = tempedge
                #----------
                #print("after")
                #print(subnode)
                x =x+ 1
                for node in range(len(subnode)):
                    #print(node)
                    if len(marker) == 0:
                        marker.append(subnode[node])
                        root = subnode[node]
                    else:
                        for sets in range(len(graph)):
                            gethigher = random.randint(0,1)
                            #print(graph[sets])
                            if gethigher == 0: #get random
                                if graph[sets][0] == root and graph[sets][1] == subnode[node] not in marker:
                                    marker.append(subnode[node])
                                    root = subnode[node]
                                if graph[sets][1] == root and graph[sets][0] == subnode[node] not in marker:
                                    marker.append(subnode[node])
                                    root = subnode[node]
                            if gethigher == 1: # get higher
                                subindex = subnode.index(root)
                                canbreak = False
                                for node2 in range(len(hightolow)):
                                    if hightolow[node2] not in marker:
                                        for sets2 in range(len(graph)):
                                            if graph[sets2][0] == root and graph[sets2][1] == hightolow[node2]:
                                                marker.append(hightolow[node2])
                                                root = hightolow[node2]
                                                #print("add"+str(root))
                                                canbreak = True
                                                break
                                            if graph[sets2][1] == root and graph[sets2][0] == hightolow[node2]:
                                                marker.append(hightolow[node2])
                                                root = hightolow[node2]
                                                #print("add"+str(root))
                                                canbreak = True
                                                break
                                                    
                                    if canbreak == True:
                                        break
                                        
                #print(marker)
                if len(marker) > len(candidate):
                    candidate = marker
                    #break
                if len(marker) == len(nodes):
                    break
            if len(candidate) == len(nodes):
                elapsed_time = time.time() - start_time # end time
                print("")
                print("Hamiltonian path found")
                #print("Best candidate:")
                #print(candidate)
                print("")
                print("Greedy search time used:")
                print(elapsed_time)
                print("")
            else:
                elapsed_time = time.time() - start_time # end time
                print("")
                print("No hamiltonian path found")
                #print("Best candidate:")
                #print(candidate)
                print("")
                print("Greedy search time used:")
                print(elapsed_time)
                print("")
                
#----------
def exhaustive(graph,nodes):
    print("-----Exhaustive Search-----")
    start_time = time.time() # start time
    found = False
    pathfound = []
    for node in range(len(nodes)): #start with each node and each node one path only
        marker = [] # record path
        block = {} #dict record all dead end 
        marker.append(nodes[node])
        #print("start form: "+nodes[node])
        #print("marker: "+str(marker))
        root = nodes[node]
        #print("root: "+str(root))
        looping = True
        while looping: # loop all route with root if dead end go back one layer
            looping = False
            for sets in range(len(graph)): # loop edges to see path
                if graph[sets][0] == root and graph[sets][1] not in marker:
                    able = True
                    paths = str(marker).replace("[","").replace("]","").replace(",","|").replace("'","").replace(" ","")
                    if paths in block:
                        if graph[sets][1] in block[paths]:
                            able = False
                    if able == True:
                        marker.append(graph[sets][1])
                        #print("add "+graph[sets][1]+" to marker: "+str(marker))
                        root = graph[sets][1]
                        #print("root: "+str(root))
                        looping = True
                if graph[sets][1] == root and graph[sets][0] not in marker:
                    able = True
                    paths = str(marker).replace("[","").replace("]","").replace(",","|").replace("'","").replace(" ","")
                    if paths in block:
                        if graph[sets][0] in block[paths]:
                            able = False
                    if able == True:
                        marker.append(graph[sets][0])
                        #print("add "+graph[sets][0]+" to marker: "+str(marker))
                        root = graph[sets][0]
                        #print("root: "+str(root))
                        looping = True
            if looping == False:
                if len(marker) < len(nodes) and len(marker) > 1:
                    root = marker[len(marker)-2]
                    #print("root: "+str(root))
                    temp = marker[-1]
                    marker.pop()
                    keys = str(marker).replace("[","").replace("]","").replace(",","|").replace("'","").replace(" ","")
                    ##print(keys)
                    if keys not in block:
                        block[keys] = [temp]
                    else:
                        if temp not in block[keys]:
                            block[keys].append(temp)
                    #print("block"+str(block))
                    #print("rm "+temp+" from marker: "+str(marker))
                    looping = True
            
                
        #print("marker: "+str(marker))
        if len(marker) == len(nodes):
            found = True
            pathfound.append(marker)
            break
        #print("")
    if found == True:
        print("")
        print("Hamiltonian path found")
        print("")
        #print(pathfound)
        print("")
        #for eachpath in range(len(pathfound)):
            #print(pathfound[eachpath])
    else:
        print("")
        print("No hamiltonian path found")
        print("")
    elapsed_time = time.time() - start_time
    print("Exhaustive search time used:")
    print(elapsed_time)
    print("")
#----------
while True:
    # Declaration
    graphSet = [] # random edges
    pairsSet = [] # full edges
    #pairs = [] # later for solve
    alph = [] # nodes
    switch = True
    
    #user input
    while switch:
        nodes = input("How many nodes do you want? (must more than 1)")
        if nodes.isdigit() == True:
            nodes = int(nodes)
            if nodes <= 1:
                #if nodes<=26:
                    #switch = False
                #else :
                    #print("Nodes mush be less than 26")
                print("Nodes mush be more than 1")
            else:
                switch = False
        else :
            print("Please enter in 'number'")
    #----------
    # add nodes to alph
    for x in range(nodes):
        alph.append(str(x))
    #----------
    pairing(alph,nodes)
