class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):                
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            else:
                i += 1
        return self.text


remover = VowelRemover("aeiou")
print(remover.remove_vowels())


"""
line 8 - while i is less than the length of text, the loop will run:
    -* i is assigned to a count of 0
    -* len of text starts at 5

line 11 is adding and assigning 1 to i, each time.

however 'i' steadily increases, and the length of text progressively gets  smaller with each run of the loop
    -* len starts at 5, whilst i is 0
    -* len becomes at 4, whilst i is 1
    -* len becomes 3 whilst i is 2
    -* len becomes 2 whilst i is 3   -- This is where i becomes more than len of text, and the loop stops

This leaves us with a string of 'eo' instead of an empty string

each time i += 1 (line 12) happened it moved the index of the next letter,
and we were left with 'eo'

We want the index of the vowel to always be the first index (0), so we are iterating thru
each vowel in the string

* code was missing an 'else:' conditional, meaning if string is not a vowel, then increment i by +1

"""