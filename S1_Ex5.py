context = str(input())
sentences = context.split('.')
special_words = []
for i in sentences:
    words = i.split()
    for w in words[1:]:
        if w[0].isupper():
            special_words.append(w.strip(','))

# print(special_words)

words_list = [i.strip(".").strip(',') for i in context.split()]
if "" in words_list:
    words_list.remove("")

special_words_index = []
for i in special_words:
    special_words_index.append(words_list.index(i) + 1)
    words_list[words_list.index(i)] = '-'

result = [f'{j}:{i}' for i,j in zip(special_words, special_words_index)]
if len(result) == 0:
    print("None")
else:
    for i in result:
        print(i)


