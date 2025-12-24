class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacitySorted = sorted(capacity,reverse = True)
        
        needed = 0
        while total > 0:
            total -= capacitySorted[needed]
            needed +=1
        return needed