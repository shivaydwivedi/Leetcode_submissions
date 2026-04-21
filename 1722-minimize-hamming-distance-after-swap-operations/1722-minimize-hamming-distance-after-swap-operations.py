from collections import defaultdict


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        n = len(source)
        parent = list(range(n))

    # DSU Find function
        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]

    # DSU Union function
        for i, j in allowedSwaps:
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j

    # Group indices by their root parent
        components = defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)

        hamming_distance = 0
        for root in components:
            indices = components[root]
        
        # Count frequencies of numbers in this component
            count = defaultdict(int)
            for i in indices:
                count[source[i]] += 1
            
        # Try to match with target
            match = 0
            for i in indices:
                if count[target[i]] > 0:
                    match += 1
                    count[target[i]] -= 1
        
        # Any index in this component that didn't match adds to distance
            hamming_distance += (len(indices) - match)

        return hamming_distance