
# Python 3.14

import csv

# Produce a list of 333k english words ranked by frequency

ranked_english_words = []

with open('unigram_freq.csv', newline='') as csvfile:
    spam_reader = csv.reader(csvfile)
    for row in spam_reader:
        ranked_english_words.append(row[0])

# print(ranked_english_words)


# Parse hsscript.txt to extract all
# words into a 1D list called homestuck_all_words.
# For each word in ranked_english_words, find
# the frequency of that word in homestuck_all_words.
# Create a CSV file called homestuck_freq.csv
# where column A and B are <word, count> respectively,
# and the most common words are at the top of the CSV.


