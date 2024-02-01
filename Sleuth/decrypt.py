a_ascii = ord("a")
alphabet_size = 26

message_dic = {"Ncevy": 13, "gpvsui": 25, "ugflgkg": -18, "wjmmf": -1}

word_list = ["Ncevy", "gpvsui", "ugflgkg", "wjmmf"]
shift_list = [13, 25, -18, -1]


def lasso_letter(letter, shift_amount):
    # lower_letter = letter.lower()
    # ord_letter = ord(lower_letter)
    # new_ord = a_ascii + (((ord_letter - a_ascii) + shift_amount) % alphabet_size)
    # new_letter = chr(new_ord)
    # return new_letter

    # return chr(ord(letter.lower()) + shift_amount)

    lower_letter = letter.lower()
    new_letter = chr(
        a_ascii + (((ord(lower_letter) - a_ascii) + shift_amount) % alphabet_size)
    )
    if lower_letter == letter:
        return new_letter
    else:
        return new_letter.upper()


def lasso_word(word, shift_amount):
    new_word = ""
    for letter in word:
        new_letter = lasso_letter(letter, shift_amount)
        new_word += new_letter

    return new_word


def lasso_sentence_dic(message):
    new_sentence = ""
    for word in message:
        # print(word)
        shift_amount = message[word]
        new_sentence += lasso_word(word, shift_amount) + " "
    return new_sentence


def lasso_sentence_list(word_list, shift_list):
    new_sentence = ""
    for i in range(len(word_list)):
        word = word_list[i]
        shift_amount = shift_list[i]
        new_sentence += lasso_word(word, shift_amount) + " "
    return new_sentence


# print(lasso_letter("a", 5))
# print(lasso_letter("N", 13))
# print(lasso_letter("Z", 22))
# print(chr(ord("a") + 2))

# print(lasso_word(f"hello", 26))

# Try to decode the word "terra"
print(f'Shifting Terra by 13 gives:\n{lasso_word("Terra", 13)} \n')

# print(lasso_word(f"Ncevy", 13))
# print(lasso_word(f"gpvsui", 25))
# print(lasso_word(f"ugflgkg", -18) + lasso_word(f"wjmmf", -1))


# print("Shifting Ncevy by 13 gives: \n" + lasso_word("Ncevy", 13))
# print("Shifting gpvsui by 25 gives: \n" + lasso_word("gpvsui", 25))
# print("Shifting ugflgkg by -18 gives: \n" + lasso_word("ugflgkg", -18))
# print("Shifting wjmmf by -1 gives: \n" + lasso_word("wjmmf", -1))

print(lasso_sentence_dic(message_dic))

print(lasso_sentence_list(word_list, shift_list))
# print(f"{message_dic.keys()}, {message_dic.values()}")
print(lasso_sentence_list(list(message_dic.keys()), list(message_dic.values())))

# Other challenges for your decrypt code
# As an added challenge, you can explore how to:

# Maintain casing for each letter throughout the decoding process. DONE
# Create a function to read in an entire message without having to print each word individually. DONE
# Modify your decoder to include numbers.
