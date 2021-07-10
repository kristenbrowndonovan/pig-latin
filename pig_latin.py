while True:

# get sentence from user

    original = input("What would you like to translate?: ").strip().lower()

# split sentence into individual words

    words = original.split()

# translate each word (loop through each word and convert)

    new_words = []

# if word starts with vowel, add "yay"

    for word in words:
        if word[0] in "aeiou":
            new_word = word + "yay"
            new_words.append(new_word)
    

# otherwise, move consonents to end of word and add "ay"
        else:
            vowel_pos = 0

            for letter in word:
                if letter not in "aeiou":
                    vowel_pos = vowel_pos + 1
                else:
                    break
            cons = word[0:vowel_pos]
            the_rest = word[vowel_pos:]
            new_word = the_rest + cons + "ay"
            new_words.append(new_word)
        

# string words back into sentence

    output = " ".join(new_words)

# print translated sentence

    print(output.capitalize())
