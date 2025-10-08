class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        rev1 = version1.split(".")
        rev2 = version2.split(".")

        len1, len2 = len(rev1), len(rev2)
        maxLen = max(len1, len2)

        for i in range(maxLen):
            r1 = int(rev1[i]) if i < len1 else 0
            r2 = int(rev2[i]) if i < len2 else 0

            if r1 < r2:
                return -1
            elif r1>r2:
                return 1
        return 0
        