""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''

from typing import FrozenSet

_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"

_pad = '_'

symbols = [_pad] + list(_letters_ipa)

symbols.append(" ")

# Export all symbols:
# symbols = [_pad] + list(URDU_ALL_CHARACTERS) + list(_letters_ipa)
# symbols.append(" ")
# symbols.append("(")
# symbols.append("e")
# symbols.append("n")
# symbols.append("u")
# symbols.append("r")
# symbols.append(")")
# symbols.append("l")
# symbols.append("k")
# symbols.append("h")
# symbols.append("t")
# symbols.append("s")
# symbols.append("w")
# symbols.append("a")
# symbols.append("d")
# symbols.append("b")
# symbols.append("j")
# symbols.append("i")
# symbols.append("m")
# symbols.append("f")
# symbols.append("p")
# symbols.append("z")
# symbols.append("c")
# symbols.append("o")
# symbols.append("g")
# symbols.append("q")
# symbols.append("v")
# symbols.append("x")
# symbols.append("y")
# symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)

# Special symbol ids
SPACE_ID = symbols.index(" ")
