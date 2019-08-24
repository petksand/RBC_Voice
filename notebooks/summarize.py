# Importing All The Necessary Libraries
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance 
import numpy as np
import networkx as nx
import os
import path
from functools import reduce

# Levenshtein Distance Function
def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y
          
    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    return (matrix[size_x - 1, size_y - 1])

# Generate Clean Sentences
def read_article(file_name):
    file = open(file_name, "r")
    filedata = file.readlines()
    article = list(filter(lambda paragraph: paragraph != '\n', filedata))
    article = reduce(lambda acc, s: acc + s, article, '')
    article = article.split('. ')
    sentences = []
    for sentence in article:
      sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    
    sentences.pop() 
    
    return sentences

# Generates Sentence Similarity
def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1

    return levenshtein(vector1, vector2)
    #return 1 - cosine_distance(vector1, vector2)


# Similarity Matrix
def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)
    return similarity_matrix

# Generate Summary Method
def generate_summary(sentences, top_n=5):
    stop_words = stopwords.words('english')
    summarize_text = []

    # Step 2 - Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    # Step 3 - Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
    #print("\nIndexes of top ranked_sentence order are ", ranked_sentence)    

    top_n = len(ranked_sentence) if top_n > len(ranked_sentence) else top_n
    
    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentence[i][1]))

    # Step 5 - Offcourse, output the summarize text
    print("Summarize Text: \n-", ".\n- ".join(summarize_text))
    print("Done!")

# Generate Summary Method
# cwd = os.getcwd()
# generate_summary(cwd + "\\sample-wiki.txt", 5)