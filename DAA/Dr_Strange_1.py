import heapq

def shortest_path(n, m, portals, demon_times):
    # Create a list to store the shortest travel time to each universe
    shortest_time = [float('inf')] * (n + 1)
    # Initialize the starting universe with time 0
    shortest_time[1] = 0

    # Create a priority queue to store the universes to be visited O(log N)
    pq = [(0, 1)]  # (time, universe)
# n
    while pq:
        current_time, current_universe = heapq.heappop(pq)

        # Check if we have reached the destination universe
        if current_universe == n:
            return current_time

        # Check if the current time is safe to travel in the current universe
        safe_time_index = 0
        while safe_time_index < len(demon_times[current_universe]) and demon_times[current_universe][safe_time_index] <= current_time:
            safe_time_index += 1

        # Iterate through the portals connected to the current universe O(log N)
        for portal in portals[current_universe]:
            next_universe, travel_time = portal

            next_time = current_time + travel_time
            if safe_time_index < len(demon_times[current_universe]) and demon_times[current_universe][safe_time_index] <= next_time:
                next_time = demon_times[current_universe][safe_time_index] + 1
                safe_time_index += 1

            if next_time < shortest_time[next_universe]:
                shortest_time[next_universe] = next_time
                heapq.heappush(pq, (next_time, next_universe))

    return -1

n, m = map(int, input().split())
portals = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    portals[a].append((b, c))
    portals[b].append((a, c))
demon_times = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    demon_times[i] = list(map(int, input().split()))

# Calculate the shortest travel time O(N log N)
result = shortest_path(n, m, portals, demon_times)
print("Output : ", result)
