def main():
    word = input("Please enter one word: ")
    position = len(word) - 1
    result_word = ""
    new_word = invertir(word,position,result_word)
    print(new_word)

def invertir(word, position,result_word): 
    if position == 0:
        result_word += word[position]
        return result_word

    result_word += word[position]
    
    return invertir(word, position - 1, result_word)

main()