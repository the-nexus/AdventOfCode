def isValidPassphrase(passphrase):
    words = passphrase.replace("\n", "").split(" ")
    word_list = []
    for word in words:
        characters = list(word)
        characters.sort()
        sorted_word = str.join("", characters)
        if sorted_word in word_list:
            return False
        word_list.append(sorted_word)
    return True


filename = "./day04/day04_input.txt"
input_file = open(filename)
lines = input_file.readlines()

valid_passphrase_count = 0
for passphrase in lines:
    if isValidPassphrase(passphrase):
        valid_passphrase_count = valid_passphrase_count + 1

print("There are", valid_passphrase_count, "valid passphrases")
