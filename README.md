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

The fuzzywuzzy library uses a variety of string matching algorithms to determine the similarity between two strings. You can read more about how it works [here](https://github.com/seatgeek/fuzzywuzzy#fuzz-functions)

# 3. Fuzzy String Matching

This script uses the pandas and fuzzywuzzy libraries to perform fuzzy string matching between two Excel files (text1.xlsx and text2.xlsx). The script compares the data in the Name column of each dataframe and returns the closest match for each element in the first dataframe according to a customizable threshold value (default is 80).

# Usage

To use the string matching script, make sure you have the required libraries installed and that you have two Excel files (text1.xlsx and text2.xlsx) in the same directory as the script. Then, run the script to perform the matching and output the results.

# Notes

The fuzzywuzzy library uses a variety of string matching algorithms to determine the similarity between two strings. In this case, the token_set_ratio method is used, which returns a ratio of the number of tokens in the intersection of the sets of tokens formed from the strings to the number of tokens in the union of the sets of tokens formed from the strings. You can read more about the different matching methods available in fuzzywuzzy [here](https://github.com/seatgeek/fuzzywuzzy#fuzz-functions).

The script also includes a function, find_alpha(), that removes non-alphabetic characters from a string. This function is used to clean the data in the Name column of dframe1 before performing the matching.
