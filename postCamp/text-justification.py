class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, currLine, currLen = [], [], 0

        for word in words:
            if currLen + len(word) + len(currLine) > maxWidth:
                for i in range(maxWidth - currLen):
                    currLine[i % (len(currLine) - 1 or 1)] += ' '

                result.append(''.join(currLine))
                currLine, currLen = [], 0

            currLine += [word]
            currLen += len(word)

        result.append(' '.join(currLine).ljust(maxWidth))

        return result
            