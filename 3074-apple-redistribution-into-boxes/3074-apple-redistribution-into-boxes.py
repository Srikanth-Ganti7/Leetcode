class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:

        totalSum = sum(apple)
        capacity.sort(reverse = True)
        count = 0

        for cap in capacity:
            totalSum -= cap
            count += 1
            if totalSum <=0:
                return count

        

        