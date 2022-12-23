from fuzzywuzzy import fuzz
import numpy as np

bad = ['4TU']

good = ['4TU.Center for Research Data','Figshare']

# you can even set custom threshold and only return matches if above certain
# matching threshold
def correctspell(word, spellcorrect, thresh = 70):
    mtchs = map(lambda x: fuzz.ratio(x, word) if fuzz.ratio(x, word) > thresh else None, spellcorrect)
    max = np.max(mtchs)
    if max is not None:
        return spellcorrect[mtchs.index(max)]
    else:
        return None

# get correct spelling
map(lambda x: correctspell(x, good, thresh = 70), bad) # ['Barcelona', 'Amsterdam', 'Prague']
