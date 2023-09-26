# Stylometry => Quantitative study of literacy style.
# Authors have consistent, recognizable and unique ways
# using nltk library
# criteria : word length distribution

import os
import nltk
# nltk.download()

papers = {
    "Madison": [10, 14, 37, 38, 39, 40, 41, 42, 43, 44,
                45, 46, 47, 48],
    "Hamilton": [1, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17,
                 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                 31, 32, 33, 34, 35, 36, 59, 60, 61, 65,
                 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
                 76, 77, 78, 79, 80, 81, 82, 83, 84, 85],
    "Jay": [2, 3, 4, 5],
    "Shared": [18, 19, 20],
    "Disputed": [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63]
}


def read_files(filename):
    directory = r"d:/TJCP/Week 9/data"
    strings = []
    for file in filename:
        file_path = os.path.join(directory, f'federalist_{file}.txt')
        with open(file_path) as f:
            # value of each key for each author
            strings.append(f.read())

    return ("\n".join(strings))


# key : author's name, value : all words in a single string
federalist_by_author = {}

for author, files in papers.items():
    # author = key, files = values
    federalist_by_author[author] = read_files(files)
    # all words from all papers will be stored in strings

for author in papers:
    print(federalist_by_author[author][:100])
    # taking sliced 100 characters for testing

# word-length distribution
authors = ('Hamilton', 'Madison', 'Jay', 'Shared', 'Disputed')

author_tokens = length_distribution = {}

for author in authors:
    tokens = nltk.word_tokenize(federalist_by_author[author])
    # all punctuated words, letters will be tokenized as strings

    # Initialize a list for each author to store tokens
    author_tokens[author] = []

    # filter out punctuations
    # author_tokens[author] = ([token for token in tokens if any(c.alpha) for c in token])
    for token in tokens:
        if any(c.isalpha() for c in token):
            author_tokens[author].append(token)

    token_lengths = [len(token) for token in author_tokens[author]]

    length_distribution[authors] = nltk.FreqDist(token_lengths)

    length_distribution[authors].plot(20, title=author)
    # maximum 15 words ka graph
