class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for i in range(n+1)]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        q = {1}
        excl = set()
        mem = set()

        dist = 0

        while n not in q:
            level = set()

            for el in mem:
                if el not in excl:
                    excl.add(el)

            for node in q:
                for con in graph[node]:
                    if con not in excl and con not in level:
                        level.add(con)

            mem = q
            q = level
            dist += 1 

        level = set()

        for node in q:
            for con in graph[node]:
                if con not in level:
                    level.add(con)

        one_longer = False
        if n in level:
            one_longer = True

        if one_longer:
            dist += 1
        else:
            dist += 2

        out = 0

        for i in range(dist):
            if (out // change) % 2 == 0:
                out += time
            else:
                out = (out//change + 1) * change + time

        return out



        