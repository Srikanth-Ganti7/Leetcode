class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")
        
        words = paragraph.lower().split()

        hashMap = {}

        for word in words:
            if word not in banned:
                hashMap[word] = 1 + hashMap.get(word, 0)

        maxVal = 0
        maxWord = ""
        for keys, values in hashMap.items():
            if values > maxVal:
                maxVal = values
                maxWord = keys
        
        return maxWord

        