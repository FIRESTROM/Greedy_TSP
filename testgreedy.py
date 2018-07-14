from cycle import Graph

def greedy_tour(matrix, src): # A matrix of all distances. src is the index shows it's place in matrix

    k = len(matrix)  # dimention of matrix
    constrains = [0 for i in range(k)]  # check how many time that each nodes have been visited (must <= 2)
    order = []
    num_edge = 0
    edges = []
    tour = []
    # Sort first
    for i in range(k):
        for j in range(k):
            if i < j:
                order.append([edgeToindex(i, j, k), matrix[i][j]])
    order = bubble_sort(order)
    # Add edges
    index = 0
    while num_edge < k: # Add at most k edges
        edge = indexToedge(order[index][0], k)
        boolen = check_constrains(constrains, edges, edge, k)
        if boolen:
            constrains[edge[0]] += 1
            constrains[edge[1]] += 1
            edges.append(edge) # Add this edge
            num_edge += 1

        index += 1 # see next edge in each loop


    # Get the tour
    tour.append(src) # Start point
    start = [edges[i][0] for i in range(k)] # All start points
    end = [edges[i][1] for i in range(k)] # All end points
    visited = [0 for i in range(k)]
    if src in start:
        visited[start.index(src)] = 1
        endpoint = end[start.index(src)]
    else:
        visited[end.index(src)] = 1
        endpoint = start[end.index(src)]

    while len(tour) < k: # At most k points except coming back to src
        for i in range(k):
            if visited[i] == 0:
                if endpoint == start[i]:
                    visited[i] = 1
                    new_start = start[i]
                    tour.append(new_start)
                    endpoint = end[i]
                elif endpoint == end[i]:
                    visited[i] = 1
                    new_start = end[i]
                    tour.append(new_start)
                    endpoint = start[i]
    tour.append(src) # Coming back to src

    return tour, src


# Edge[i,j] to a number
def edgeToindex(i, j, k):
    return i * k + j
# A number to edge[i,j]
def indexToedge(x, k):
    return [int(x / k), int(x % k)]
# Sort the order by order[i][1] which are the distances
def bubble_sort(order):
    change = True
    while change:
        change = False
        for i in range(len(order) - 1):
            if order[i][1] > order[i + 1][1]:
                order[i], order[i + 1] = order[i + 1], order[i]
                change = True
    return order

def check_constrains(constrains, edges, edge, k):
    new_constrains = [constrains[i] for i in range(len(constrains))]
    new_constrains[edge[0]] += 1
    new_constrains[edge[1]] += 1
    boolen_has_cycle = True
    boolen_less_two = True
    for i in range(len(new_constrains)):
        if new_constrains[i] > 2:
            boolen_less_two = False
    if sum(new_constrains) == 2 * len(new_constrains) and boolen_less_two:
        return True
    boolen_no_cycle = not check_cycle(edges, edge, k)

    return boolen_less_two and boolen_no_cycle



def check_cycle(edges, edge, k):
    if len(edges) == 0:
        return False
    new_edges = [edges[i] for i in range(len(edges))]
    new_edges.append(edge)
    g = Graph(k)
    for i in range(len(new_edges)):
        g.addEdge(new_edges[i][0], new_edges[i][1])
    return g.have_cycle()
