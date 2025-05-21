#Link: https://leetcode.com/problems/open-the-lock/
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        
        q = deque(["0000"])
        visited = set(deadends)
        turns = 0
        while q:
            for _ in range(len(q)):
                lock = q.popleft() 
                if lock == target:
                    return turns
                for child in children(lock):
                    if child not in visited:
                        visited.add(child)
                        q.append(child)
            turns += 1
        return -1

"""
Same as Word Ladder.
For each word, adjacent words will be what happens when we move the lock.
0000 → 0001 If we move front
0000 → 0009 If we move back.

So, for each word, there will be 8 children.
If the child word is in deadend, we cannot go further with it.

Take each character in the range(4).
convert it to int(). Then % 10.

For ex: 0000 → ‘00’ + (int(0) + 1) % 10 + ‘0’

If we reach the end word, return the number of steps.
"""