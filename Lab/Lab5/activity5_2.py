sentence = input("Enter a sentence: ")

sentence = sentence.lower()

words = sentence.split()

word_counts = {}

for word in words:

    word = word.strip('.,!?"')

    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("\nWord Frequency:")
print(word_counts)