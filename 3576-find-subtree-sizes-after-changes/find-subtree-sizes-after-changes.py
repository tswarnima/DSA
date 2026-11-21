
class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:

        n = len(parent)
        tree = [[] for _ in range(n)]

        for i in range(1, n):
            tree[parent[i]].append(i)

        new_parent = parent[:]
        last = {}
        order = []

        stack = [(0, 0, -1)]

        while stack:
            node, state, prev = stack.pop()

            if state == 0:
                ch = s[node]
                prev = last.get(ch, -1)

                if prev != -1:
                    new_parent[node] = prev

                last[ch] = node
                order.append(node)

                stack.append((node, 1, prev))

                for child in reversed(tree[node]):
                    stack.append((child, 0, -1))

            else:
                ch = s[node]

                if prev == -1:
                    del last[ch]
                else:
                    last[ch] = prev

        ans = [1] * n

        for node in reversed(order):
            if new_parent[node] != -1:
                ans[new_parent[node]] += ans[node]

        return ans
