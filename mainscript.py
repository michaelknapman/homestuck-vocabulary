# Python 3.14
import csv
import re
from collections import Counter

##########      RANK ENGLISH WORDS          ##########
# Produce a list of 333k english words ranked by frequency
ranked_english_words = []
with open('unigram_freq.csv', newline='') as csvfile:
    spam_reader = csv.reader(csvfile)
    for row in spam_reader:
        ranked_english_words.append(row[0])
# print(ranked_english_words)

##########      PARSE HOMESTUCK SCRIPT      ##########

# Parse `hsscrpt.txt` to extract all words into a 1D list
# called `homestuck_all_words`, in order of appearance.
# There should be multiple entries for each unique word.

# Read the file trying common encodings and fall back if necessary
text = None
for enc in ('utf-8', 'utf-8-sig', 'utf-16', 'utf-16-le', 'latin-1'):
    try:
        with open('hsscrpt.txt', encoding=enc) as f:
            text = f.read()
        break
    except UnicodeDecodeError:
        continue

if text is None:
    # last-resort: decode bytes ignoring errors
    with open('hsscrpt.txt', 'rb') as f:
        text = f.read().decode('utf-8', errors='ignore')

# Tokenize: sequences of letters and apostrophes; preserve order
tokens = re.findall(r"[A-Za-z']+", text)

# Keep original casing to preserve exact appearances (change to lower() if desired)
homestuck_all_words = tokens

##########      BUILD homestuck_freq.csv    ##########

# Build a case-insensitive counter of all words from the Homestuck text.
# We use lowercase keys so they match typical unigram lists.
homestuck_counter = Counter(w.lower() for w in homestuck_all_words)

# Normalize ranked_english_words: skip header if present and lowercase
normalized_ranked = []
for w in ranked_english_words:
    if isinstance(w, str) and w.lower() == 'word':
        continue
    normalized_ranked.append(w.lower())

# For each word in the ranked list, get its frequency in the homestuck text
results = [(w, homestuck_counter.get(w, 0)) for w in normalized_ranked]

# Sort by frequency descending (most common first)
results_sorted = sorted(results, key=lambda x: x[1], reverse=True)

# Write out CSV: word,count
with open('homestuck_freq.csv', 'w', newline='', encoding='utf-8') as out_csv:
    writer = csv.writer(out_csv)
    writer.writerow(['word', 'count'])
    writer.writerows(results_sorted)

print(f'Wrote homestuck_freq.csv ({len(results_sorted)} entries).')
