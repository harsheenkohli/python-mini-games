# sentiment analysis => working out whether a certain piece of text is positive or negative

# Step-1 : Download Facebook data
# Step-2 : Store it in an excel file
# Step-3 : Import pandas library => Provides easy to use DS for data analysis
# Step-4 : Import nltk library => to process human language => provides sentiment analysis
# Step-5 : Download VADER Lexicon => Lexicon acts as a dictionary here
# Step-6 : Use VADER (Valence Aware Dictionary and Sentiment Reasoner) => also takes intensity of sentiment into account
# Step-7 : Convert Excel sheet to data frame with the help of Pandas => Data frame = 2D structure in table format

import pandas
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.downloader.download('vader_lexicon')
file = 'd:/TJCP/Week 8/Facebook-sentiment-analysis.xlsx'     # write proper path

xl = pandas.ExcelFile(file)     # read from excel
dfs = xl.parse(xl.sheet_names[0])     # 0 => info in first column
# parsing excel sheet to data frame

# name of column => removes blank rows from data frame
dfs = list(dfs['Timeline'])
# print(dfs)

# initialise sentiment intensity analyser
sid = SentimentIntensityAnalyzer()

# actual fb data has time as well, which we should not analyse in sentiment
# remove this by hard code
str1 = "UTC+"

for data in dfs:
    a = data.find(str1)
    if (a == -1):
        ss = sid.polarity_scores(data)
        # list of neg, neu, pos and compound
        print(data)
        for k in ss:
            print(k, ss[k])
