"""Functions for creating, transforming, and adding prefixes to strings."""

#Do this one leaving pass for the remainders and see if it works (if it works, go back to the other exercise and add pass to the latter ones.)

def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    
    new_word = 'un' + word
    return new_word
    
    #Take the word and add 'un' at place 0


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    prefix = vocab_words[0]
    prefixed_words = [prefix + word for word in vocab_words[1:]]
    output = ' :: '.join([prefix] + prefixed_words)
    return output

  

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    
    no_suffix = word[:-4]
    
    if no_suffix[-1] == 'i':
        return no_suffix[:-1] + 'y'
    else:
        return no_suffix
    




def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    #Note to self, had to google how to remove the punctuation. Probs a better way to do this, come back to it later
    #Thought about googling for all types of punctuation, but would be instances where you wouldn't want to remove hyphens, or apostrophes
    if '.' in sentence:
        sentence = sentence.replace('.', '')
    words = sentence.split()
    adj = words[index]
    verb = adj + 'en'
    return verb


