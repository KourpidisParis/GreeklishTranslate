def get_greek_letter(ch1):
    # Έλεγχος για το αν τα γράμματα έιναι πεζά
    if ch1 is 'a': return 'α'
    if ch1 is 'b': return 'β'
    if ch1 is 'c': return 'κ'
    if ch1 is 'd': return 'δ'
    if ch1 is 'e': return 'ε'
    if ch1 is 'f': return 'φ'
    if ch1 is 'g': return 'γ'
    if ch1 is 'h': return 'η'
    if ch1 is 'i': return 'ι'
    if ch1 is 'j': return 'τζ'
    if ch1 is 'k': return 'κ'
    if ch1 is 'l': return 'λ'
    if ch1 is 'm': return 'μ'
    if ch1 is 'n': return 'ν'
    if ch1 is 'o': return 'ο'
    if ch1 is 'p': return 'π'
    if ch1 is 'q': return 'κ'
    if ch1 is 'r': return 'ρ'
    if ch1 is 's': return 'σ'
    if ch1 is 't': return 'τ'
    if ch1 is 'u': return 'θ'
    if ch1 is 'v': return 'β'
    if ch1 is 'w': return 'ω'
    if ch1 is 'x': return 'χ'
    if ch1 is 'y': return 'υ'
    if ch1 is 'z': return 'ζ'

    # έλεγχος για κένα
    if ch1 is ' ': return ' '

    # έλεγχος για το αν τα γράμματα είναι κεφαλαία
    if ch1 is 'A': return 'Α'
    if ch1 is 'B': return 'Β'
    if ch1 is 'C': return 'Κ'
    if ch1 is 'D': return 'Δ'
    if ch1 is 'E': return 'Ε'
    if ch1 is 'F': return 'Φ'
    if ch1 is 'G': return 'Γ'
    if ch1 is 'H': return 'Η'
    if ch1 is 'I': return 'Ι'
    if ch1 is 'J': return 'TZ'
    if ch1 is 'K': return 'Κ'
    if ch1 is 'L': return 'Λ'
    if ch1 is 'M': return 'Μ'
    if ch1 is 'N': return 'Ν'
    if ch1 is 'O': return 'Ο'
    if ch1 is 'P': return 'Π'
    if ch1 is 'Q': return 'Κ'
    if ch1 is 'R': return 'Ρ'
    if ch1 is 'S': return 'Σ'
    if ch1 is 'T': return 'Τ'
    if ch1 is 'U': return 'Θ'
    if ch1 is 'V': return 'Β'
    if ch1 is 'W': return 'Ω'
    if ch1 is 'X': return 'Χ'
    if ch1 is 'Y': return 'Υ'
    if ch1 is 'Z': return 'Ζ'


def get_the_same_character(x):
    return x


def is_character(ch1):
    list1 = ['a', 'b', 'c', 'd', 'e', 'o', 'x', 'i', 't', 'r', 'f', 'n', 'y', 'w', 'l', 'k', 'h', 'm', 's', 'u', 'e',
             'h', 'g', 'z', 'p', 'v', 'q', 'j']
    list2 = ['A', 'B', 'C', 'D', 'E', 'X', 'O', 'I', 'T', 'R', 'F', 'N', 'Y', 'W', 'L', 'K', 'H', 'M', 'S', 'U', 'E',
             'H', 'G', 'Z', 'P', 'V', 'Q', 'J']
    if (ch1 in list1) or (ch1 in list2):
        return True


# ακολουθούν έλεγχοι για το τελικό 'ς'
def check_for_last_s(temp_list):
    final_list = []
    greek_alphabet = ["α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "ι", "κ", "λ", "μ", "ν", "ξ", "ο", "π", "ρ", "σ", "τ",
                      "υ", "φ", "χ", "ψ", "ω"]
    i = 0
    while i < temp_list.__len__():
        if temp_list[i] == 'σ' and i == temp_list.__len__() - 1:
            temp_list[i] = 'ς'
            break
        if temp_list[i] == 'σ' and temp_list[i + 1] == ' ':
            temp_list[i] = 'ς'

        if temp_list[i] == 'σ' and temp_list[
            i + 1] not in greek_alphabet:  # αν δεν ειναι στο ελληνικο αλφάβητο ,τοτε θα έιναι κάποιος άλλος χαρακτηρας πχ .  . /,
            temp_list[i] = 'ς'
        i = i + 1


def check_tow_characters_will_be_one(list_with_letters, final_text_on_greek):
    special_combinations = ["πσ", "τη", "ΤΗ",
                            "ΠΣ","κσ","ΚΣ"]  # Οι χρήστες που γράφουν greeklish, συχνα πληκτρολογούν δύο αγγλικά γράμματα που
    # όμως στα ελληνικα μεταγράζεται ως ένα
    # Τα γράμματα αυτά ειναι στην λίστα special combinatons

    list_with_letters.append("-")  # προσθέτω έναν χαρακτήρα ,στη τελευταία θέση που θα σηματοδοτεί το τέλος της λίστας

    i = 0
    while i < list_with_letters.__len__():
        j = 0
        while j < special_combinations.__len__():
            special_phrase = special_combinations[j]
            if list_with_letters[i] == special_phrase[0] and list_with_letters[i + 1] == special_phrase[1]:  # ελέγω
                # αν το τρέχον γράμμα και το αμέσως επόμενο του είναι ενας απο τους ζητούμενους συνδυασμούς
                # αντικαθιστω
                if special_phrase.__eq__("πσ"): list_with_letters[i] = 'ψ'
                if special_phrase.__eq__("τη"): list_with_letters[i] = "θ"
                if special_phrase.__eq__("ΤΗ"): list_with_letters[i] = "Θ"
                if special_phrase.__eq__("ΠΣ"): list_with_letters[i] = "Ψ"
                if special_phrase.__eq__("ΚΣ"): list_with_letters[i] = "Ξ"
                if special_phrase.__eq__("κσ"): list_with_letters[i] = "ξ"
                list_with_letters.remove(list_with_letters[i + 1]) # αφαιρώ το επόμενο γράμμα δηλαδή το i + 1
            j = j + 1
        i = i + 1

    i = 0
    while i < list_with_letters.__len__() - 1: # και εδώ αφαιρώ τον χαρακτήρα - που πρόσθεασε στη αρχη
        final_text_on_greek.append(list_with_letters[i])
        i = i + 1
