# Cristian Starting his NLP Learning

# April 20, 2019


## 1.3 Searching Text
A concordance view shows us every occurrence of a given word, together with some context.
- `text1.concordance("monstrous")`

```
Displaying 11 of 11 matches:
ong the former , one was of a most monstrous size . ... This came towards us ,
ON OF THE PSALMS . " Touching that monstrous bulk of the whale or ork we have r
ll over with a heathenish array of monstrous clubs and spears . Some were thick
d as you gazed , and wondered what monstrous cannibal and savage could ever hav
that has survived the flood ; most monstrous and most mountainous ! That Himmal
they might scout at Moby Dick as a monstrous fable , or still worse and more de
th of Radney .'" CHAPTER 55 Of the monstrous Pictures of Whales . I shall ere l
ing Scenes . In connexion with the monstrous pictures of whales , I am strongly
ere to enter upon those still more monstrous stories of them which are to be fo
ght have been rummaged out of this monstrous cabinet there is no telling . But
of Whale - Bones ; for Whales of a monstrous size are oftentimes cast up dead u 
```

A concordance permits us to see words in context. For example, we saw that monstrous occurred in contexts such as the ___ pictures and a ___ size . What other words appear in a similar range of contexts? We can find out by appending the term similar to the name of the text in question, then inserting the relevant word in parentheses:
- `text1.similar("monstrous")`
```
mean part maddens doleful gamesome subtly uncommon careful untoward
exasperate loving passing mouldy christian few true mystifying
imperial modifies contemptible
```

The term common_contexts allows us to examine just the contexts that are shared by two or more words, such as monstrous and very. We have to enclose these words by square brackets as well as parentheses, and separate them with a comma:
- `text2.common_contexts(["monstrous", "very"])`
```
a_pretty is_pretty am_glad be_glad a_lucky
```

## 1.4 Counting Vocabulary
Let's begin by finding out the length of a text from start to finish, in terms of the words and punctuation symbols that appear.
- `len(text3)`
```
44764
```

A token is the technical name for a sequence of characters — such as hairy, his, or :) — that we want to treat as a group. When we count the number of tokens in a text, say, the phrase to be or not to be, we are counting occurrences of these sequences. 
 - `sorted(set(text3))`
 ```
 ['!', "'", '(', ')', ',', ',)', '.', '.)', ':', ';', ';)', '?', '?)',
'A', 'Abel', 'Abelmizraim', 'Abidah', 'Abide', 'Abimael', 'Abimelech',
'Abr', 'Abrah', 'Abraham', 'Abram', 'Accad', 'Achbor', 'Adah', ...]
 ```

A word type is the form or spelling of the word independently of its specific occurrences in a text — that is, the word considered as a unique item of vocabulary. Our count of 2,789 items will include punctuation symbols, so we will generally call these unique items types instead of word types.
- `len(set(text3)) / len(text3)`
```
 0.06230453042623537
```

Next, let's focus on particular words. We can count how often a word occurs in a text, and compute what percentage of the text is taken up by a specific word:
- `text3.count("smote")`
```
5
```

Instead, you can come up with your own name for a task, like "lexical_diversity" or "percentage", and associate it with a block of code. Now you only have to type a short name instead of one or more complete lines of Python code, and you can re-use it as often as you like.
 ```
 def lexical_diversity(text):
 	return len(set(text)) / len(text)
 ```

## 2. A Closer Look at Python: Texts as Lists of Words

## 2.1 Lists
 Here's how we represent text in Python, in this case the opening sentence of Moby Dick:
 - `sent1 = ['Call', 'me', 'Ishmael', '.']`

## 3 Computing with Language: Simple Statistics

