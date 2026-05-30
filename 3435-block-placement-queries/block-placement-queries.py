from sortedcontainers import SortedList

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1);

    def update(self, i, val):
        while i < len(self.bit):
            self.bit[i] = max(self.bit[i], val)
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res = max(res, self.bit[i])
            i -= i & -i
        return res


class Solution:
    def getResults(self, queries):
        LIMIT = min(50000, len(queries) * 3)

        obstacles = SortedList([0, LIMIT])

        # Insert all obstacles first
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        bit = Fenwick(LIMIT + 2)

        # Initialize gaps
        for i in range(len(obstacles) - 1):
            a = obstacles[i]
            b = obstacles[i + 1]
            bit.update(b, b - a)

        ans = []

        # Process backwards
        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]

                idx = obstacles.index(x)
                prev_pos = obstacles[idx - 1]
                next_pos = obstacles[idx + 1]

                obstacles.remove(x)

                # merged interval
                bit.update(next_pos, next_pos - prev_pos)

            else:
                _, x, sz = q

                idx = obstacles.bisect_right(x)
                prev_pos = obstacles[idx - 1]

                ok = (
                    bit.query(prev_pos) >= sz or
                    x - prev_pos >= sz
                )

                ans.append(ok)

        return ans[::-1]