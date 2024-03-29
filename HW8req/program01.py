'''
Your dear friend Pico de Paperis sent you a very strange message scribbled on a postcard.
You haven't seen him in a long time and you've always had fun writing to each other in code.
To decode his message, go and look for a rather particular book in your library,
the Archimedes Pythagorean cipher. The cipher to be applied is the famous "Pharaoh's Cipher".
The decipherment with the Pharaoh's method is based on rules for substituting sequences of symbols in the text.
The reason why it is called "Pharaoh's cipher" is that in ancient Egyptian sequences made up of multiple hieroglyphs
could be written in any order, so any anagram of the sequences was valid.
To make things stranger, Pico de Paperis decided to use a cipher that is not exactly the one of Pharaoh,
but a variant of it. Instead of using anagrams he uses "quasi-anagrams", that is, anagrams that in the original text
have one more spurious character than the searched sequence.
The cipher contains pairs of sequences that indicate how to transform the text.
For example, the pair 'shampoo' -> 'soap' corresponds to searching for a point in the message where the sequence
'shampoo' appears (or an anagram of it) but with an extra character (e.g. 'pmQohaso')
and replace it with the sequence 'soap'.
Decoding the message can lead to more possible final messages, because there can be more sequences in the text
that can be transformed at any time and the order of transformations influences subsequent transformations.
At some point it will happen that none of the "quasi-anagrams" of a cipher sequence is present anywhere
in the sequence of symbols, and therefore it is no longer possible to make transformations.
We call these sequences final sequences.
Of all the possible final sequences, the one we are interested are all the shortest.

To decode the Pico de Paperis message you must implement the function
pharaohs_revenge(encrypted_text : str, pharaohs_cypher : dict[str,str]) -> set[str]:
which receives as arguments:
- the text that Pico de Paperis sent you, as a string of symbols (characters)
- the cipher to be applied, a dictionary whose keys are the sequences to search for a quasi-anagram in the text
    and as the associated value the string to replace the quasi-anagram found with.
The function must return the set of the shortest texts obtainable by repeatedly applying
the transformations until it is no longer possible to apply any of them.

Example:
encrypted_text  = 'astronaut-flying-cyrcus'
pharaohs_cypher = {'tuar': 'me', 'cniy': 'op', 'sorta': 'tur', 'fult': 'at', 'rycg': 'nc'}

Result: {'tmeopcus', 'metopcus', 'ameopcus', 'atmepcus'}
Notice, and all the transformations applied are those contained in the example.txt file
(in alphabetical order and without repetitions)

NOTE: At least one of the functions or methods you implement must be recursive
NOTE: the recursive function/method must be defined at the outermost level
      otherwise you will fail the recursion test.
'''

class SubString:
    def __init__(self, value, start, end) -> None:
        self.value = value
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f"'{self.value}' start at index {self.start} and end at index {self.end}"

def split_text(text, lenght):
    return [SubString(text[i:i+lenght], i, i+lenght) for i in range(len(text)-lenght+1)]

def get_substraction(list1, list2):
    for c in list2:
        try:
            list1.remove(c)
        except ValueError:
            pass
    return list1

def is_reducible(encrypted_text, pharaohs_cypher):
    for key in pharaohs_cypher:
        lenght = len(key)+1
        sub_string_list = split_text(encrypted_text, lenght)
        for sub_string in sub_string_list:
            substraction = get_substraction(list(sub_string.value), list(key))
            if len(substraction) == 1:
                return True
    return False

def create_set_rec(encrypted_text : str, pharaohs_cypher : dict[str,str], done) -> set[str]:
    if not is_reducible(encrypted_text, pharaohs_cypher):
        done.add(encrypted_text)
    else:
        for key in pharaohs_cypher:
            lenght = len(key)+1
            sub_string_list = split_text(encrypted_text, lenght)
            for sub_string in sub_string_list:
                substraction = get_substraction(list(sub_string.value), list(key))
                if len(substraction) == 1:
                    new_encrypted_text = "".join((encrypted_text[:sub_string.start], pharaohs_cypher[key], encrypted_text[sub_string.end:]))
                    create_set_rec(new_encrypted_text, pharaohs_cypher, done)
    

def min_length_strings(input_set):
    min_length = min(len(s) for s in input_set)
    return {s for s in input_set if len(s) == min_length}


def pharaohs_revenge(encrypted_text : str, pharaohs_cypher : dict[str,str]) -> set[str]:
    a = set()
    create_set_rec(encrypted_text, pharaohs_cypher, a)
    b = min_length_strings(a)
    return b



if __name__ == '__main__':
    encrypted_text =  "aaabaaac"
    pharaohs_cypher = {"aa":"bc","bb":"c","cc":"d"}
    c = pharaohs_revenge(encrypted_text, pharaohs_cypher)
    print(c)