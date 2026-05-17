from collections import deque

class Solution:
    def canReach(self, arr, start):
        q = deque([start])
        visited = set([start])

        while q:
            i = q.popleft()

            if arr[i] == 0:
                return True

            for nxt in (i + arr[i], i - arr[i]):
                if 0 <= nxt < len(arr) and nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return False