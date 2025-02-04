#Link: https://leetcode.com/problems/top-k-frequent-words/
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans = []
        count = Counter(words)
        maxHeap = []
        for word, freq in count.items():
            heapq.heappush(maxHeap, (-freq, word))
        
        for _ in range(0, k):
            freq, word = heapq.heappop(maxHeap)
            ans.append(word)
            
        return ans
