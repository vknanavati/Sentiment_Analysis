import nltk
from pprint import pprint
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

nltk.download(
    [
        "names",
        "stopwords",
        "state_union",
        "twitter_samples",
        "movie_reviews",
        "averaged_perceptron_tagger",
        "vader_lexicon",
        "punkt",
    ]
)

words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]


stopwords = nltk.corpus.stopwords.words("english")

words = [w for w in words if w.lower() not in stopwords]

# print(words)
# text = """
# For some quick analysis, creating a corpus could be overkill.
# If all you need is a word list,
# there are simpler ways to achieve that goal."""

# pprint(nltk.word_tokenize(text), width=79, compact=True)
# --> ['For', 'some', 'quick', 'analysis', ',', 'creating', 'a', 'corpus', 'could',
#  'be', 'overkill', '.', 'If', 'all', 'you', 'need', 'is', 'a', 'word', 'list',
#  ',', 'there', 'are', 'simpler', 'ways', 'to', 'achieve', 'that', 'goal', '.']

text = nltk.Text(nltk.corpus.state_union.words())
fd = nltk.FreqDist(words)

fd.most_common(3)
fd.tabulate(3)
fd["America"]
fd["ameria"]
fd["AMERICA"]
# words: list[str] = nltk.word_tokenize(text)
lower_fd = nltk.FreqDist([w.lower() for w in fd])

text.concordance("america", lines=5)
# print(text)

concordance_list = text.concordance_list("america", lines=2)
for entry in concordance_list:
    print(entry.line)


words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]
finder = nltk.collocations.TrigramCollocationFinder.from_words(words)

finder.ngram_fd.most_common(2)
finder.ngram_fd.tabulate(2)
