"""
“United States”とコサイン類似度が高い10語と, その類似度を出力せよ
"""

from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin.gz', binary=True)

print(model.most_similar('United_States', topn=10))