#!/usr/bin/env python3
# Python 3.14
import csv
import re
from collections import Counter


##########      RANK ENGLISH WORDS          ##########
# Produce a list of english words ranked by frequency
ranked_english_words = []
with open('unigram_freq.csv', newline='', encoding='utf-8') as csvfile:
    spam_reader = csv.reader(csvfile)
    for row in spam_reader:
        if row:
            ranked_english_words.append(row[0])


##########      PARSE HOMESTUCK SCRIPT      ##########

# Parse `hsscrpt.txt` to extract all words into a 1D list
# called `homestuck_all_words`, in order of appearance.

# Read the file trying common encodings and fall back if necessary
text = None
for enc in ('utf-8', 'utf-8-sig', 'utf-16', 'utf-16-le', 'latin-1'):
    try:
        with open('hsscrpt.txt', encoding=enc) as f:
            text = f.read()
        break
    except (UnicodeDecodeError, LookupError):
        continue

if text is None:
    # last-resort: decode bytes ignoring errors
    with open('hsscrpt.txt', 'rb') as f:
        text = f.read().decode('utf-8', errors='ignore')

# Tokenize: sequences of letters and apostrophes; preserve order
tokens = re.findall(r"[A-Za-z']+", text)

# Keep original casing to preserve exact appearances (change to .lower() if desired)
homestuck_all_words = tokens


##########      BUILD homestuck_freq.csv    ##########

# Build a case-insensitive counter of all words from the Homestuck text.
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



##########      BUILD UNIGRAM FREQ MODIFIED ##########

# Pseudocode:
# Copy unigram_freq.csv to unigram_freq_modified.csv.
# Add a third column to unigram_freq_modified.csv that
# contains the decimal proportion of each word (float).

unigram_rows = []
total = 0

with open('unigram_freq.csv', newline='', encoding='utf-8') as uf:
    reader = csv.reader(uf)
    header = next(reader, None)
    for row in reader:
        if not row:
            continue
        word = row[0]
        count_str = row[1] if len(row) > 1 else '0'
        try:
            count = int(count_str)
        except Exception:
            try:
                count = int(float(count_str))
            except Exception:
                count = 0
        unigram_rows.append((word, count))
        total += count

with open('unigram_freq_modified.csv', 'w', newline='', encoding='utf-8') as outf:
    writer = csv.writer(outf)
    if header:
        writer.writerow(header + ['proportion'])
    else:
        writer.writerow(['word', 'count', 'proportion'])

    for word, count in unigram_rows:
        if total == 0:
            prop = 0.0
        else:
            prop = float(count) / float(total)
        writer.writerow([word, str(count), repr(prop)])

print('Wrote unigram_freq_modified.csv with third column for frequency proportion.')


##########      BUILD HOMESTUCK FREQ MODIFIED ##########

# pseudocode
# Repeat line 73 to 115 BUT itss for homestuck_freq_modified.csv instead.

# Implement: create homestuck_freq_modified.csv with float proportions
# proportion = count / total_homestuck_tokens

hf_rows = []
total_homestuck_tokens = len(homestuck_all_words)

with open('homestuck_freq.csv', newline='', encoding='utf-8') as hf:
    reader = csv.reader(hf)
    header = next(reader, None)
    for row in reader:
        if not row:
            continue
        word = row[0]
        count_str = row[1] if len(row) > 1 else '0'
        try:
            count = int(count_str)
        except Exception:
            try:
                count = int(float(count_str))
            except Exception:
                count = 0
        hf_rows.append((word, count))

with open('homestuck_freq_modified.csv', 'w', newline='', encoding='utf-8') as outf:
    writer = csv.writer(outf)
    if header:
        writer.writerow(header + ['proportion'])
    else:
        writer.writerow(['word', 'count', 'proportion'])

    for word, count in hf_rows:
        if total_homestuck_tokens == 0:
            prop = 0.0
        else:
            prop = float(count) / float(total_homestuck_tokens)
        writer.writerow([word, str(count), repr(prop)])

print('Wrote homestuck_freq_modified.csv with float proportions (relative to homestuck tokens).')


##########      COMPARE FREUQENCIES FROM HOMESTUCK TO UNIGRAM ##########
