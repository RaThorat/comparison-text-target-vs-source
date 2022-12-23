#Correction of names

#First, you should use Levenshtein distances between strings,
# I found a link with the following Levenshtein Distance Algorithm for Python:
#https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python

# Define Levenshtein distance function (from the mentioned link)
def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 
            deletions = current_row[j] + 1  
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]
  
# Once you got this, you should make a function able to find the closest match between a given string and the list with the well spelled names.
names_list = ['4TU.Center for Research Data']
good_names = repo_list

# Define a function that returns the best match
def get_closest_match(name, real_names):
    levdist = [levenshtein(name, real_name) for real_name in real_names]
    for i in range(len(levdist)):
        if levdist[i] == min(levdist):
            return real_names[i]

# Loops the first list
final_list = [ get_closest_match(name, good_names) for name in names_list ]
# Finally you just have to loop the first list with this function. The outcome is the following:
print(final_list)

