#Link: https://leetcode.com/problems/word-ladder/
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        adj_list = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adj_list[pattern].append(word)
        
        q = deque()
        visited = set()

        q.append(beginWord)
        visited.add(beginWord)
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adj_list[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            res += 1
        return 0

"""
Each word string is treated as a node in a graph.

Two nodes are connected (i.e., adjacent) if the strings differ by exactly one character.

To efficiently find such neighbors, we use a pattern-matching trick:

For each word in the `wordList`, we replace one character at a time with a `*`.

This creates patterns that group together all the words that differ at just that one position.

Example:

- For `"AAAB"`, generate:
    - `AAB`, `A*AB`, `AA*B`, `AAA*`
- Any other word with the same pattern is one mutation away.

We start a Breadth-First Search (BFS) from the `beginWord`, treating the count as the level (starting at 0).

At each level, we explore all possible transformation words (neighbors) of the current word using the pattern-based mapping.

As soon as we reach the `endWord`, we return the current count, this is the minimum number of transformation needed.

If the endWord is not in wordList, we return 0.
"""