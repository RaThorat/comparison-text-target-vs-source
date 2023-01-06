# comparison-text-target-vs-source
Comparison-text-target-vs-source

# 1. Sequence Matching (difflib)
This script contains a function is_similar that compares two sequences and returns True if their similarity ratio is above a certain threshold. The similarity ratio is calculated using the SequenceMatcher from the difflib library.

# Usage
To use the function, call 'is_similar(first, second, ratio)' and pass in the two sequences to be compared as the first and second arguments, and the desired ratio as the third argument. The function will return 'True' if the similarity ratio of the two sequences is above the given ratio, and 'False' otherwise.

# 2. Fuzzy Spell Checker
This script provides a simple spell checking function using the fuzzywuzzy library and numpy. The function, correctspell(), takes in a word and a list of correct spellings, and returns the closest match in the list according to a customizable threshold value (default is 70).

# Usage

To use the spell checker, simply import the function and call it on the word you want to check. 

You can also set the thresh parameter to customize the minimum matching ratio required for a correction to be returned. If no match is found above the threshold, the function will return None.

# Notes

The fuzzywuzzy library uses a variety of string matching algorithms to determine the similarity between two strings. You can read more about how it works https://github.com/seatgeek/fuzzywuzzy
