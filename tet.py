from phonemizer import phonemize
import re
def collapse_whitespace(text):
  return re.sub(_whitespace_re, ' ', text)
text = "اس حوالے سے مصنف نے لکھاہے کہ ٹرمپ کومعافی دینے کابہت شوق ہے"
phonemes = phonemize(text, language='ur', backend='espeak', strip=True, language_switch='remove-flags')
print(phonemes)