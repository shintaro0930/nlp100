"""
“Spain”の単語ベクトルから”Madrid”のベクトルを引き,
”Athens”のベクトルを足したベクトルを計算し,そのベクトルと類似度の高い10語とその類似度を出力せよ.
"""

from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin.gz', binary=True)

vec = model['Spain'] - model['madrid'] + model['Athens'] 
print(model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=10))

