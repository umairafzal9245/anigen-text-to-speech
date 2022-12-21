""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''

from typing import FrozenSet

_letters_ipa = "akəː.ɟbxtrhmɛpẽuʌʂsiloʋndɪfjqʃcɡʰʊwʈzɔɖʐɣðŋʒɹœɒθɐʔ"

_pad = '_'

symbols = [_pad] + list(_letters_ipa)

symbols.append(" ")

# Special symbol ids
SPACE_ID = symbols.index(" ")
