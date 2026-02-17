class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        result = []

        for hour in range(12):
            for minute in range(60):
                hourBits = bin(hour).count("1")
                minuteBits = bin(minute).count("1")

                if hourBits + minuteBits == turnedOn:
                    timeString = f"{hour}:{minute:02d}"
                    result.append(timeString)

        return result        