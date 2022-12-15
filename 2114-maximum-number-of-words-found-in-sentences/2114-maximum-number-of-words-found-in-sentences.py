import sys
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        word_count = []

        for i in range(len(sentences)):
            space_count = 0
            for j in range(len(sentences[i])):
                if (sentences[i][j]) == " ":
                    space_count += 1
            
            word_count.append(space_count + 1)

        return max(word_count)



