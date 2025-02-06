#Link: https://leetcode.com/problems/hand-of-straights/
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        minHeap = [num for num in count.keys()]
        heapq.heapify(minHeap)

        while minHeap:
            current_ele = minHeap[0]
            for _ in range(groupSize):
                if not current_ele in count or (count[current_ele] == 0):
                    return False
                count[current_ele] -= 1
                if count[current_ele] == 0:
                    if minHeap[0] == current_ele:
                        heapq.heappop(minHeap)
                    else:
                        return False
                current_ele += 1
        return True

