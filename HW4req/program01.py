'''
Ajeje the librarian, recently found a hidden room
in the Keras Library (a great place located in
Umkansa, the largest village in the White Mountains).
There, she discovered several books, containing
music scores of ancient Tarahumara songs.
So, she invited over a musician friend to have a look
at them, and he informed her that the scores are
written in Tarahumara notation and need to be translated
into a notation familiar to Umkansanian musicians,
so they can play them back.

Tarahumaras used numbers instead of letters for
writing notes:
0 in place of A, 1 in place of B, and so on, until
7 in place of G. Flat (b) and sharp (#) notes
(see note 3 below, if you do not know what flat
and sharp notes are)
were followed by a - and a +, respectively (for example,
0- meant flat A). Moreover, they just repeated the
same number multiple times to represent the note's
duration. For example, 0000 would mean that the
A note had a length of 4, while 0-0-0-0- would mean
that the A flat note had a length of 4.
Pauses were written down
as spaces; for example, twelve spaces represent
a pause of 12. Both notes and pauses could span
different lines of the score (e.g., starting on line
x and continuing on line x + 1, x + 2, and so on).
Finally, music scores were written from right
to left and from top to bottom, and going to a new
line did not mean anything in terms of the music score.
Umkansanians, instead, are used to write down notes using letters,
and each note is followed by its duration (so, the example
above would be written as A4). Flat and sharp notes are
followed by a b or a #, respectively (for example, A flat
is written as Ab, so the example above would be written ad
Ab4). Pauses are written using the letter P, followed by
their duration, and no spaces are used at all.
Finally, they are used to read music from left
to right on a single row.

As Ajeje knows that you are a skilled programmer, she
provides you with a folder containing the transcription
of all the Tarahumara songs she found, organized in
multiple subfolders and files (one song per file).
Also, she prepared an index file in which each row
contains the title of a Tarahumara song (in quotes),
followed by a space and the path of the file containing
that song (in quotes, relative to the root folder).
She would like to translate all the songs listed in
the index and store them into new files, each one
named with the title of the song it contains (.txt),
in a folder structure matching the original one.
Also, she would like to store in the root folder of
the created structure, a file containing on each row
the title of a song (in quotes) and the corresponding
song length, separated by a space. Songs in the index
need to be ordered in descending length and, if the
length of some songs is the same, in ascending alphabetical
order. The length of a song is the sum of the durations
of all notes and pauses it is made of.

Would you be able to help Ajeje out in translating
the Tarahumara songs into Umkansanian ones?

Note 0: below, you are provided with a function to
Umkansanize the Tarahumara songs; after being executed,
it must return a dictionary in which each key is a song
title and the associated value is the song's duration

Note 1: the songs index file index.txt
is stored in the source_root folder

Note 2: the index of the translated songs
index.txt is in the target_root folder

Note 3: flat and sharp notes are just "altered" versions
of regular notes; for example an F# ("F sharp") is the
altered version of an F, that is, an F note which is a
half of a tone higher than a regular F; the same holds for
flat notes, which are a half of a tone lower than regular notes;
from the point of view of the homework, flat and sharp notes
must be treated the same as regular notes (except for their notation).

Note 4: to create the directory structure you can use the 'os' library functions
(e.g. os.makedirs)
'''

import os

#We extract the contents of the song into a string:
# each line must be cleaned of the \n and inverted (we use slicing).

def convert_string(line):
    return line.removesuffix("\n")[::-1]


def get_music_string(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = list(map(convert_string, f.readlines()))
    return "".join(lines)


###    DECODER    ###

#      TAR     ---->    MINE    ----->     UM
#
#  In my encoding the altered notes are represented with a single character
#  and each time unit represents a single character.


def convert_from_tar_to_my_encoding(tar_string):

    conversion_dict_0 = {
    "0-":"H",
    "0+":"I",
    "1-":"J",
    "1+":"K",
    "2-":"L",
    "2+":"M",
    "3-":"N",
    "3+":"O",
    "4-":"Q",
    "4+":"R",
    "5-":"S",
    "5+":"T",
    "6-":"U",
    "6+":"V"
    }

    conversion_dict_1 = {
    "0":"A",
    "1":"B",
    "2":"C",
    "3":"D",
    "4":"E",
    "5":"F",
    "6":"G",
    " ":"P"
    }
    mapping_table_conversion_1 = str.maketrans(conversion_dict_1)

    for key, value in conversion_dict_0.items():
        tar_string = tar_string.replace(key, value)
    tar_string = tar_string.translate(mapping_table_conversion_1)
    return tar_string

#  The function returns a string in which each character is followed
#  by the number of times it appears in each internal substring.
def replace_duplicates(m_e_s):
    result = []
    i = 0
    while i < len(m_e_s):
        char = m_e_s[i]
        count = 1
        try:
            while m_e_s[i + 1] == char:
                count += 1
                i += 1
        except IndexError:
            pass
        result.append(char + str(count))
        i += 1
    return ''.join(result)


def convert_from_my_encoding_to_um(s):
    conversion_dict_2 = {
    "H":"Ab",
    "I":"A#",
    "J":"Bb",
    "K":"B#",
    "L":"Cb",
    "M":"C#",
    "N":"Db",
    "O":"D#",
    "Q":"Eb",
    "R":"E#",
    "S":"Fb",
    "T":"F#",
    "U":"Gb",
    "V":"G#"
    }
    mapping_table_conversion_2 = str.maketrans(conversion_dict_2)
    s = replace_duplicates(convert_from_tar_to_my_encoding(s))
    s = s.translate(mapping_table_conversion_2)
    return s


def converter(s):
    s = convert_from_tar_to_my_encoding(s)
    dur = len(s)
    s = convert_from_my_encoding_to_um(s)
    return s, dur


def write_document(s, filepath):
    with open(filepath,"w", encoding="utf-8") as f_out:
        print(s, file = f_out)

#  Create index in target root
def create_index(index_dict, source_root):
    with open("".join((source_root, "/index.txt")), "w", encoding="utf-8") as f_index:
        for name, dur in sorted(index_dict.items(), key=lambda item: (-item[1], item[0])):
            line = '"'+name+'" '+str(dur)
            print(line, file=f_index)


####  MAIN FUNCTION ####
def Umkansanize(source_root:str, target_root:str) -> dict[str,int]:
    index_dict = dict()
    with open(source_root+"/index.txt","r", encoding="utf-8") as f:
            lines = f.readlines()
    for line in lines:
        name, ipath = line.removesuffix("\n")[1:-1].split('" "')
        try:
            pos, oldname = ipath.rsplit("/", maxsplit = 1)
            os.makedirs("/".join((target_root, pos)), exist_ok=True)
            content, dur = converter(get_music_string("/".join((source_root, ipath))))
            write_document(content, "/".join((target_root, pos, name+".txt")))
            index_dict[name] = dur
        except:
            os.makedirs(target_root, exist_ok=True)
            content, dur = converter(get_music_string("/".join((source_root, ipath))))
            write_document(content, "/".join((target_root, name+".txt")))
            index_dict[name] = dur
    create_index(index_dict, target_root)
    return index_dict



if __name__ == "__main__":
    #Umkansanize("test05", "test05.prova")
    pass