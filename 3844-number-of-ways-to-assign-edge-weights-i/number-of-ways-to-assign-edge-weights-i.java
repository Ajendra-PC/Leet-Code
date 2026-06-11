class Solution {
    static final long MOD = 1000000007L;

    public int assignEdgeWeights(int[][] edges) {
        int n = edges.length + 1;

        List<Integer>[] graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{1, 0});

        boolean[] vis = new boolean[n + 1];
        vis[1] = true;

        int maxDepth = 0;

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int node = curr[0];
            int depth = curr[1];

            maxDepth = Math.max(maxDepth, depth);

            for (int nei : graph[node]) {
                if (!vis[nei]) {
                    vis[nei] = true;
                    q.offer(new int[]{nei, depth + 1});
                }
            }
        }




        return (int) modPow(2, maxDepth - 1, MOD);
    }

    private long modPow(long base, long exp, long mod) {
        long ans = 1;

        while (exp > 0) {
            if ((exp & 1) == 1) {
                ans = (ans * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }

        return ans;
    }
}