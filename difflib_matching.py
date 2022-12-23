import difflib
def is_similar(first, second, ratio):
    return difflib.SequenceMatcher(None, first, second).ratio() > ratio


first = ['resarch data']
second = ['4TU.centre for Research Data', 'Figshare']

result = [s for f in first for s in second if is_similar(f,s, 0.7)]
print(result)
