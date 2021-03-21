from nltk import WhitespaceTokenizer
from collections import defaultdict
from collections import Counter
from random import choices

#file_name = input()
file_name = "corpus.txt"
wst = WhitespaceTokenizer()
with open(f"{file_name}", "r", encoding="utf-8") as corpus:
    raw_text = corpus.read()
tokenized_corpus = wst.tokenize(raw_text)

trigrams_list = []


def trigram_creation(tokens):
    """create list containing trigrams from given list with tokens"""
    global trigrams_list
    trigrams_list = []
    for n in range(0, len(tokens) - 2):
        trigrams_list.append([str(tokens[n]) + ' ' + str(tokens[n + 1]), tokens[n + 2]])


trigram_creation(tokenized_corpus)


def trigrams2dict(trigrams):
    """take a trigrams list and return a dictionary
    with heads as keys and another dict as value with all tails as keys and their counts as values """
    tails_collection = defaultdict(list)
    for h in trigrams:
        tails_collection.setdefault(h[0], []).append(h[1])
    for key in tails_collection:
        tails_collection[key] = Counter(tails_collection[key])
    return tails_collection


freq_dict = trigrams2dict(trigrams_list)

freq_dict_heads = []
for k in freq_dict:
    freq_dict_heads.append(k)

sentences_range = 0
while sentences_range < 10:
    random_head = choices(freq_dict_heads)
    random_head = str(random_head[0])
    if random_head[0].isupper() and random_head.split()[0][-1] not in [".", "!", "?"]:
        print(random_head, end=' ')
        sentences_range += 1
    else:
        continue

    words_range = 0
    while True:
        tails_dict = dict(freq_dict[random_head])
        tails_keys = []
        tails_weight = []
        for k, v in tails_dict.items():
            tails_keys.append(k)
            tails_weight.append(v)
        random_tail = choices(tails_keys, tails_weight)
        random_tail = str(random_tail[0])
        if words_range < 2 or random_tail[-1] not in [".", "!", "?"]:
            print(random_tail, end=' ')
            words_range += 1
        else:
            print(random_tail, end='')
            break
        random_head = random_head.split()[1] + " " + random_tail
    print('\n', end='')
