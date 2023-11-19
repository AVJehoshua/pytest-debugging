class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}                        
        most_common = None
        most_common_count = 0
        for char in self.text:
            if not char.isalpha():
                continue
            counter[char] = counter.get(char, 0) + 1
            if counter[char] > most_common_count:
                most_common = char
                most_common_count = counter[char]    # this line is suspicious - stores both 'd' and 'i' history of being most common letter
                #print(most_common_count)
                #print(counter[char])
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]

#Actual output:
# [3, "D"]

#New output:  most_common_count is storing d's most common count, as well as i's most common count - we only want i
# [3, 'i']

# Solution output: line 15 was suspicious, += counter[char] was storing both d and i's most common letter occurance, changing this to = makes it just 'i's (mco)
# [2, 'i']

"""
Notes on above code -

line 6 - assigned an empty dict to variable 'counter'

line 7 - set the value of the most_common variable to None (meaning) no common letters atm

line 8 - set most_common_count (letter occurances) to 1 - this is suspicious to me as it should start at 0?

line 9 - begining for for loop to iterate through text

line 10 - setting if conditional, if not char in text isalpha(meaning is it in alphabet)

line 11 - if char is in alphabet, continue on

line 12 - counter[char] represents key in dictionary, assigned it a value of counter.get(char, 0) + 1
    -* in first iteration, counter[char] = 'D', counter.get(char,0) +1 = 1 : this gives the key(letter) d an occurance value of 1

line 13 - setting if conditional if counter[char] is greater than most_common_count
    -* Now counter[char] is 1, and if it is more than most_common_count, assign the char ('D') to the most common variable (originally none)

line 14 - add and assign counter[char] to most common count
    -* add 1 to the total most common letter count - not specific to 'd', increases later with 'i'

line 15 - return a list of the occurance of most common letter, and the most common letter


"""