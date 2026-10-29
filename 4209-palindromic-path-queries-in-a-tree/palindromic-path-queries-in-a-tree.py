class Solution:
    def palindromePath(self, n, edges, s, queries):
        import sys
        sys.setrecursionlimit(300000)

        graph = [[] for i in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        chars = list(s)
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n

        timer = 0

        def dfs(node, par, mask):
            nonlocal timer

            parent[node] = par
            prefix[node] = mask ^ (1 << (ord(chars[node]) - ord('a')))

            tin[node] = timer
            timer += 1

            for nei in graph[node]:
                if nei != par:
                    depth[nei] = depth[node] + 1
                    dfs(nei, node, prefix[node])

            tout[node] = timer - 1

        dfs(0, 0, 0)

        # Binary lifting for LCA
        LOG = n.bit_length()
        up = [[0] * n for i in range(LOG)]

        for i in range(n):
            up[0][i] = parent[i]

        for j in range(1, LOG):
            for i in range(n):
                up[j][i] = up[j - 1][up[j - 1][i]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        # Fenwick Tree supporting range XOR updates
        bit = [0] * (n + 2)

        def add(i, val):
            i += 1

            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def range_xor(l, r, val):
            add(l, val)
            add(r + 1, val)

        def get(i):
            i += 1
            ans = 0

            while i > 0:
                ans ^= bit[i]
                i -= i & -i

            return ans

        def get_prefix(node):
            return prefix[node] ^ get(tin[node])

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old_bit = 1 << (ord(chars[u]) - ord('a'))
                new_bit = 1 << (ord(c) - ord('a'))

                change = old_bit ^ new_bit

                range_xor(tin[u], tout[u], change)

                chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                common = lca(u, v)

                mask = (
                    get_prefix(u)
                    ^ get_prefix(v)
                    ^ (1 << (ord(chars[common]) - ord('a')))
                )

                # At most one odd-frequency character
                if mask & (mask - 1) == 0:
                    answer.append(True)
                else:
                    answer.append(False)

        return answer