## 3.1   Frequency Distributions
A frequency distribution, and it tells us the frequency of each vocabulary item in the text. (In general, it could count any kind of observable event.) It is a "distribution" because it tells us how the total number of word tokens in the text are distributed across the vocabulary items. Since we often need frequency distributions in language processing, NLTK provides built-in support for them. Let's use a FreqDist to find the 50 most frequent words of Moby Dick:
- `fdist1 = FreqDist(text1)`
```
<FreqDist with 19317 samples and 260819 outcomes>
```
- `fdist1.most_common(50)`
```
[(',', 18713), ('the', 13721), ('.', 6862), ('of', 6536), ('and', 6024),
('a', 4569), ('to', 4542), (';', 4072), ('in', 3916), ('that', 2982),
("'", 2684), ('-', 2552), ('his', 2459), ('it', 2209), ('I', 2124),
('s', 1739), ('is', 1695), ('he', 1661), ('with', 1659), ('was', 1632),
('as', 1620), ('"', 1478), ('all', 1462), ('for', 1414), ('this', 1280),
('!', 1269), ('at', 1231), ('by', 1137), ('but', 1113), ('not', 1103),
('--', 1070), ('him', 1058), ('from', 1052), ('be', 1030), ('on', 1005),
('so', 918), ('whale', 906), ('one', 889), ('you', 841), ('had', 767),
('have', 760), ('there', 715), ('But', 705), ('or', 697), ('were', 680),
('now', 646), ('which', 640), ('?', 637), ('me', 627), ('like', 624)]
```

## 3.2 Fine-grained Selection of Words
The corresponding Python expression is given in (1b). (Note that it produces a list, not a set, which means that duplicates are possible.) Observe how similar the two notations are. Let's go one more step and write executable Python code:
- `V = set(text1)`
- `long_words = [w for w in V if len(w) > 15]`
- `sorted(long_words)`
```
['CIRCUMNAVIGATION', 'Physiognomically', 'apprehensiveness', 'cannibalistically',
'characteristically', 'circumnavigating', 'circumnavigation', 'circumnavigations',
'comprehensiveness', 'hermaphroditical', 'indiscriminately', 'indispensableness',
'irresistibleness', 'physiognomically', 'preternaturalness', 'responsibilities',
'simultaneousness', 'subterraneousness', 'supernaturalness', 'superstitiousness',
'uncomfortableness', 'uncompromisedness', 'undiscriminating', 'uninterpenetratingly']
```

## 3.3 Collocations and Bigrams
A collocation is a sequence of words that occur together unusually often. Thus red wine is a collocation, whereas the wine is not. A characteristic of collocations is that they are resistant to substitution with words that have similar senses; for example, maroon wine sounds definitely odd.
- `list(bigrams(['more', 'is', 'said', 'than', 'done']))`
```
[('more', 'is'), ('is', 'said'), ('said', 'than'), ('than', 'done')]
```

Here we see that the pair of words than-done is a bigram, and we write it in Python as ('than', 'done'). Now, collocations are essentially just frequent bigrams, except that we want to pay more attention to the cases that involve rare words. In particular, we want to find bigrams that occur more often than we would expect based on the frequency of the individual words. The collocations() function does this for us. We will see how it works later.
- `text4.collocations()`
```
United States; fellow citizens; four years; years ago; Federal
Government; General Government; American people; Vice President; Old
World; Almighty God; Fellow citizens; Chief Magistrate; Chief Justice;
God bless; every citizen; Indian tribes; public debt; one another;
foreign nations; political parties
```

## 3.4 Counting Other Things
Counting words is useful, but we can count other things too. For example, we can look at the distribution of word lengths in a text, by creating a FreqDist out of a long list of numbers, where each number is the length of the corresponding word in the text:
```
>>> [len(w) for w in text1] [1]
[1, 4, 4, 2, 6, 8, 4, 1, 9, 1, 1, 8, 2, 1, 4, 11, 5, 2, 1, 7, 6, 1, 3, 4, 5, 2, ...]
>>> fdist = FreqDist(len(w) for w in text1)  [2]
>>> print(fdist)  [3]
<FreqDist with 19 samples and 260819 outcomes>
>>> fdist
FreqDist({3: 50223, 1: 47933, 4: 42345, 2: 38513, 5: 26597, 6: 17111, 7: 14399,
  8: 9966, 9: 6428, 10: 3528, ...})
>>>
```

### Functions Defined for NLTK's Frequency Distributions
```
Example							Description
fdist = FreqDist(samples)	create a frequency distribution containing the given samples
fdist[sample] += 1			increment the count for this sample
fdist['monstrous']			count of the number of times a given sample occurred
fdist.freq('monstrous')		frequency of a given sample
fdist.N()					total number of samples
fdist.most_common(n)		the n most common samples and their frequencies
for sample in fdist:		iterate over the samples
fdist.max()					sample with the greatest count
fdist.tabulate()			tabulate the frequency distribution
fdist.plot()				graphical plot of the frequency distribution
fdist.plot(cumulative=True)	cumulative plot of the frequency distribution
fdist1 |= fdist2			update fdist1 with counts from fdist2
fdist1 < fdist2				test if samples in fdist1 occur less frequently than in fdist2
```

