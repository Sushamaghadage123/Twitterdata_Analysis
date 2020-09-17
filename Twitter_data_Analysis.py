import pandas as pd
#from pandas_profiling import ProfileReport
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re

from collections import Counter
from matplotlib import pyplot as plt
#from nltk.stem import WordNetLemmatizer

data=pd.read_csv("sample.csv",delimiter=',',index_col=10)
'''per=ProfileReport(data)
per.to_file("output.html")'''
#print(per)
#print(data)
#print(data.describe())
#print(data.shape)
import sys
m=[]
final_words=[]
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
for i in data['Tweet Content']:
    m.append(i.translate(non_bmp_map))
print(m)
meaning_less_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "done", "should", "now"]
final_words=[]
for tweet in m:
    # Remove all the special characters
    cleaned_string=re.sub(r'\W', ' ',tweet)
    #make the all string in lowercase
    cleaned_string=cleaned_string.lower()
    # remove all single characters
    cleaned_string= re.sub(r'\s+[a-zA-Z]\s+', ' ', cleaned_string)
    # Remove single characters from the start
    cleaned_string = re.sub(r'\^[a-zA-Z]\s+', ' ',cleaned_string)
    #Substituting multiple spaces with single space
    cleaned_string= re.sub(r'\s+', ' ', cleaned_string, flags=re.I)
    #replacing the unvanted words from string
    tokenized_words=cleaned_string.split()
    for word in tokenized_words:
        if word not in meaning_less_words:
            final_words.append(word)   
print(final_words)  

# Lemmatization - From plural to single + Base form of a word (example better-> good)
'''lemma_words = []
for word in final_words:
   word = WordNetLemmatizer().lemmatize(word)
   lemma_words.append(word)'''

# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

'''#overall the tweeter is positive or negative
cleaned_text=" ".join(final_words)
def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")


sentiment_analyse(cleaned_text)'''
print(emotion_list)
w = Counter(emotion_list)
print(w)
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()

print(data['Likes Received'])
print(max(data['Likes Received']))




