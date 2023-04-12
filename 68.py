"""
国名に関する単語ベクトルに対し,Ward法による階層型クラスタリングを実行せよ.
さらに，クラスタリング結果をデンドログラムとして可視化せよ．
"""

from gensim.models import KeyedVectors
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin.gz', binary=True)

# 国名の取得
countries = set()
with open('./questions-words-add.txt') as f:
    for line in f:
        line = line.split()
        if line[0] in ['capital-common-countries', 'capital-world']:
            countries.add(line[2])
        elif line[0] in ['currency', 'gram6-nationality-adjective']:
            countries.add(line[1])
countries = list(countries)

# 単語ベクトルの取得
countries_vec = [model[country] for country in countries]

plt.figure(figsize=(15, 5))
Z = linkage(countries_vec, method='ward')
dendrogram(Z, labels=countries)
plt.savefig('68.jpg')
