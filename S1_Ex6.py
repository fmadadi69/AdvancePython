number_of_entries = int(input())
dictionary = dict()


def get_dictionary_input(num):
    for i in range(num):
        entry = str(input())
        entry = entry.split()
        for j in range(len(entry) - 1):
            dictionary[entry[j + 1]] = entry[0]
    return dictionary


get_dictionary_input(number_of_entries)

sentence = str(input())
words_list = sentence.split()


def translate(words):
    translated_words = []
    for w in words:
        if w in dictionary:
            translated_words.append(dictionary[w])
        else:
            translated_words.append(w)
    return ' '.join(translated_words)


print(translate(words_list))
