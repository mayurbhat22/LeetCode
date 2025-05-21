#Link: https://leetcode.com/problems/minimum-genetic-mutation/
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank.append(startGene)
        adj_list = defaultdict(list)
        for word in bank:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adj_list[pattern].append(word)
        
        q = deque([startGene])
        visited = set([startGene])
        res = 0
        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endGene:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adj_list[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            res += 1
        
        return -1
    
"""
Each gene string is treated as a node in a graph.

Two nodes are connected (i.e., adjacent) if their gene strings differ by exactly one character.

To efficiently find such neighbors, we use a pattern-matching trick:

For each word in the gene bank, we replace one character at a time with a `*`.

This creates patterns that group together all genes that differ at just that one position.

Example:

- For `"AAAB"`, generate:
    - `AAB`, `A*AB`, `AA*B`, `AAA*`
- Any other gene with the same pattern is one mutation away.

We start a Breadth-First Search (BFS) from the `startGene`, treating the mutation count as the level (starting at 0).

At each level, we explore all possible mutations (neighbors) of the current gene using the pattern-based mapping.

As soon as we reach the `endGene`, we return the current mutation count, this is the minimum number of mutations needed.

If we exhaust all possibilities without reaching `endGene`, we return `-1`.
"""