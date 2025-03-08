class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        minW = float("infinity")

        for i in range(len(blocks)-k+1):
            Wlen = 0
            Blen = 0
            for char in blocks[i:k+i]:
                if char == 'W':
                    Wlen += 1
                if char == 'B':
                    Blen += 1
            if Blen == k:
                return 0
            else:
                minW = min(Wlen, minW)
        
        return minW



        