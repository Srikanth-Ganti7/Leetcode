class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        Hmap = {}

        l = 0
        count = 0
        for r in range(len(s)):
            Hmap[s[r]] = 1 + Hmap.get(s[r], 0)

            while len(Hmap) == 3:
                # count += 1
                count += len(s) - r

                Hmap[s[l]] -= 1

                if Hmap[s[l]] == 0:
                    del Hmap[s[l]]
                l += 1
        return count

            



        