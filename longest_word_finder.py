# Write down a program to identify the longest word from given user input list.

def get_longest_word(words):
    longest_words = []
    max_length = 0

    for word in words:
        word_length = len(word)
        if word_length > max_length:
            longest_words = [word]
            max_length = word_length
        elif word_length == max_length:
            longest_words.append(word)

    return longest_words,max_length

words_input = input("Enter a list of words separated by spaces: ")
words = words_input.split()

longest_words, max_length = get_longest_word(words)

if longest_words:
    print(f"The longest word(s): {', '.join(longest_words)} with length {max_length}.")
    for word in longest_words:
        print(f"Word: {word}, Length: {len(word)}")
else:
    print("No words were provided.")