class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        # Count initial inversions
        inversionsCount = sum(nums[i + 1] < nums[i] for i in range(n - 1))

        # Linked-list simulation
        nextIndices = [i + 1 for i in range(n)]
        prevIndices = [i - 1 for i in range(n)]

        # Store (pairSum, leftIndex)
        pairSums = SortedList(
            (a + b, i) for i, (a, b) in enumerate(itertools.pairwise(nums))
        )

        while inversionsCount > 0:
            ans += 1

            pairSum, currIndex = pairSums.pop(0)
            nextIndex = nextIndices[currIndex]
            prevIndex = prevIndices[currIndex]

            # ---- Handle left neighbor ----
            if prevIndex >= 0:
                oldPairSum = nums[prevIndex] + nums[currIndex]
                newPairSum = nums[prevIndex] + pairSum

                pairSums.remove((oldPairSum, prevIndex))
                pairSums.add((newPairSum, prevIndex))

                if nums[prevIndex] > nums[currIndex]:
                    inversionsCount -= 1
                if nums[prevIndex] > pairSum:
                    inversionsCount += 1

            # ---- Handle current → next inversion ----
            if nextIndex < n and nums[nextIndex] < nums[currIndex]:
                inversionsCount -= 1

            # ---- Handle right neighbor ----
            nextNextIndex = nextIndices[nextIndex] if nextIndex < n else n
            if nextNextIndex < n:
                oldPairSum = nums[nextIndex] + nums[nextNextIndex]
                newPairSum = pairSum + nums[nextNextIndex]

                pairSums.remove((oldPairSum, nextIndex))
                pairSums.add((newPairSum, currIndex))

                if nums[nextNextIndex] < nums[nextIndex]:
                    inversionsCount -= 1
                if nums[nextNextIndex] < pairSum:
                    inversionsCount += 1

                prevIndices[nextNextIndex] = currIndex

            # ---- Update links and value ----
            nextIndices[currIndex] = nextNextIndex
            nums[currIndex] = pairSum

        return ans