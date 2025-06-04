# interview question
# This is a common interview question. reversing the sentence

from pprint import pprint
sentence = "This is a common interview question."
words = sentence.split()
words.reverse()
reversed_sentence = ' '.join(words)
print(reversed_sentence)
print("\n")

# Count the most frequent character in a string
# This is a common interview question. counting the most frequent character in a string

sentence = "This is a common interview question."
char_count = {}
for char in sentence:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
pprint(char_count, width=1)
char_frequency_sorted = sorted(
    char_count.items(),
    key=lambda x: x[1],
    reverse=True)
print(char_frequency_sorted[0])


# Find the longest word in a sentence