## 4 Back to Python: Making Decisions and Taking Control

## 4.1 Conditionals
We can use these to select different words from a sentence of news text. Here are some examples — only the operator is changed from one line to the next. They all use sent7, the first sentence from text7 (Wall Street Journal). As before, if you get an error saying that sent7 is undefined, you need to first type: from nltk.book import *

```
>>> sent7
['Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'will', 'join', 'the',
'board', 'as', 'a', 'nonexecutive', 'director', 'Nov.', '29', '.']
>>> [w for w in sent7 if len(w) < 4]
[',', '61', 'old', ',', 'the', 'as', 'a', '29', '.']
>>> [w for w in sent7 if len(w) <= 4]
[',', '61', 'old', ',', 'will', 'join', 'the', 'as', 'a', 'Nov.', '29', '.']
>>> [w for w in sent7 if len(w) == 4]
['will', 'join', 'Nov.']
>>> [w for w in sent7 if len(w) != 4]
['Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'the', 'board',
'as', 'a', 'nonexecutive', 'director', '29', '.']
>>>
```

Some Word Comparison Operators
```
Function				Meaning
s.startswith(t)		test if s starts with t
s.endswith(t)		test if s ends with t
t in s				test if t is a substring of s
s.islower()			test if s contains cased characters and all are lowercase
s.isupper()			test if s contains cased characters and all are uppercase
s.isalpha()			test if s is non-empty and all characters in s are alphabetic
s.isalnum()			test if s is non-empty and all characters in s are alphanumeric
s.isdigit()			test if s is non-empty and all characters in s are digits
s.istitle()			test if s contains cased characters and is titlecased (i.e. all words in s have initial capitals)
```

Here are some examples of these operators being used to select words from our texts: words ending with -ableness; words containing gnt; words having an initial capital; and words consisting entirely of digits.

```
>>> sorted(w for w in set(text1) if w.endswith('ableness'))
['comfortableness', 'honourableness', 'immutableness', 'indispensableness', ...]
>>> sorted(term for term in set(text4) if 'gnt' in term)
['Sovereignty', 'sovereignties', 'sovereignty']
>>> sorted(item for item in set(text6) if item.istitle())
['A', 'Aaaaaaaaah', 'Aaaaaaaah', 'Aaaaaah', 'Aaaah', 'Aaaaugh', 'Aaagh', ...]
>>> sorted(item for item in set(sent7) if item.isdigit())
['29', '61']
>>>
```

## 4.2 Operating on Every Element
In 3, we saw some examples of counting items other than words. Let's take a closer look at the notation we used:
```
>>> [len(w) for w in text1]
[1, 4, 4, 2, 6, 8, 4, 1, 9, 1, 1, 8, 2, 1, 4, 11, 5, 2, 1, 7, 6, 1, 3, 4, 5, 2, ...]
>>> [w.upper() for w in text1]
['[', 'MOBY', 'DICK', 'BY', 'HERMAN', 'MELVILLE', '1851', ']', 'ETYMOLOGY', '.', ...]
>>>

```

Let's return to the question of vocabulary size, and apply the same idiom here:
```
>>> len(text1)
260819
>>> len(set(text1))
19317
>>> len(set(word.lower() for word in text1))
17231
>>>
```

## 4.4 Looping with Conditions
Now we can combine the if and for statements. We will loop over every item of the list, and print the item only if it ends with the letter l. We'll pick another name for the variable to demonstrate that Python doesn't try to make sense of variable names.
```
>>> sent1 = ['Call', 'me', 'Ishmael', '.']
>>> for xyzzy in sent1:
...     if xyzzy.endswith('l'):
...         print(xyzzy)
...
Call
Ishmael
>>>
```

## 5 Automatic Natural Language Understanding

## 5.1 Word Sense Disambiguation

In word sense disambiguation we want to work out which sense of a word was intended in a given context. Consider the ambiguous words serve and dish:

```
(2)		
	a.		serve: help with food or drink; hold an office; put ball into play

	b.		dish: plate; course of a meal; communications device

```











