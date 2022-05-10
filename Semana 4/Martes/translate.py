dictionary = {}
words = input("Please enter word with translations separated by : and ,\n->")
result = words.split(",")
for words in result:
    split_result = words.split(":")
    key = split_result[0].lower()
    value = split_result[1].lower()
    dictionary[key] = value

phrase = input("Please enter a phrase in spanish:")
phrase_words = phrase.split(" ")
for word in phrase_words:
    print(dictionary.get(word.lower(),word.lower()), end=" ")