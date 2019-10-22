import help_lib

if __name__ == "__main__":

    while True:
        print("Give your text on greeklish: ")
        word = input()
        text_on_greeklish = []

        for x in word:
            text_on_greeklish.append(x)  # δημιουργώ μια λίστα με τα γράμματα που θα μετατρέψω σε ελληνικά

        text_on_greek = []  # η λίστα αυτή περιλαμβάνει τη λέξη στα ελληνικά

        for x in text_on_greeklish:
            if help_lib.is_character(x):
                letter = help_lib.get_greek_letter(x)
                text_on_greek.append(letter)
            else:
                letter = help_lib.get_the_same_character(x)
                text_on_greek.append(letter)

        final_text_on_greek = []
        help_lib.check_for_last_s(text_on_greek)
        help_lib.check_tow_characters_will_be_one(text_on_greek, final_text_on_greek)
        str1 = ''.join(final_text_on_greek)
        print(str1)

        answer = input(" Do you want to translate any text ,yes/no : ")
        answer = answer.lower()

        answers = ["yes", "no"]
        while True:
            if answer not in answers:
                answer = input("ONLY yes or no : ")
                answer = answer.lower()
            else:
                break

        if answer.__eq__("no"):
            break