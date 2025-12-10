import time

start_time = time.time()

with open("inp8.txt") as f:
    lines = f.read().splitlines()

lines = [tuple(map(int, line.split(','))) for line in lines]

def distance(a :tuple, b :tuple):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

distances = {}
for i, line1 in enumerate(lines):
    for j, line2 in enumerate(lines[i:]):
        if line1 != line2:
            distances.update({(line1, line2) : distance(line1, line2)})


sorted_distances = sorted(distances.items() , key=lambda k: k[1])
# print(len(sorted_distances))



# PART 1
# number_of_connections = 1000
# connections :dict[tuple, list]= {}
# for dist in sorted_distances[:number_of_connections]:
#     points = dist[0]
#     p1, p2 = points

#     if connections.get(p1): connections[p1].append(p2)
#     else:   connections[p1] = [p2]
#     if connections.get(p2): connections[p2].append(p1)
#     else:   connections[p2] = [p1]

# # print(connections)
# # print(len(connections))

def map_circuit(visited :dict[tuple, bool], node :tuple, connections :dict[tuple, list]):
    if visited[node]:
        return visited, 0
    
    if not connections.get(node):
        visited[node] = True
        return visited, 1
    
    visited[node] = True
    total_circuit_length = 1
    for neighbour in connections[node]:
        visited, no_of_neighbours = map_circuit(visited, neighbour, connections)
        total_circuit_length += no_of_neighbours
    
    return visited, total_circuit_length

# visited = {line: False for line in lines}
# circuit_lengths = []
# for node in lines:
#     if not visited[node]:
#         visited, no_of_nodes = map_circuit(visited, node, connections)
#         circuit_lengths.append(no_of_nodes)

# circuit_lengths = sorted(circuit_lengths, reverse=True)
# print(circuit_lengths[0] * circuit_lengths[1] * circuit_lengths[2])


# PART 2
for dist_index in range(len(lines)-1, len(distances)):

    connections :dict[tuple, list]= {}
    for dist in sorted_distances[:dist_index]:
        points = dist[0]
        p1, p2 = points

        if connections.get(p1): connections[p1].append(p2)
        else:   connections[p1] = [p2]
        if connections.get(p2): connections[p2].append(p1)
        else:   connections[p2] = [p1]
    
    visited = {line: False for line in lines}
    circuit_lengths = []
    for node in lines:
        if not visited[node]:
            visited, no_of_nodes = map_circuit(visited, node, connections)
            circuit_lengths.append(no_of_nodes)

    if max(circuit_lengths) == len(lines):
        # print(connections)
        l = next(reversed(sorted_distances[:dist_index]))[0]
        print(l)
        print(f"the final link is {l[0]} : {l[1]}")
        print(f"Mul value is {l[0][0] * l[1][0]}")
        break



# 255456327 is too low

print(f"----- {time.time() - start_time} -----")