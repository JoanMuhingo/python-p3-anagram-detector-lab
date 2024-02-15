# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        word_sorted = sorted(self.word)
        anagrams = []

        for word in word_list:
            if word.lower() != self.word and sorted(word.lower()) == word_sorted:
                anagrams.append(word)

        return anagrams
