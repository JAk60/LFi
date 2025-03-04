from libc.stdlib cimport malloc, free
from libc.string cimport memcpy
from gensim.parsing.preprocessing import STOPWORDS
from gensim.models.keyedvectors import KeyedVectors
import gensim.matutils as gm
import numpy as np
cimport numpy as cnp
cimport cython

# Load the GloVe model
def load_glove_model():
    print("glove_w2v model loading")
    try:
        model = KeyedVectors.load_word2vec_format(
            "/home/user/IITB/LFi/helper/glove_w2v.txt", binary=False
        )
    except:
        model = KeyedVectors.load_word2vec_format(
            "/home/user/IITB/LFi/helper/glove_w2v.txt", binary=False
        )
    print("glove_w2v model loaded")
    return model

model = load_glove_model()


@cython.boundscheck(False)
@cython.wraparound(False)
def get_word_vectors(list[str] btw_words):
    cdef list word_vectors = []
    for word in btw_words:
        try:
            word_vectors.append(model[word])
        except KeyError:
            pass  # Store words not available in glove if needed
    return word_vectors

@cython.boundscheck(False)
@cython.wraparound(False)
def get_similarity(list word_vectors, str target_word):
    cdef double similarity = 0.0
    try:
        target_word_vector = model[target_word]
    except KeyError:
        return similarity  # Word not found in model
    
    target_word_sparse = gm.any2sparse(target_word_vector, eps=1e-9)
    for wv in word_vectors:
        wv_sparse = gm.any2sparse(wv, eps=1e-9)
        similarity = max(similarity, gm.cossim(wv_sparse, target_word_sparse))
    return similarity

@cython.boundscheck(False)
@cython.wraparound(False)
def preprocess(list[str] tokens):
    return [word for word in tokens if word not in STOPWORDS and word.isalpha()]

def word_similarity(str sentence, **kwargs):
    print("sentence---->>", sentence)
    cdef double similarity = 0.0
    words = preprocess(sentence.split())
    word_vectors = get_word_vectors(words)
    for w in kwargs["keywords"]:
        similarity = min(max(similarity, get_similarity(word_vectors, w)), 1.0)
    return similarity