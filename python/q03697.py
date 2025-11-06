"""
3607. Power Grid Maintenance

You are given an integer `c` representing `c` power stations, each with a
unique identifier `id` from `1` to `c` (1‑based indexing).

These stations are interconnected via `n` bidirectional cables, represented by
a 2D array `connections`, where each element `connections[i] = [ui, vi]`
indicates a connection between station `ui` and station `vi`. Stations that
are directly or indirectly connected form a power grid.

Initially, all stations are online (operational).

You are also given a 2D array `queries`, where each query is one of the
following two types:
    `[1, x]`: A maintenance check is requested for station `x`. If station `x`
        is online, it resolves the check by itself. If station `x` is offline,
        the check is resolved by the operational station with the smallest
        `id` in the same power grid as `x`. If no operational station exists
        in that grid, return `-1`.
    `[2, x]`: Station `x` goes offline (i.e., it becomes non-operational).

Return an array of integers representing the results of each query of type
`[1, x]` in the order they appear.

Note: The power grid preserves its structure; an offline (non‑operational)
node remains part of its grid and taking it offline does not alter
connectivity.
"""

class Solution:
    def processQueries(self,
            c: int,
            connections: List[List[int]],
            queries: List[List[int]]
        ) -> List[int]:
        """
        TOO SLOW
        Pretty sure this is a 'union-find' problem...
        Need to keep track of minimum id in each group...
        """
        # Construct groups of stations
        groups = [{i: True} for i in range(1, c + 1)]
        for p, q in connections:
            # Locate group containing `p`
            i = 0
            for i in range(len(groups)):
                if p in groups[i]: break
            
            # If `q` is already in same group as `p`, do nothing
            if q in groups[i]:
                continue
            
            # If not, find group containing `q`...
            j = 0
            for j in range(len(groups)):
                if q in groups[j]: break
            
            # Take all elements from later group and merge them into earlier group
            if i < j:
                groups[i].update(groups[j])
                del groups[j]
            else:
                groups[j].update(groups[i])
                del groups[i]
        
        results = []
        for op, station in queries:
            # Locate group containing `station`
            i = 0
            for i in range(len(groups)):
                if station in groups[i]: break
            
            # Peform specified operation
            if op == 1:
                if groups[i][station]:
                    results.append(station)
                    continue
            
                online_stations = [n for n, online in groups[i].items() if online]
                if online_stations:
                    results.append(min(online_stations))
                else:
                    results.append(-1)
            else:  # op == 2
                groups[i][station] = False
        
        return results

    def processQueries(self,
            c: int,
            connections: List[List[int]],
            queries: List[List[int]]
        ) -> List[int]:
        """INCORRECT"""
        # Construct power_grids of stations
        power_grids = [{i: True} for i in range(1, c + 1)]  # array of sets of stations
        grid = {i : i - 1 for i in range(1, c + 1)}  # lookup table for which grid a station is part of
        for p, q in connections:
            # Locate group containing `p`
            i = grid[p]
            
            # If `q` is already in same group as `p`, do nothing
            if grid[q] == i:
                continue
            
            # If not, find group containing `q`...
            j = grid[p]
            
            # Take all elements from later group and merge them into earlier group
            if i < j:
                for station, online in power_grids[j].items():
                    power_grids[i][station] = online
                    grid[station] = i
                del power_grids[j]
            else:
                for station, online in power_grids[i].items():
                    power_grids[j][station] = online
                    grid[station] = j
                del power_grids[i]
        
        results = []
        for op, station in queries:
            # Locate group containing `station`
            i = grid[station]
            
            # Peform specified operation
            if op == 1:
                if power_grids[i][station]:
                    results.append(station)
                    continue
            
                online_stations = [n for n, online in power_grids[i].items() if online]
                if online_stations:
                    results.append(min(online_stations))
                else:
                    results.append(-1)
            else:  # op == 2
                power_grids[i][station] = False
        
        return results