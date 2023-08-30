def count_each_word(sentence):
    word_count = {}
    words = sentence.split(" ")
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(word_count)


sentence = input("Enter the sentence: ")
words = {}
count = 0
words = sentence.split(" ")
for word in words:
    count += 1
print("Number of words in the given sentence is: ", count)
count_each_word(sentence)
