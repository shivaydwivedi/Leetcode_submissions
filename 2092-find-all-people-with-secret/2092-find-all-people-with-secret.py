class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        from collections import defaultdict

        meetings.sort(key=lambda x: x[2])
        knows = set([0, firstPerson])

        i = 0
        m = len(meetings)

        while i < m:
            time = meetings[i][2]
            temp = []
            people = set()

            # collect all meetings at this time
            while i < m and meetings[i][2] == time:
                x, y, _ = meetings[i]
                temp.append((x, y))
                people.add(x)
                people.add(y)
                i += 1

            # union-find only for people at this time
            parent = {p: p for p in people}

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            def union(x, y):
                px, py = find(x), find(y)
                if px != py:
                    parent[py] = px

            for x, y in temp:
                union(x, y)

            # group by connected component
            groups = defaultdict(list)
            for p in people:
                groups[find(p)].append(p)

            # if any member knows the secret, whole group learns it
            for group in groups.values():
                if any(p in knows for p in group):
                    knows.update(group)

        return list(knows)
