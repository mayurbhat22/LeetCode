class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj_list = defaultdict(list)
        for u,v,t in meetings:
            adj_list[u].append((v,t))
            adj_list[v].append((u,t))
        
        earliest = [inf] * n
        earliest[0] = 0
        earliest[firstPerson] = 0
        q = deque()
        q.append((firstPerson,0))
        q.append((0,0))
        visited = set()
        visited.add(0)
        visited.add(firstPerson)
        while q:
            person, curr_time = q.popleft()

            for nei, meeting_time in adj_list[person]:
                if curr_time <= meeting_time and earliest[nei] > meeting_time:
                    q.append((nei, meeting_time))
                    earliest[nei] = meeting_time
                    visited.add(nei)
        
        return list(visited)

"""
BFS Would work.
Start by adding 0 and the firstPerson with time 0 in the queue. Since at Time = 0 0 tells the first peerson.
So, Start a BFS.
If the current time is smaller than the meeting time and earliest[nei] > meeting_time, that means before the meeting, the person is getting to know the secret and he can pass it on later. If the current time is greater, that means he got to the know the secret after the meeting time.

But wait, Just using BFS Queue wont be helpful.
Take this example.
`[[0,1,4],[1,3,3],[2,1,2]]`. firstPerson = 2
So, 
The front of the queue `(0, 0)` will be processed first. We will process person `0`, and will add its neighbors to the queue. Hence, `(1, 4)` will be added to the queue.
Next in the queue is `(2, 2)`. We will process person `2`. However, all its neighbors are already processed. Hence, we will not add any new person to the queue.

Next in the queue is `(1, 4)`. We will process person `1`, and due to state information, we will assume that it was informed of the secret at time `t = 4`. Hence, it can inform the secret only to those people it meets after time `t = 4`. However, it meets person `3` at time `t = 3`, hence we will not add person `3` to the queue.

Turns out we are incorrect. Person `1` was informed of the secret at time `t = 2`, because of meeting `[2, 1, 2]`. Hence, `1` can inform the secret to person `3` at time `t = 3`.

We are arriving at an incorrect answer because of the incorrect assumption that we will not revisit a node. Hence, we need to revisit a node if we realize that the earliest time at which a person learns the secret decreases.

So, along with BFS use earliest array to store at what point the person gets to know the secret.
"""