class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        choices_of_letters = set(''.join(wordList))
        queue = collections.deque()
        queue.append((beginWord, 1))
        while queue:
            word, steps = queue.popleft()
            for i in range(len(beginWord)):
                for chr in choices_of_letters:
                    new_word = word[:i] + chr + word[i+1:]
                    if new_word == endWord:
                        return steps+1
                    if new_word in wordList:
                        queue.append((new_word, steps+1))
                        wordList.remove(new_word)
                        
        return 0
                        